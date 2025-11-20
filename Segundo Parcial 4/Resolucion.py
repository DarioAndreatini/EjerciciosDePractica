import random
import json
import os

# Definición de rutas
pathEquipos = os.path.join(os.path.dirname(__file__), "equipos.txt")
pathResultados = os.path.join(os.path.dirname(__file__), "resultados.txt")
pathRanking = os.path.join(os.path.dirname(__file__), "ranking.json")

def cargar_equipos():
    codigos_usados = set()
    nombres_usados = set()
    regiones = ("SAM", "NA", "EU")
    
    bandera = True
    
    try:
        # 'w' sobrescribe el archivo cada vez que se ejecuta esta opción
        with open(pathEquipos, "w", encoding='utf-8') as equipos:
            print("--- REGISTRO DE EQUIPOS ---")
            print("Ingrese 'FIN' como nombre para terminar.")
        
            while bandera:
                nombreEquipo = input("Nombre del Equipo: ").strip()
                
                if nombreEquipo.upper() == "FIN":
                    if len(codigos_usados) < 2:
                        print("Error: Debe cargar al menos 2 equipos para jugar.")
                        continue
                    break
                
                if not nombreEquipo:
                    print("El nombre no puede estar vacío.")
                    continue
                    
                if nombreEquipo.upper() in nombres_usados:
                    print("Error: Nombre ya registrado.")
                    continue
                
                # Bucle para validar ID
                while True:
                    try:
                        id_str = input("ID Equipo (1 - 99): ")
                        idEquipo = int(id_str)

                        if not (1 <= idEquipo <= 99):
                            print("El ID debe estar entre 1 y 99.")
                            continue
                            
                        if idEquipo in codigos_usados:
                            print("El ID ya existe.")
                            continue
                        break # Sale del while del ID si todo está bien
                    except ValueError:
                        print("Error: Debe ser un número entero.")
                        
                # Bucle para validar Región
                while True:
                    region_input = input(f"Región {regiones}: ").upper()
                    if region_input in regiones:
                        break # Sale del while de región si es válida
                    print("Región inválida.")

                # Guardar en archivo y memoria
                equipos.write(f"{idEquipo};{nombreEquipo};{region_input}\n")
                codigos_usados.add(idEquipo)
                nombres_usados.add(nombreEquipo.upper())
                print(f"Equipo {nombreEquipo} registrado.")
            
        print("Archivo equipos.txt generado correctamente.")  
                
    except IOError as e:
        print(f"Error de archivo: {e}") 
    
def simular_partidos():
    if not os.path.exists(pathEquipos):
        print("Error: No existe el archivo de equipos. Ejecute la opción 1 primero.")
        return

    try:
        with open(pathEquipos, "r", encoding='utf-8') as equipos:
            # Lee solo líneas no vacías
            lista_equipos = [line.strip().split(";")[0] for line in equipos if line.strip()]
            
        if len(lista_equipos) < 2:
            print("Insuficientes equipos para simular.")
            return
            
        with open(pathResultados, "w") as resultados:
            for i in range(1, 11):
                idEquipo1, idEquipo2 = random.sample(lista_equipos, 2)
                
                Goles1 = random.randint(0, 5) 
                Goles2 = random.randint(0, 5)
                
                resultados.write(f"{i};{idEquipo1};{idEquipo2};{Goles1};{Goles2}\n")
        
        print("Simulación completada. Archivo resultados.txt generado.") 
    except IOError as e:
        print(f"Error al procesar archivos: {e}")
    
def procesar_torneo():
    
    if not os.path.exists(pathEquipos) or not os.path.exists(pathResultados):
        print("Faltan archivos de datos. Genere equipos y simule partidos primero.")
        return None, None

    info_equipos = {}

    with open(pathEquipos, "r", encoding='utf-8') as equipos:
        for linea in equipos:
            if not linea.strip(): continue
            idEquipo, nombre, region = linea.strip().split(";")
            idEquipo = int(idEquipo)
            info_equipos[idEquipo] = {'Nombre': nombre, 'Region': region}
    
    tabla = {}
    for idEquipo in info_equipos:
        tabla[idEquipo] = {'Pts': 0, 'PJ': 0, 'PG': 0, 'PE': 0, 'PP': 0, 'Diff': 0}
    

    with open(pathResultados, "r", encoding='utf-8') as resultados:
        for linea in resultados:
            if not linea.strip(): continue
            datos_resultado = linea.strip().split(";")
            
            # Estructura: ID_Partido; id1; id2; s1; s2
            partido = (int(datos_resultado[1]), int(datos_resultado[2]), int(datos_resultado[3]), int(datos_resultado[4]))
            
            id1, id2, s1, s2 = partido
            
            # Verificación de seguridad por si un equipo fue borrado pero está en resultados
            if id1 not in tabla or id2 not in tabla:
                continue

            tabla[id1]['PJ'] += 1
            tabla[id2]['PJ'] += 1
            tabla[id1]['Diff'] += (s1 - s2)
            tabla[id2]['Diff'] += (s2 - s1)
            
            if s1 > s2: 
                tabla[id1]['Pts'] += 3
                tabla[id1]['PG'] += 1
                tabla[id2]['PP'] += 1
            elif s2 > s1: 
                tabla[id2]['Pts'] += 3
                tabla[id2]['PG'] += 1
                tabla[id1]['PP'] += 1
            else: 
                tabla[id1]['Pts'] += 1
                tabla[id2]['Pts'] += 1
                tabla[id1]['PE'] += 1
                tabla[id2]['PE'] += 1
    
    print("Torneo procesado correctamente.")
    # CORRECCIÓN IMPORTANTE: Retornar los datos calculados
    return tabla, info_equipos

def exportar_json(tabla, info_equipos):
    if not tabla:
        print("No hay datos para exportar.")
        return

    lista_ranking = []
    
    for id_eq, stats in tabla.items():
        item = {
            "Posicion": 0, 
            "Equipo": info_equipos[id_eq]['Nombre'],
            "Region": info_equipos[id_eq]['Region'],
            "Estadisticas": stats
        }
        lista_ranking.append(item)

    # Ordenar por Puntos y luego por Diferencia de Gol
    lista_ranking.sort(key=lambda x: (x['Estadisticas']['Pts'], x['Estadisticas']['Diff']), reverse=True)
    
    for idx, item in enumerate(lista_ranking):
        item['Posicion'] = idx + 1
        
    with open(pathRanking, "w", ) as ranking:
        json.dump(lista_ranking, ranking, indent=4)
        
    print(f"Ranking exportado a '{pathRanking}' exitosamente.")

    print("\n--- TOP 3 ---")
    for i in range(min(3, len(lista_ranking))):
        eq = lista_ranking[i]
        print(f"{eq['Posicion']}. {eq['Equipo']} - Pts: {eq['Estadisticas']['Pts']} (Diff: {eq['Estadisticas']['Diff']})")
        
def informe_regional(tabla, info_equipos):
    regiones_validas = ("SAM", "NA", "EU") # Renombrado para evitar conflicto
    print("\n--- Informe Regional ---")
    
    if not tabla:
        print("No hay datos procesados.")
        return
        
    victorias_region = {r: 0 for r in regiones_validas}
    
    for id_eq, stats in tabla.items():
        region_equipo = info_equipos[id_eq]['Region']
        # Validamos que la región exista en nuestro contador para evitar crash
        if region_equipo in victorias_region:
            victorias_region[region_equipo] += stats['PG']
        
    mejor_region = max(victorias_region.items(), key=lambda x: x[1])
    
    print("Victorias totales por Región:")
    for reg, vics in victorias_region.items():
        print(f"- {reg}: {vics}")
        
    print(f"\nLa región dominante es {mejor_region[0]} con {mejor_region[1]} victorias acumuladas.")        


def menu():
    tabla_posiciones = None
    info_equipos = None
    
    while True:
        print("\n=== CYBERLEAGUE 2025 ===")
        print("1. [ADMIN] Generar Equipos")
        print("2. [ADMIN] Simular Partidos")
        print("3. Procesar Liga (Calcular Tabla)")
        print("4. Ver Tabla / Exportar JSON")
        print("5. Informe Regional")
        print("6. Salir")
        
        op = input("Opción: ")
        
        if op == "1":
            cargar_equipos()
        elif op == "2":
            simular_partidos()
        elif op == "3":
            # Capturamos el retorno de la función
            resultado = procesar_torneo()
            if resultado[0] is not None:
                tabla_posiciones, info_equipos = resultado
        elif op == "4":
            if tabla_posiciones:
                exportar_json(tabla_posiciones, info_equipos)
            else:
                print("⚠️ Primero debe procesar el torneo (Opción 3).")
        elif op == "5":
            if tabla_posiciones:
                informe_regional(tabla_posiciones, info_equipos)
            else:
                print("⚠️ Primero debe procesar el torneo (Opción 3).")
        elif op == "6":
            print("¡GG WP!") # Good Game, Well Played
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    menu()