from rich.console import Console
from rich.prompt import Prompt
from rich.table import Table
from app.estudiante import Estudiante
from app.curso import Curso

console = Console()
curso = Curso("Programación en Python")

def menu():
    while True:
        console.print("\n[cyan]Menú de opciones:[/cyan]")
        console.print("1. Agregar estudiante al curso")
        console.print("2. Listar estudiantes en el curso")
        console.print("3. Agregar calificación a un estudiante")
        console.print("4. Calcular promedio de un estudiante")
        console.print("5. Salir")

        opcion = Prompt.ask("\n[bold green]Elige una opción[/bold green]")

        if opcion == "1":
            nombre = Prompt.ask("Nombre del estudiante")
            identificacion = Prompt.ask("Identificación del estudiante")
            curso.agregar_estudiante(Estudiante(nombre, identificacion))

        elif opcion == "2":
            curso.listar_estudiantes()

        elif opcion == "3":
            nombre = Prompt.ask("Nombre del estudiante")
            estudiante = curso.buscar_estudiante(nombre)
            if estudiante:
                try:
                    nota = float(Prompt.ask("Ingrese la calificación (0-10)"))
                    estudiante.agregar_calificacion(nota)
                except ValueError:
                    console.print("[red]Error: Debes ingresar un número válido.[/red]")

        elif opcion == "4":
            nombre = Prompt.ask("Nombre del estudiante")
            estudiante = curso.buscar_estudiante(nombre)
            if estudiante:
                promedio = estudiante.calcular_promedio()
                if promedio is not None:
                    console.print(f"[blue]El promedio de {nombre} es {promedio:.2f}[/blue]")

        elif opcion == "5":
            console.print("[bold green]Saliendo del programa...[/bold green]")
            break

        else:
            console.print("[red]Opción no válida. Inténtalo de nuevo.[/red]")

if __name__ == "__main__":
    menu()
