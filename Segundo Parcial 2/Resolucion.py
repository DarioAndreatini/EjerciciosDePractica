import random
import json
import sys
import os

pathChoferes = os.path.join(os.path.dirname(__file__),"choferes.txt")
pathEnvios = os.path.join(os.path.dirname(__file__),"envios.txt")

def archivoChoferes():
    
    codigos_usados = set()
    
    bandera = True
    
    with open(pathChoferes, "w") as choferes:
    
        while bandera:
            nombre = input("Ingrese el Apellido y Nombre del Chofer (o FIN para terminar): ").strip() # El strip elimina espacios en blanco al inicio y final
            if nombre.upper() == "FIN":
                bandera = False
                break   
            try:
                legajo = int(input("Ingrese el legajo de la planta (1000 a 9999, no repetido): "))
            except ValueError:
                print("El código debe ser un número entero.")
                continue
            
            if legajo < 1000 or legajo > 9999:
                print("El código debe estar entre 1000 y 9999.")
                continue
            
            if legajo in codigos_usados:
                print("Ese código ya fue usado. Intente con otro.")
                continue
            
            choferes.write(f"{nombre};{legajo}\n")
            codigos_usados.add(legajo)
            
        print("Archivo choferes.txt generado correctamente.")
        
def archivoEnvios():
    
    with open(pathChoferes, "r") as choferes:
        chofer = [line.strip().split(";")[1] for line in choferes]
        
    datosZona = ["Norte", "Sur", "Este", "Oeste", "CABA"]
    
    with open(pathEnvios, "w") as envios:
        
        for envio in range(1, 21): # Limitado a 10 para manejo mas facil
            
            IdChofer = random.choice(chofer)
            zona = random.choice(datosZona)
            kilos = random.randint(50, 2000)
            
            envios.write(f"{envio};{IdChofer};{zona};{kilos}\n")
        
    print("Archivo envios.txt generado con 5.000 registros.")
    
def procesarEnvios ():
    resumenEnvios = {}
    totales_por_zona = {"Norte":0, "Sur":0, "Este":0, "Oeste":0, "CABA":0}
    total_kilos = []
    mejor_rendimiento = 0
    
    with open(pathEnvios, "r") as envios:
        for envio in envios:
            id_envio, id_chofer, zona, kilos = envio.strip().split(";")
            kilos = int(kilos)
            
            # 1. Llenar lista para recursividad
            total_kilos.append(kilos)
                
            # 2. Acumular por Zona Global
            if zona in totales_por_zona:
                totales_por_zona[zona] += kilos
            
            # 3. Diccionario Resumen por Chofer
            if id_chofer not in resumenEnvios:
                resumenEnvios[id_chofer] = {"Norte": 0, "Sur": 0, "Este": 0, "Oeste": 0, "CABA": 0}
            
            if zona in resumenEnvios[id_chofer]:
                resumenEnvios[id_chofer][zona] += kilos
            
        sys.setrecursionlimit(6000) # Aumentamos límite por las dudas
        total_general_recursivo = sumar_recursivamente(total_kilos)

        cant_envios = len(total_kilos)
        promedio = total_general_recursivo / cant_envios if cant_envios > 0 else 0
        
    return resumenEnvios, totales_por_zona, promedio, total_general_recursivo

def sumar_recursivamente(lista):
    
    if not lista:
        return 0
    else:
        return lista[0] + sumar_recursivamente(lista[1:])
    
            
def menu():
    
    print("\n--- Generación de Datos ---")
    archivoChoferes()
    archivoEnvios()
    
    datos = procesarEnvios()
    
    resumenEnvios, totales_por_zona, promedio, total_general_recursivo = datos
    
    print("\n--- REPORTES ---")
    print(f"1. Total Kilos (Calculado Recursivamente): {total_general_recursivo} kg")
    print(f"2. Promedio por Envío: {promedio:.2f} kg")
    
    zona_max = max(totales_por_zona.items(), key=lambda x: x[1])
    print(f"3. Zona con mayor movimiento: {zona_max[0]} ({zona_max[1]:,} kg)")
    
    print("4. Resumen de Choferes: ")
    for leg, zonas in resumenEnvios.items():
        print(f"Legajo {leg}: {zonas}")

if __name__ == "__main__":
    menu()