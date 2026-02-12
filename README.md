# 🎵 Sabadino - DJ Bot para Discord

¡Hola! Soy **Santi**, estudiante de la Tecnicatura Universitaria en Programación en la **UTN FRBB**. Este es mi primer proyecto de automatización: un bot de música para Discord optimizado para correr en **macOS (M1)**.

## 🚀 Funcionalidades
- 🔊 Reproducción de audio de alta calidad.
- ☁️ Integración con **SoundCloud** (solución estable ante bloqueos de YouTube).
- 🛠️ Comandos de control: `!play`, `!pause`, `!resume` y `!stop`.

## 🛠️ Tecnologías y Desafíos
Para este proyecto utilicé:
- **Python 3.12+** y la librería `discord.py`.
- **FFmpeg** y **Opus**: Configurados específicamente para arquitectura **Apple Silicon (M1)**.
- **yt-dlp**: Para la extracción dinámica de audio.

### Aprendizajes Clave:
Durante el desarrollo aprendí a gestionar **autenticación por tokens**, manejo de **dependencias de audio** y resolución de errores de servidor (como el famoso HTTP 403 de YouTube).

## 📋 Requisitos
Si querés probarlo, necesitás tener instalado en tu Mac:
- Python
- FFmpeg (`brew install ffmpeg`)
- Un token de bot de Discord

---
*Este proyecto es parte de mi camino hacia convertirme en Desarrollador Full Stack. ¡Gracias por pasar!*
