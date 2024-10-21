"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

class State(rx.State):
    def __init__(self):
        super().__init__()
        self.mostrar_solo_pendientes = False
        
    def mostrar_pendientes(self):
        self.mostrar_solo_pendientes = True

def tarjeta_tarea(tarea):
    return rx.div(
        tarea["titulo"],
        # ... otros detalles de la tarea
    )

def columna_kanban(nombre, tareas):
    if State.mostrar_solo_pendientes:
        tareas = [t for t in tareas if t["estado"] == "Pendiente"]
    
    return rx.div(
        rx.heading(nombre),
        rx.div(
            [tarjeta_tarea(tarea) for tarea in tareas]
        )
    )

def index():
    # Ejemplo de datos de tareas
    tareas_en_progreso = [
        {"titulo": "Tarea 1", "estado": "Pendiente"},
        {"titulo": "Tarea 2", "estado": "En Progreso"},
    ]
    tareas_completadas = [
        {"titulo": "Tarea 3", "estado": "Completada"},
        {"titulo": "Tarea 4", "estado": "Pendiente"},
    ]

    return rx.div(
        rx.button("Mostrar Pendientes", on_click=State.mostrar_pendientes),
        columna_kanban("En Progreso", tareas_en_progreso),
        columna_kanban("Completadas", tareas_completadas)
    )

# Definir la instancia de la aplicación
app = rx.App(state=State)

# Agregar el componente raíz al aplicativo
app.add_page(index)
app.compile()
