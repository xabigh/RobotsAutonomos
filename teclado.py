import keyboard
from irobot_edu_sdk.backend.bluetooth import Bluetooth
from irobot_edu_sdk.robots import event, Create3

# 1. Conexión al robot
robot = Create3(Bluetooth("C3_UIEC_Grupo2"))

# 2. Inicio del evento principal
@event(robot.when_play)
async def control_manual(robot):
    print("Control listo. Usa las flehcas del teclado.")
    
    # 3. Bucle infinito de lectura
    while True:
        
        # 4. Evaluación de las teclas
        if keyboard.is_pressed('up'):
            await robot.set_wheel_speeds(15, 15)
            
        elif keyboard.is_pressed('down'):
            await robot.set_wheel_speeds(-15, -15)
            
        elif keyboard.is_pressed('left'):
                await robot.set_wheel_speeds(-10, 10)
                
        elif keyboard.is_pressed('right'):
            await robot.set_wheel_speeds(10, -10)
            
        elif keyboard.is_pressed('q'):
            print("Cerrando conexión...")
            await robot.set_wheel_speeds(0, 0)
            break 
            
        else:
            await robot.set_wheel_speeds(0, 0)
            
        # 5. Control de flujo del procesador
        await robot.wait(0.1)

robot.play()