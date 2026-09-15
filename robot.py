from irobot_edu_sdk.backend.bluetooth import Bluetooth
from irobot_edu_sdk.robots import event, Create3
import asyncio

# Inicializa el robot Create 3 por Bluetooth
robot = Create3(Bluetooth("C3_UIEC_Grupo2"))

# Evento que se dispara al iniciar (Play)
@event(robot.when_play)
async def play(robot):
    print('Conectado al robot')
    
    # Fijar luz roja
    await robot.set_lights_on_rgb(255, 0, 0)
    
    # Ruido de Desconexión
    await robot.play_note(440, 1)
    
    # Comando para que el robot se desplace -20cm hacia atrás
    await robot.move(-20)

# Inicia y mantiene activo el motor de eventos del robot
robot.play()