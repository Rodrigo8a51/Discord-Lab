import discord
import os
import re
from dotenv import load_dotenv
import datetime
from practica02.gestor_comando import buscar_en_diccionario, validar_variable
from practica03.agente_logica import ejecutar_multiplicacion, ejecutar_suma, buscar_en_diccionario, obtener_fecha_completa
from practica01.procesador_comandos import obtener_saludo, procesar_comando_recordar, calcular_uptime

def mostrar_bienvenida():
    """Retorna la lista de comandos disponibles."""
    return (
        "📜 Bot de Gestión de Tareas (Modo Estructurado):\n"
        "📜 Primeros pasos Agente Discord UX:\n"
        "📜 Escriba !inicio para ver la lista de comandos:\n"
        "📜 Escriba !hora para ver la hora actual:\n"
        "📜 Escriba !buscar <termino> para buscar en el diccionario:\n"
        "📜 Escriba !validar <nombre> para validar un nombre de variable:\n"
        "📜 Escriba !suma <num1> <num2> para sumar dos números:\n"
        "📜 Escriba !multiplicacion <num1> <num2> para multiplicar dos números:\n"
        "📜 Escriba !ayuda para ver la lista de comandos:\n"
        "📜 Escriba !fecha para ver la fecha actual:\n"
        "📜 Escriba !saludo para recibir un saludo:\n"
        "📜 Escriba !recordar <tarea> para agregar una tarea:\n"
        "📜 Escriba !uptime para ver el tiempo de actividad:\n"
        "📜 Escriba !Exit para salir del Agente:"

    )



def main(entrada):
    
        PREFIJO = "!"
        
        if not entrada.startswith(PREFIJO):
            if entrada: print("Recuerda usar '!' para comandos.")
            
        # Procesamiento de la entrada
        cuerpo = entrada[len(PREFIJO):].split(maxsplit=1)
        comando = cuerpo[0].lower()
        argumento = cuerpo[1] if len(cuerpo) > 1 else ""
        
        # Selección de acción (Estructura de control)
        if comando == "exit":
            print("Saliendo del gestor...")
            return "Saliendo del gestor..."
        
        elif comando == "inicio":
            print(mostrar_bienvenida())
            return mostrar_bienvenida()
        
        elif comando == "hora":
            ahora = datetime.datetime.now().strftime("%H:%M:%S")
            return f" Hora actual: {ahora}"

        elif comando == "buscar":
            return buscar_en_diccionario(argumento)
        
        elif comando == "validar":
            return validar_variable(argumento) 
        
        elif comando == "suma":
            return ejecutar_suma(argumento)
        
        elif comando == "multiplicacion":
            return ejecutar_multiplicacion(argumento)
        
        elif comando == "fecha":
            return obtener_fecha_completa()
        
        elif comando == "saludo":
            return obtener_saludo("Agente Discord UX")
        
        elif comando == "recordar":
            return procesar_comando_recordar(argumento)
        
        elif comando == "uptime":
            hora_inicio = datetime.datetime.now()  # Para demo, se reinicia cada vez
            return calcular_uptime(hora_inicio)

        elif comando == "ayuda":
            return (
                "Comandos disponibles:\n"
                "1. '!definir <termino>' - Busca conceptos de Python\n"
                "2. '!validar <nombre>' - Revisa si un nombre de variable es correcto\n"
                "3. '!hora' - Muestra la hora del sistema\n"
                "4. '!inicio' - Muestra esta lista de comandos\n"
                "5. '!suma <num1> <num2>' - Realiza una suma\n"
                "6. '!multiplicacion <num1> <num2>' - Realiza una multiplicación\n"
                "7. '!fecha' - Muestra la fecha actual\n"
                "8. '!saludo' - Recibe un saludo\n"
                "9. '!recordar <tarea>' - Agrega una tarea a la lista de recordatorios\n"
                "10. '!uptime' - Muestra el tiempo de actividad del bot\n"
            )
        
        else:
            print(f" Error: Comando '!{comando}' no reconocido.")
            return f" Error: Comando '!{comando}' no reconocido."
        
        print("-" * 20)


# --- CONFIGURACIÓN DE DISCORD ---

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Definir los "intents" (permisos) necesarios
intents = discord.Intents.default()
intents.message_content = True  # Necesario para leer el contenido de los mensajes

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Sincronizado como {client.user} (ID: {client.user.id})')
    print('------')

@client.event
async def on_message(message):
    # Evitar que el bot se responda a sí mismo
    if message.author == client.user:
        return
    
    # 3. Procesamiento: Pasamos el contenido del mensaje a nuestra lógica
    print(f"Mensaje recibido de {message.author}: {message.content}")

      # Solo procesamos si el mensaje empieza con un prefijo (opcional, pero recomendado)
    if message.content.startswith('!'):
        resultado = main(message.content)

        print(f"Resultado del procesamiento: {resultado}")
        
        # 4. Respuesta: El bot escribe el resultado en el mismo canal
        await message.channel.send(f" **Bot Procesador:** {resultado}")
    
# Ejecutar el bot
if __name__ == "__main__":
    if TOKEN:
        client.run(TOKEN)
    else:
        print("ERROR: No se encontró el TOKEN en el archivo .env")