# dump 

import json
import os

persona = {
    "Nombre": "Dario",
    "Edad": 24,
    "Lenguaje": ["Python", "Java"]
}

rutaArchivo = os.path.join(os.path.dirname(__file__), "persona.json")

try:
    with open(rutaArchivo, 'w') as archivo:
        json.dump(persona, archivo, indent=2)
        print("Se creo el archivo!")
except Exception as e:
    print(e)