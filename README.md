# Sistema de Gestión de Estudiantes y Calificaciones

## Descripción General
Este proyecto implementa un sistema para gestionar estudiantes en un curso, permitiendo la administración de sus calificaciones y el cálculo de sus promedios utilizando Programación Orientada a Objetos (POO) en Python. El sistema permite registrar estudiantes, asignarles calificaciones y calcular sus promedios mediante un menú interactivo en la consola.

## Requisitos del Sistema
El sistema cuenta con las siguientes clases:

### Clase `Estudiante`
**Atributos:**
- `nombre` (str): Nombre del estudiante.
- `identificacion` (str): Identificación única del estudiante.
- `calificaciones` (list): Lista de calificaciones del estudiante.

**Métodos:**
- `agregar_calificacion(nota: float)`: Agrega una calificación al estudiante si está en el rango de 0 a 10.
- `calcular_promedio()`: Retorna el promedio de las calificaciones del estudiante. Si no tiene calificaciones, muestra un mensaje indicando que no hay registros.

### Clase `Curso`
**Atributos:**
- `nombre` (str): Nombre del curso.
- `estudiantes` (list): Lista de estudiantes inscritos en el curso.

**Métodos:**
- `agregar_estudiante(estudiante: Estudiante)`: Agrega un estudiante a la lista de inscritos en el curso.
- `listar_estudiantes()`: Muestra la lista de estudiantes inscritos en el curso.

## Interacción con el Usuario (Menú de Opciones)
El sistema permite al usuario interactuar a través de un menú en la consola con las siguientes opciones:

1. **Agregar estudiante al curso**: Permite registrar un nuevo estudiante en el curso solicitando su nombre e identificación.
2. **Listar estudiantes en el curso**: Muestra los nombres de todos los estudiantes inscritos en el curso.
3. **Agregar calificación a un estudiante**: Permite ingresar el nombre de un estudiante y añadirle una calificación, validando que esté dentro del rango permitido (0 a 10).
4. **Calcular promedio de un estudiante**: Permite ingresar el nombre de un estudiante y calcular su promedio de calificaciones.
5. **Salir**: Finaliza la ejecución del programa.

## Restricciones
- Se debe validar la existencia del estudiante antes de agregarle calificaciones o calcular su promedio.
- Las calificaciones deben estar en el rango de 0 a 10.
- Se debe manejar correctamente la entrada de datos del usuario para evitar errores.

## Tecnologías Utilizadas
- Python 3
- Programación Orientada a Objetos (POO)
- Python UV
- Python Rich

## Instalación y Ejecución
1. Clonar este repositorio.
2. Ejecutar el script principal con Python:
   ```sh
   python -m app.main
