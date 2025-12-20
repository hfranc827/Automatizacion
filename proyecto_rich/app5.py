import typer
from rich.table import Table
from rich.console import Console

app = typer.Typer()
console = Console()

@app.command()
def usuarios():
    table = Table(title="Usuarios Registrados")

    table.add_column("ID", justify="right")
    table.add_column("Nombre", style="green")
    table.add_column("Rol", style="cyan")

    table.add_row("1", "Hector", "Admin")
    table.add_row("2", "Ana", "Usuario")
    table.add_row("3", "Luis", "Invitado")

    console.print(table)

if __name__ == "__main__":
    app()
