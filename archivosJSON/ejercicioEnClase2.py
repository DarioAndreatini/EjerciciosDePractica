# Una pizzería guarda su menú en formato JSON. Querés leer el archivo pizzas.json y mostrar el nombre de cada pizza y su precio

import json
import os

try:
    archivoPizzas = os.path.join(os.path.dirname(__file__), "pizzas.json")
        
    with open(archivoPizzas, "r") as archivo:
        datosPizza = json.load(archivo)

    print("Menú de la pizzería:")
    for NombreYPrecio in datosPizza:
        print(f"- {NombreYPrecio['nombre']}: ${NombreYPrecio['precio']}")
    
except FileNotFoundError:
    print("No se encontro")
