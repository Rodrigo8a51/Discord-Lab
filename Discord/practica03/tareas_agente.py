import datetime

def agregar_tarea(lista_tareas, descripcion):
    """
    Agrega una tarea a la lista si cumple los requisitos
    """
    if len(descripcion) < 3:
        return "ERROR. La descripción debe tener al menos 3 caracteres."
    
    # CREAR FORMATO DE TAREA
    fecha = datetime.datetime.now().strftime("%H:%M")
    nueva_tarea = f"{descripcion} - {fecha}"
    lista_tareas.append(nueva_tarea)
    return f"Tarea '{descripcion}' agregada con exito."
