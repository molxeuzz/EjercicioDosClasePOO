from rich.console import Console
from app.estudiante import Estudiante

console = Console()

class Curso:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.estudiantes = []

    def agregar_estudiante(self, estudiante: Estudiante):
        self.estudiantes.append(estudiante)
        console.print(f"[green]Estudiante {estudiante.nombre} agregado al curso {self.nombre}.[/green]")

    def listar_estudiantes(self):
        if not self.estudiantes:
            console.print("[yellow]No hay estudiantes inscritos en el curso.[/yellow]")
        else:
            console.print("[blue]Estudiantes en el curso:[/blue]")
            for estudiante in self.estudiantes:
                console.print(f"- {estudiante}")

    def buscar_estudiante(self, nombre: str):
        for estudiante in self.estudiantes:
            if estudiante.nombre.lower() == nombre.lower():
                return estudiante
        console.print("[red]Estudiante no encontrado.[/red]")
        return None
