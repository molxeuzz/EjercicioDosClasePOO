from rich.console import Console
from rich.text import Text

console = Console()

class Estudiante:
    def __init__(self, nombre: str, identificacion: str):
        self.nombre = nombre
        self.identificacion = identificacion
        self.calificaciones = []

    def agregar_calificacion(self, nota: float):
        if 0 <= nota <= 10:
            self.calificaciones.append(nota)
            console.print(f"[green]Calificación {nota} añadida a {self.nombre}.[/green]")
        else:
            console.print("[red]Error: La calificación debe estar entre 0 y 10.[/red]")

    def calcular_promedio(self):
        if not self.calificaciones:
            console.print("[yellow]No hay calificaciones registradas para este estudiante.[/yellow]")
            return None
        return sum(self.calificaciones) / len(self.calificaciones)

    def __str__(self):
        return f"{self.nombre} ({self.identificacion})"
