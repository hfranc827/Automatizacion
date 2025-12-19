""" import typer

app = typer.Typer()

@app.command()
def saludar(nombre: str):
    
    # Saluda a una persona por su nombre
    
    print(f"Hola {nombre}, bienvenido a Python 🚀")


if __name__ == "__main__":
    app()
 """

import typer
import shutil
import os

app = typer.Typer()

@app.command()
def mover(archivo: str, destino: str):
    """
    Mueve un archivo a otra carpeta
    """
    if not os.path.exists(archivo):
        typer.echo("❌ El archivo no existe")
        raise typer.Exit(code=1)

    shutil.move(archivo, destino)
    typer.echo(f"✅ Archivo movido a {destino}")


if __name__ == "__main__":
    app()
