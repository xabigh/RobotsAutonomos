from irobot_edu_sdk.backend.bluetooth import Bluetooth
from irobot_edu_sdk.robots import event, Create3

# Inicializa el robot Create 3 por Bluetooth
robot = Create3(Bluetooth("C3_UIEC_Grupo2"))

# Evento que se dispara al iniciar (Play)
@event(robot.when_play)
async def play(robot):
    print('Conectado al robot')
    # Comando para que el robot avance 10 cm
    await robot.move(10)

# Inicia y mantiene activo el motor de eventos del robot
robot.play()