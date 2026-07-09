# Conversor a WEBP

Este script convierte los formatos `.PNG`, `.JPG` y `.JPEG` a `.WEBP` para optimizar las imágenes.

## Requisitos:
### Linux:

  - Tener instalado `Python`.
    
  - Necesario tener instalado el paquete `webp`.
    
    - Ubuntu/Debian:
      ```
      sudo apt install webp
      ```
    - Fedora:
      ```
      sudo dnf install libwebp-tools
      ```
    - Arch Linux:
      ```
      sudo pacman -S libwebp
      ```
    - OpenSUSE:
      ```
      sudo zypper install libwebp-tools
      ```

### Windows:

  Se puede usar de dos maneras:
  1. **Usando el código fuente:**

     - Tener Python instalado previamente y descargar WebP desde **[AQUÍ](https://developers.google.com/speed/webp/download?hl=es-419)**. Debes pulsar donde diga **`Descargar para Windows`**. Si usas el código fuente, cuando descargues WebP debes de descomprimir el `.zip` y poner el directorio generado donde se encuentre el `main.py` para la versión de Windows.
     
  2. **Código compilado a `.exe`:**
  
     - Este no necesita descargar WebP, ya viene embebido dentro del código. Puedes descargar el binario desde **[AQUÍ](https://github.com/JotaQC/Conversor-a-WEBP/releases/tag/v1.0)**. 
