# dumps

import json
import os

persona = {
    "Nombre": "Dario",
    "Edad": 24,
    "Lenguaje": ["Python", "Java"]
}

jsonString = json.dumps(persona, indent=4)

print(jsonString)

diccionarioPersona = json.loads(jsonString)

print(diccionarioPersona)