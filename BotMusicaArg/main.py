import discord
from discord.ext import commands
import yt_dlp
import asyncio

# 1. MOTOR DE AUDIO
discord.opus.load_opus('/opt/homebrew/lib/libopus.dylib')

# 2. CONFIGURACIÓN
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

ytdl_format_options = {
    'format': 'bestaudio/best',
    'noplaylist': True,
    'nocheckcertificate': True,
    'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'cookiefile': 'cookies.txt' # Esto lee tu archivo de cookies
}

ffmpeg_options = {
    'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
    'options': '-vn',
    'executable': '/opt/homebrew/bin/ffmpeg'
}

ytdl = yt_dlp.YoutubeDL(ytdl_format_options)

class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)
        self.data = data
        self.title = data.get('title')

    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))
        if 'entries' in data:
            data = data['entries'][0]
        filename = data['url'] if stream else ytdl.prepare_filename(data)
        return cls(discord.FFmpegPCMAudio(filename, **ffmpeg_options), data=data)

# 3. COMANDOS
@bot.event
async def on_ready():
    print(f'¡VAMOS! Sabadino está online.')
    print(f'Comandos activos: {[c.name for c in bot.commands]}')

@bot.command()
async def join(ctx):
    if not ctx.author.voice:
        return await ctx.send("Metete a un canal de voz, Santi.")
    channel = ctx.author.voice.channel
    await channel.connect()

@bot.command()
async def play(ctx, *, url):
    if ctx.voice_client is None:
        if ctx.author.voice:
            await ctx.author.voice.channel.connect()
        else:
            return await ctx.send("Entrá a un canal de voz primero.")

    async with ctx.typing():
        try:
            player = await YTDLSource.from_url(url, loop=bot.loop, stream=True)
            ctx.voice_client.play(player)
            await ctx.send(f'Reproduciendo: **{player.title}**')
        except Exception as e:
            await ctx.send(f"Error: {e}")

@bot.command()
async def stop(ctx):
    if ctx.voice_client:
        await ctx.voice_client.disconnect()



@bot.command()
async def pause(ctx):
    if ctx.voice_client and ctx.voice_client.is_playing():
        ctx.voice_client.pause()
        await ctx.send("⏸️ Música pausada.")

        @bot.command()
        async def resume(ctx):
            if ctx.voice_client and ctx.voice_client.is_paused():
                ctx.voice_client.resume()
        await ctx.send("▶️ Seguimos con el baile.")

        @bot.command()
        async def stop(ctx):
            if ctx.voice_client:
                await ctx.voice_client.disconnect()
                await ctx.send("👋 ¡Nos vemos!, Limpiando conexión...")

    bot.run('TU_TOKEN_ACA')