import datetime

def obtener_saludo(nombre_bot):

    """
        Retorna un saludo formateado
    """
    return f"Hola, soy {nombre_bot} y estoy listo para ayudarte"

def procesar_comando_recordar(comando):

    """
        Valida y procesa la accion de recordar un dato
    """
    if not comando:
        return "Error: Falta el nombre. Uso recordar [nombre]"
    
    return f"¡Entendido! Recordaré el nombre: {comando}"

def calcular_uptime(hora_inicio):

    """
        Calcula la diferencia de tiempo entre el inicio y el actual (mostrar actividad del boot)
    """
    ahora = datetime.datetime.now()
    diferencia = ahora - hora_inicio
    segundos = int(diferencia.total_seconds())
    return f"Tiempo de actividad: {segundos} segundos"

def mostrar_ayuda():
    """"
    Comandos disponibles para el usuario
    """
    return (
        "Comandos disponibles:\n"
        "!saludo - Muestra un saludo del bot\n"
        "!recordar [nombre] - El bot recordará el nombre proporcionado\n"
        "!uptime - Muestra el tiempo de actividad del bot\n"
        "!ayuda - Muestra esta lista de comandos"
    )
# Funcion principal para probar las funciones 

def iniciar_agente():
    Nombre_bot = "AlexaBot"
    prefijo = "!"
    hora_inicio = datetime.datetime.now()

    print(f"{obtener_saludo(Nombre_bot)}")
    print("Escribe !ayuda para ver los comandos disponibles.")

    ejecutando = True
    while ejecutando:
        entrada = input(f"[{Nombre_bot}] Ingrese comando: ").strip()

        if not entrada.startswith(prefijo):
            print("Comando no reconocido")
            continue
        partes = entrada[len(prefijo):].split(maxsplit=1)
        comando = partes[0].lower()
        argumento = partes[1] if len(partes) > 1 else ""

        if comando == "saludo":
            print(obtener_saludo(Nombre_bot))
        elif comando == "ayuda":
            print(mostrar_ayuda())
        elif comando == "salir":
            print("Hasta luego")
            ejecutando = False
        else:
            print("Comando no reconocido")


def main():
    iniciar_agente()

if __name__ == "__main__":
    main()