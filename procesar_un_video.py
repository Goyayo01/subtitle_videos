import os
import subprocess

# Configura la ruta del video y la carpeta de salida
RUTA_VIDEO = "C:\\Users\\john_\\OneDrive\\Pictures\\dante\\prueba.mp4"  # Cambia esto si es necesario
CARPETA_SUBTITULOS = "subtitulos"

if not os.path.exists(RUTA_VIDEO):
    print(f"El video no existe en la ruta proporcionada: {RUTA_VIDEO}")
else:
    print("Archivo encontrado. Procediendo con el procesamiento.")


# Crea la carpeta de subtítulos si no existe
if not os.path.exists(CARPETA_SUBTITULOS):
    os.makedirs(CARPETA_SUBTITULOS)

# Procesa un único video
def generar_subtitulo():
    if not os.path.exists(RUTA_VIDEO):
        print(f"El video no existe: {RUTA_VIDEO}")
        return

    nombre_base = os.path.splitext(os.path.basename(RUTA_VIDEO))[0]
    ruta_subtitulo = os.path.join(CARPETA_SUBTITULOS, f"{nombre_base}.srt")

    print(f"Procesando: {RUTA_VIDEO}")
    try:
        # Ejecuta Whisper para generar subtítulos
        subprocess.run(
            [
                "whisper",
                RUTA_VIDEO,
                "--language", "es",
                "--output_format", "srt",
                "--output_dir", CARPETA_SUBTITULOS
            ],
            check=True
        )
        print(f"Subtítulo generado: {ruta_subtitulo}")
    except subprocess.CalledProcessError as e:
        print(f"Error al procesar el video: {e}")

# Ejecuta la función
if __name__ == "__main__":
    generar_subtitulo()
