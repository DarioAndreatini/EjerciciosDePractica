#Simulacro Plantas

import random
import json
import os

pathPlantas = os.path.join(os.path.dirname(__file__),"plantas.txt")
pathProduccion = os.path.join(os.path.dirname(__file__),"produccion.txt")


def archivoPlantas():
    codigos_usados = set()
    
    with open(pathPlantas, "w") as archivo:
        while True:
            nombre = input("Ingrese el nombre de la planta (o FIN para terminar): ").strip()
            if nombre.upper() == "FIN":
                break

            try:
                codigo = int(input("Ingrese el código de la planta (1 a 150, no repetido): "))
            except ValueError:
                print("El código debe ser un número entero.")
                continue

            if codigo < 1 or codigo > 150:
                print("El código debe estar entre 1 y 150.")
                continue

            if codigo in codigos_usados:
                print("Ese código ya fue usado. Intente con otro.")
                continue

            archivo.write(f"{nombre};{codigo}\n")
            codigos_usados.add(codigo)

    print("Archivo plantas.txt generado correctamente.")


def archivoProducciones():
  
    with open(pathPlantas, "r") as archivo:
        plantas = [line.strip().split(";")[0] for line in archivo]

    tiposDeEnergia = ["Solar", "Eolica", "Hidroelectrica", "Geotermica", "Biomasa"]

    with open(pathProduccion, "w") as f:
        for i in range(1, 12001):
            planta = random.choice(plantas)
            tipo = random.choice(tiposDeEnergia)
            kw = random.randint(10, 500)
            f.write(f"{i};{planta};{tipo};{kw}\n")

    print("Archivo produccion.txt generado con 12.000 registros.")


def Procesamiento():
    
    resumen = {}
    totales_por_tipo = {"Solar":0,"Eolica":0,"Hidroelectrica":0,"Geotermica":0,"Biomasa":0}
    total_kw = 0
    total_registros = 0

    with open(pathProduccion, "r") as f:
        for linea in f:
            id_registro, planta, tipo, kw = linea.strip().split(";")
            kw = int(kw)

            totales_por_tipo[tipo] += kw

            if planta not in resumen:
                resumen[planta] = {
                    "Solar":0,
                    "Eolica":0,
                    "Hidroelectrica":0,
                    "Geotermica":0,
                    "Biomasa":0
                }
            resumen[planta][tipo] += kw

            total_kw += kw
            total_registros += 1

    mejor_planta = max(resumen.items(), key=lambda x: x[1]["Solar"] + x[1]["Eolica"])

    tipo_max = max(totales_por_tipo.items(), key=lambda x: x[1])

    promedio = total_kw / total_registros if total_registros > 0 else 0

    return resumen, totales_por_tipo, mejor_planta, tipo_max, promedio


def menu():
    print("Generar archivo de Plantas:")
    archivoPlantas()
    archivoProducciones()
    
    resumen, totales, mejor_planta, tipo_max, promedio = Procesamiento()
    
    print("--- Visualizacion de Opciones ---")
    print("1) Total de KW por Energia")
    print("2) Ver planta que mas energia genero Solar y Eolica")
    print("3) Mayor energia generada")
    print("4) Ver promedio ")
    print("5) Resumen General")
    print("6) Salir ")
    
    opcion = input("Ingrese opcion: ")
    
    while opcion != 6:
        if opcion == 1:
            
            print("\nTotal KW por tipo de energía:")
            for tipo, valor in totales.items():
                print(f"{tipo}: {valor}")
                
        if opcion == 2:
            print(f"\nPlanta con mayor Solar+Eolica: {mejor_planta[0]} ({mejor_planta[1]['Solar']+mejor_planta[1]['Eolica']} KW)")
    
        if opcion == 3:
            print(f"Tipo de energía con mayor producción: {tipo_max[0]} ({tipo_max[1]} KW)")

        if opcion == 4:
            print(f"Promedio global de KW por registro: {promedio: f}")

        if opcion == 5:
            print("\nDiccionario resumen:")
            print(json.dumps(resumen, indent=4))
            
        
            

if __name__ == "__main__":
    menu()