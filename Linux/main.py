import subprocess
import shutil
from pathlib import Path

input_folder = Path(input("Introduce ruta:").strip()).expanduser()
quality = 80
ext = [".png", ".jpg", ".jpeg"]

del_original = input("¿Eliminar los archivos originales después de convertir? (s/n): ").strip().lower() == "s"

cwebp_path = shutil.which("cwebp")
if cwebp_path is None:
    print("No se encontró cwebp. Instala el paquete 'webp'.")
    exit(1)

if not input_folder.exists():
    print(f"La ruta '{input_folder}' no existe.")
else:
    for image_path in input_folder.rglob("*"):
        if image_path.suffix.lower() in ext:
            webp_path = image_path.with_suffix(".webp")

            cmd = [
                str(cwebp_path),
                "-q", str(quality),
                str(image_path),
                "-o", str(webp_path)
            ]

            try:
                subprocess.run(cmd, check=True)
                print(f"Convertido: {image_path} -> {webp_path}")

                if del_original:
                    image_path.unlink()
                    print(f"Eliminado: {image_path}")

            except subprocess.CalledProcessError as e:
                print(f"Error al convertir {image_path}: {e}")
