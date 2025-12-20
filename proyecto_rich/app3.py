from rich.progress import track
import time

for i in track(range(10), description="Procesando archivos..."):
    time.sleep(0.5)
