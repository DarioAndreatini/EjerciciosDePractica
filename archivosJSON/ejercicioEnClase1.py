# Tenés un archivo animales.json con animales y su edad. Mostrá solo los animales mayores de 10 años.

import json
import os

try:
    archivoAnimales = os.path.join(os.path.dirname(__file__), "animales.json")
        
    with open(archivoAnimales, "r") as archivo:
        datosAnimales = json.load(archivo)

    mayores = [animal for animal in datosAnimales if animal["edad"] > 10]

    print("Animales mayores de 10 años:")
    for animal in mayores:
        print(f"{animal['tipo']} - {animal['edad']}")    
    
except FileNotFoundError:
    print("No se encontro")


