import reflex as rx

def contar_tareas_por_estado(tareas):
    contadores = {}
    for tarea in tareas:
        estado = tarea["estado"]
        if estado in contadores:
            contadores[estado] += 1
        else:
            contadores[estado] = 1
    return contadores

def tarjeta_tarea(tarea):
    return rx.div(
        tarea["titulo"],
    )

def columna_kanban(nombre_columna, tareas):
    return rx.div(
        rx.heading(nombre_columna),
        rx.div(
            [tarjeta_tarea(tarea) for tarea in tareas]
        )
    )

def tablero_kanban():
    tareas_en_progreso = [
        {"titulo": "Diseñar UI", "estado": "Pendiente"},
        {"titulo": "Implementar Autenticación", "estado": "En Progreso"},
    ]
    tareas_completadas = [
        {"titulo": "Configurar Base de Datos", "estado": "Completada"},
        {"titulo": "Configurar CI/CD", "estado": "Pendiente"},
    ]

    todas_las_tareas = tareas_en_progreso + tareas_completadas
    contadores = contar_tareas_por_estado(todas_las_tareas)

    return rx.div(
        columna_kanban("En Progreso", tareas_en_progreso),
        columna_kanban("Tareas Completadas", tareas_completadas),
        rx.div(f"Pendientes: {contadores.get('Pendiente', 0)}"),
        rx.div(f"En Progreso: {contadores.get('En Progreso', 0)}"),
        rx.div(f"Completadas: {contadores.get('Completada', 0)}")
    )

app = rx.App()
app.add_page(tablero_kanban)
app.compile()
