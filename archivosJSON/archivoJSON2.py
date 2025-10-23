# load

import json
import os

try:
    rutaArchivo = os.path.join(os.path.dirname(__file__), "persona.json")
    
    with open(rutaArchivo, 'r') as archivo:
        datosPersona = json.load(archivo)
    
except FileNotFoundError:
    print("No se encontro")
    

print("Datos: ")
print(f"Nombre: {datosPersona["Nombre"]}")
print(f"Edad: {datosPersona["Edad"]}")
print(f"Lenguaje: {datosPersona["Lenguaje"]}")



