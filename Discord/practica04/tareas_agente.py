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

def listar_tareas(lista_tareas):
    """
    Formatea la lista de tareas para su visualizacion
    """
    if not lista_tareas:
        return "No hay tareas"
    
    resultado = "Listado de tareas:\n"

    for i, tarea in enumerate(lista_tareas, start=1):
        resultado += f"{i}. {tarea}\n"
    return resultado

def eliminar_tarea(lista_tareas, indice):
    """
    Eliminar una tarea por su numero de indice
    """
    if not indice.isdigit():
        return "ERROR. El indice debe ser un numero."
    
    indice = int(indice) - 1
    
    if 0 <= indice < len(lista_tareas):
        tarea_eliminada = lista_tareas.pop(indice)
    else:
        return "ERROR. No existe la tarea"
    return f"Tarea eliminada: '{tarea_eliminada}'"

def main():
    tareas = []
    prefijo = "!"
    print("Bienvenido al gestor de tareas")
    activo = True
    while activo:
        entrada = input(">>>").strip()
        
        if not entrada.startswith(prefijo):
            print("ERROR. Comando no reconocido")
            continue
        
        #Procesamiento de la entrada
        cuerpo = entrada[len(prefijo):].split(maxsplit=1)
        comando = cuerpo[0].lower()
        argumento = cuerpo[1] if len(cuerpo) > 1 else ""

        if comando == "exit":
            print("Saliendo del gestor...")
            activa = False
        elif comando == "add":
            print(agregar_tarea(tareas, argumento))
            
        elif comando == "list":
            print(listar_tareas(tareas))
            
        elif comando == "del":
            print(eliminar_tarea(tareas, argumento))
            
        else:
            print(f" Error: Comando '!{comando}' no reconocido.")
        
        print("-" * 20)

if __name__ == "__main__":
    main()