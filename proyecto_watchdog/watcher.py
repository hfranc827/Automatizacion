from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
import shutil
import os

CARPETA_ENTRADA = "entrada"
CARPETA_PROCESADOS = "procesados"


class ManejadorArchivos(FileSystemEventHandler):

    def on_created(self, event):
        # Ignorar carpetas, solo archivos
        if event.is_directory:
            return

        archivo = event.src_path

        # Solo trabajar con archivos .txt
        if archivo.endswith(".txt"):
            nombre = os.path.basename(archivo)
            destino = os.path.join(CARPETA_PROCESADOS, nombre)

            time.sleep(1)  # Espera para evitar errores de acceso
            shutil.move(archivo, destino)

            print(f"Archivo movido: {nombre}")


if __name__ == "__main__":
    observer = Observer()
    observer.schedule(ManejadorArchivos(), CARPETA_ENTRADA, recursive=False)
    observer.start()

    print("👀 Vigilando la carpeta 'entrada'... (Ctrl+C para salir)")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()
