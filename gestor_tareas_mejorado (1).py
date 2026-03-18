"""
SISTEMA DE LISTA DE TAREAS PERSONAL
Autores:
- Rogger Bernita Henriquez
- Alexis Reina del Rosario

Descripción General:
Gestor de Tareas Pro es una aplicación de línea de comandos (CLI)
que permite gestionar tareas mediante operaciones CRUD:
Crear, Leer, Actualizar y Eliminar.

Características:
- Agregar tareas
- Ver tareas
- Completar tareas
- Eliminar tareas
- Interfaz con emojis
- Limpieza de pantalla automática

Requisitos:
- Python 3.6 o superior
- Compatible con Windows, Linux y macOS
"""

import os

# ==============================
# VARIABLE GLOBAL
# ==============================
# Lista que almacena todas las tareas
tasks = []


def limpiar_pantalla():
    """
    Limpia la pantalla de la terminal.

    Detecta el sistema operativo:
    - Windows: usa 'cls'
    - Linux/macOS: usa 'clear'

    Returns:
        None
    """
    os.system("cls" if os.name == "nt" else "clear")


def mostrar_menu():
    """
    Muestra el menú principal del sistema.

    Presenta las opciones disponibles al usuario:
    1. Agregar tarea
    2. Ver tareas
    3. Completar tarea
    4. Eliminar tarea
    5. Salir

    Returns:
        None
    """
    print("\n" + "="*35)
    print("📋  GESTOR DE TAREAS PRO")
    print("="*35)
    print("1. ➕ Agregar tarea")
    print("2. 📋 Ver tareas")
    print("3. ✔️ Completar tarea")
    print("4. 🗑️ Eliminar tarea")
    print("5. 🚪 Salir")


def agregar_tarea():
    """
    Permite al usuario agregar una nueva tarea.

    Solicita un título al usuario y valida que no esté vacío.
    Si es válido, se agrega a la lista 'tasks' con estado "Pendiente".

    Returns:
        None

    Example:
        >>> agregar_tarea()
        📝 Ingresa la tarea: Estudiar Python
        ✅ Tarea agregada
    """
    titulo = input("📝 Ingresa la tarea: ").strip()
    if titulo:
        tasks.append({"titulo": titulo, "estado": "Pendiente"})
        print("✅ Tarea agregada")
    else:
        print("❌ No puedes agregar una tarea vacía")


def ver_tareas():
    """
    Muestra todas las tareas almacenadas.

    - Si no hay tareas, muestra mensaje informativo.
    - Si existen, las enumera con su estado:
        ⏳ Pendiente
        ✅ Completada

    Returns:
        None
    """
    print("\n📋 LISTA DE TAREAS")
    print("-"*35)
    if not tasks:
        print("No hay tareas aún")
    else:
        for i, t in enumerate(tasks):
            estado = "✅" if t["estado"] == "Completada" else "⏳"
            print(f"{i+1}. {estado} {t['titulo']}")


def completar_tarea():
    """
    Marca una tarea como completada.

    Flujo:
    1. Muestra la lista de tareas
    2. Solicita el número de tarea
    3. Cambia su estado a "Completada"

    Manejo de errores:
    - Si el usuario ingresa un valor inválido, muestra error

    Returns:
        None
    """
    ver_tareas()
    try:
        num = int(input("✔️ Número de tarea: "))
        tasks[num-1]["estado"] = "Completada"
        print("🎉 Tarea completada")
    except:
        print("❌ Número inválido")


def eliminar_tarea():
    """
    Elimina una tarea de la lista.

    Flujo:
    1. Muestra las tareas
    2. Solicita el número de tarea
    3. Elimina la tarea usando pop()

    Manejo de errores:
    - Captura índices inválidos o entradas incorrectas

    Returns:
        None
    """
    ver_tareas()
    try:
        num = int(input("🗑️ Número de tarea a eliminar: "))
        tarea = tasks.pop(num-1)
        print(f"🗑️ Eliminaste: {tarea['titulo']}")
    except:
        print("❌ Número inválido")


# ==============================
# BUCLE PRINCIPAL
# ==============================
"""
Flujo del programa:

1. Limpia pantalla
2. Muestra menú
3. Usuario elige opción
4. Se ejecuta función correspondiente
5. Se repite hasta que elija salir
"""

while True:
    limpiar_pantalla()
    mostrar_menu()
    opcion = input("\n👉 Elige una opción: ")

    if opcion == "1":
        agregar_tarea()
    elif opcion == "2":
        ver_tareas()
    elif opcion == "3":
        completar_tarea()
    elif opcion == "4":
        eliminar_tarea()
    elif opcion == "5":
        print("👋 Hasta luego")
        break
    else:
        print("❌ Opción inválida")

    input("\nPresiona ENTER para continuar...")
