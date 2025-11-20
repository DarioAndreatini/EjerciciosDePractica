#Simulacro Plantas
# Simulacro Parcial
# La empresa EcoEnergía S.A. está desarrollando una plataforma llamada EnergiControl, que permitirá analizar la producción de plantas de energía renovable en distintas regiones.
#  
# Generación de archivos
#    -Crear el archivo plantas.txt con la estructura:
#          nombrePlanta;códigoPlanta
#     Solicitar al usuario la carga de plantas y sus códigos (entre 1 y 150, no repetidos).
#     Finalizar cuando ingrese FIN.
#  
# Crear el archivo produccion.txt con 12.000 registros automáticos:
#  
# id_registro;planta;tipo_energia;kw_generados
#  
# Donde:
#  
#     id_registro: incremental desde 1
#  
#     planta: una seleccionada al azar desde plantas.txt, el nombre de la planta.
#  
#     tipo_energia: solar, eolica, hidroeléctrica, geotérmica, biomasa
#  
#     kw_generados: número entero aleatorio entre 10 y 500
#  
# Procesamiento:
#  
#     Calcular el total de KW generados por cada tipo de energía y mostrarlo.
#  
#     Determinar la planta que generó mayor cantidad total de energía renovable solar y eólica combinadas.
#  
#     Crear un diccionario resumen como:
#  
#     {
#         "Planta Delta": {"Solar":5000,"Eolica":3000,"Hidroelectrica":2000,"Geotermica":500,"Biomasa":700},
#         "Planta Sur": ...
#     }
#  
#     Si no hay valores para algún tipo, colocar 0.
#  
# Indicadores finales:
#  
# - Tipo de energía con mayor producción total.
#  
# - Promedio global de kilowatts generados por registro.
#  
# - El programa debe incluir un menú de opciones para acceder a los distintos reportes.

import random
import json
import os

pathPlantas = os.path.join(os.path.dirname(__file__),"plantas.txt")
pathProduccion = os.path.join(os.path.dirname(__file__),"produccion.txt")


def archivoPlantas():
    codigos_usados = set()
    
    with open(pathPlantas, "w") as archivo:
        while True:
            nombre = input("Ingrese el nombre de la planta (o FIN para terminar): ").strip() # El strip elimina espacios en blanco al inicio y final
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
        # Esta linea crea una lista con los nombres de las plantas con line que lee el archivo, 
        # un strip para eliminar saltos de linea y split para separar por ; y quedarse con el nombre (posicion 0)

    tiposDeEnergia = ["Solar", "Eolica", "Hidroelectrica", "Geotermica", "Biomasa"]

    with open(pathProduccion, "w") as produccion:
        for i in range(1, 12001): # genera registros del 1 al 12000
            
            planta = random.choice(plantas) # selecciona una planta al azar de la lista plantas
            tipo = random.choice(tiposDeEnergia) # selecciona un tipo de energia al azar de la lista tiposDeEnergia
            kw = random.randint(10, 500) # genera un numero entero aleatorio entre 10 y 500
            
            produccion.write(f"{i};{planta};{tipo};{kw}\n") # escribe en el archivo el registro con los datos generados 

    print("Archivo produccion.txt generado con 12.000 registros.")


def procesamiento():
    
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
    
    print("\n--- Generación de Datos ---")
    archivoPlantas()
    archivoProducciones()

    while True:
        print("\n" + "="*40)
        print("    SISTEMA ENERGICONTROL - REPORTES  ")
        print("="*40)
      
        # Opciones de Reportes (Lo que pediste)
        print("1. Ver Totales por Tipo de Energía")
        print("2. Ver Planta con Mayor Producción (Solar + Eólica)")
        print("3. Ver Tipo de Energía Líder")
        print("4. Ver Promedio Global de Generación")
        print("5. Salir")
        
        opcion = input("\nSeleccione una opción: ")

        # Recargamos los datos después de generar archivos nuevos
        datos = procesamiento() 
        input("\nDatos generados. Presione Enter para volver al menú...")

        if opcion == "5":
            print("Saliendo del sistema. ¡Hasta luego!")
            break
            
        # Las opciones de reporte requieren que 'datos' exista
        elif opcion in ["1", "2", "3", "4"]:
            if not datos:
                print("\n¡ALERTA! No hay datos procesados.")
                print("Por favor, ejecute la opción 0 para generar los archivos primero.")
                input("Presione Enter para continuar...")
                continue
                
            resumen, totales_por_tipo, mejor_planta, tipo_max, promedio = datos
            
            if opcion == "1":
                print("\n--- Totales por Tipo de Energía ---")
                for tipo, total in sorted(totales_por_tipo.items(), key=lambda x: x[1], reverse=True):
                    print(f"{tipo:<15}: {total:>10,} kW")
                input("\nPresione Enter para volver...")

            elif opcion == "2":
                print("\n--- Planta con Mayor Producción (Solar + Eólica) ---")
                total_combinado = mejor_planta[1]['Solar'] + mejor_planta[1]['Eolica']
                print(f"Planta: {mejor_planta[0]}")
                print(f"Total Combinado: {total_combinado:,} kW")
                print(f"Detalle -> Solar: {mejor_planta[1]['Solar']:,} kW | Eólica: {mejor_planta[1]['Eolica']:,} kW")
                input("\nPresione Enter para volver...")

            elif opcion == "3":
                print("\n--- Tipo de Energía Líder ---")
                print(f"Tipo: {tipo_max[0]}")
                print(f"Total Generado: {tipo_max[1]:,} kW")
                input("\nPresione Enter para volver...")

            elif opcion == "4":
                print("\n--- Promedio Global ---")
                print(f"Promedio por registro: {promedio:.2f} kW")
                input("\nPresione Enter para volver...")
        
        else:
            print("Opción inválida. Por favor intente de nuevo.")
    
if __name__ == "__main__":
    menu()