from unitree_sdk2py.core.channel import ChannelFactoryInicializer
from unitree_sdk2py.go2.sport.sport_client import SportClient
import time
 
acciones = {
    "moverDelante": {
        "vx": 0.2,
        "vy": 0.0,
        "vyaw": 0.0
        },
    "moverIzquierda": {
        "vx": 0.0,
        "vy": 0.2,
        "vyaw": 0.0
        },
    "moverDerecha": {
        "vx": 0.0,
        "vy": -0.2,
        "vyaw": 0.0
        },
    "altura": {
        "bajar": -0.1,
        "subir": 0
        }
}
 
def move_robot(client:SportClient, params, duration):
    print("Iniciando movimiento...")
    start_time = time.time()
    while time.time() - start_time < duration:
        client.Move(vx=params["vx"], vy=params["vy"], vyaw=params["vyaw"])
        time.sleep(0.1)
    return print("Termino.")
        
def saludar_robot(client:SportClient, params, duration):
    print("Iniciando movimiento...")
    start_time = time.time()
    client.Hello()
    return print("Termino.")
    
if __name__ == "__main__":
    ChannelFactoryInicializer(0)
    client = SportClient()
    client.SetTimeout(0.5)
    client.Init()
    client.ClassicWalk(True)
    client.main()
 
    # Espera un momento para estabilizar
    time.sleep(1)
 
    duracion_segmento = 2
 
    # Ejecuta la secuencia de movimientos
     # Avanzar
    move_robot(client, acciones["moverDelante"], 7)
 
    # Mover hacia la derecha
    move_robot(client, acciones["moverDerecha"], 3)
 
    # Avanzar
    move_robot(client, acciones["moverDelante"], 3)
 
    # Mover hacia la izquierda
    move_robot(client, acciones["moverIzquierda"], 3)
 
    # Avanzar
    move_robot(client, acciones["moverDelante"], 4)
    
    saludar_robot(client)
 
    print("Secuencia completa.")
 
 