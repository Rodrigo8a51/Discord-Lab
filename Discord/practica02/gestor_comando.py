import datetime

def analizar_comando(entrada_usuario):
    """
    Segunda fase del Agente: Procesamiento de comandos y logica dinamica.
    Aqui el alumno aprende a separar la 'accion' de los 'datos'.
    """
    mensaje = entrada_usuario.lower().strip()

    # Simulacion de comandos prefijados(como se usan en Discod: !ayuda, !ejemplo)
    if mensaje.startswith("!"):
        partes = mensaje.split(" ", 1)
        comando = partes[0]
        argumento = partes[1] if len(partes) > 1 else None

        # Logica dr Comandos
        if comando == "!definir":
            return buscar_en_diccionario(argumento)
        
        elif comando == "!validar":
            return validar_variable(argumento)
        
        elif comando == "!hora":
            ahora = datetime.datetime.now().strftime("%H:%M:%S")
            return f"La hora actual es: {ahora}"
        
        elif comando == "!ayuda":
            return (
                "Comandos disponibles:\n"
                "1. '!definir <termino>' - Busca conceptos de Python\n"
                "2. '!validar <nombre>' - Revisa si un nombre de variable es correcto\n"
                "3. '!hora' - Muestra la hora del sistema\n"
            )
        else:
            return f" El comando '{comando}' no existe. Usa '!ayuda'."
        
    return " Recuerda usar el prefijo '!' para darme órdenes, o pregunta algo directamente."

def buscar_en_diccionario(termino):
        if not termino:
             return "Debes escribir que termino quieres definir. Ej: !definir list"
        conocimientos = {
            "variable": "Un espacio en memoria para almacenar datos.",
            "lista": "Collecion mutable de elementos",
            "tupla": "Coleccion inmutable de elementos (no se puede cambiar).",
        }
        return conocimientos.get(termino, f"No encontre {termino}. en mi base de datos.")

def validar_variable(nombre):
    """
    Logica pedagogica: Enseña a los alumnos las reglas de nombrado en Python
    """
    if not nombre:
        return "Indica el nombre a validar. Ej !validar mi_variable"
    
    if nombre[0].isidentifier():
        return f"'{nombre}' no es valido: ¡No puede empezar con un numero!"
    if " " in nombre:
        return f"'{nombre}' no es valido: No puede contener espacios"
    if not nombre.isidentifier():
        return f"'{nombre}' contiene caracteres no permitidos (solo letras, numeros y guiones bajos)"
    
    return f"'{nombre}' es un nombre de variable valido en Python."

if __name__ == "__main__":
    print("---Agente de Logica: Fase de Comandos---")
    print("Prueba comandos como: !validar 123hola o !definir lista\n")
 
    while True:
        user_input = input("Alumno >> ")
        if user_input.lower() in ["salir", "exit"]: break
 
        respuesta = analizar_comando(user_input)
        print(f"Bot >> {respuesta}\n")