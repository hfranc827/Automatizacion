from rich.table import Table
from rich.console import Console

console = Console()

table = Table(title="Usuarios del sistema")

table.add_column("ID", style="cyan")
table.add_column("Nombre", style="green")
table.add_column("Rol", style="magenta")

table.add_row("1", "Hector", "Admin")
table.add_row("2", "Ana", "Usuario")
table.add_row("3", "Luis", "Invitado")

console.print(table)
