# 1
"""
Crea un programa que pida un número al usuario un número de mes (por ejemplo, el 4) y diga cuántos días tiene (por ejemplo, 30). 
Debes usar una matriz para su parametrización y una función para la recuperación del dato.
"""

# mes = int(input("Ingrese un número de mes (1-12): "))
dias_por_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def obtener_dias_mes(mes):
    if 1 <= mes <= 12:
        return dias_por_mes[mes - 1]
    else:
        return "Número de mes inválido. Por favor ingrese un número entre 1 y 12."
    
# dias = obtener_dias_mes(mes)
# print(f"El mes {mes} tiene {dias} días.")

# 2
"""
Crea una matriz con un tamaño que el usuario le indique por teclado (puede ser 6×4, 7×2, etc.) 
pero como máximo podrá contener 10x10 valores y como mínimo 2x2. 
Crear una función para la cargar de los valores y, por último, otro procedimiento para visualizar los resultados. 
Los valores para cargar deberán ser número positivos entre 0 y 100, siendo éstos generados al azar.
"""

import random

# n = int(input("Ingrese el número de filas (2-10): "))
# m = int(input("Ingrese el número de columnas (2-10): "))

def validar_dimensiones(n, m):
    if n < 2 or n > 10 or m < 2 or m > 10:
        print("Dimensiones inválidas. Por favor ingrese valores entre 2 y 10.")
        exit()

def crear_matriz(filas, columnas):
    matriz = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            valor = random.randint(0, 100)
            fila.append(valor)
        matriz.append(fila)
    return matriz

def mostrar_matriz(matriz):
    for fila in matriz:
        print(" ".join(f"{valor:3}" for valor in fila))

# validar_dimensiones(n, m)
# matriz = crear_matriz(n, m)
# mostrar_matriz(matriz)
# print(matriz)

# 3
"""
Suma de Matrices: escribir una función que reciba dos matrices como entrada y devuelva la matriz resultante de su suma. 
Se asume que ambas matrices tienen las mismas dimensiones.
"""

def sumar_matrices(matriz1, matriz2):
    
    filas = len(matriz1)
    columnas = len(matriz1[0])
    matriz_suma = []
    
    for i in range(filas):
        fila_suma = []
        for j in range(columnas):
            fila_suma.append(matriz1[i][j] + matriz2[i][j])
        matriz_suma.append(fila_suma)
    
    return matriz_suma

matriz1 = []
matriz2 = []

for i in range(3):
    fila1 = []
    fila2 = []
    for j in range(3):
        fila1.append(random.randint(0, 10))
        fila2.append(random.randint(0, 10))
    matriz1.append(fila1)
    matriz2.append(fila2)
    
# print("Matriz 1:")
# mostrar_matriz(matriz1) 
# print("\nMatriz 2:")
# mostrar_matriz(matriz2)
# matriz_suma = sumar_matrices(matriz1, matriz2)
# print("\nMatriz Suma:")
# mostrar_matriz(matriz_suma)

# 4
"""
Producto Escalar: crear una función que tome una matriz y un número como entrada, 
y devuelva la matriz resultante de multiplicar cada elemento por el número dado.
"""

def producto_escalar(matriz, escalar):
    filas = len(matriz)
    columnas = len(matriz[0])
    matriz_resultado = []
    
    for i in range(filas):
        fila_resultado = []
        for j in range(columnas):
            fila_resultado.append(matriz[i][j] * escalar)
        matriz_resultado.append(fila_resultado)
    
    return matriz_resultado

matriz = []
# escalar = int(input("Ingrese un número escalar: "))

for i in range(3):
    fila = []
    for j in range(3):
        fila.append(random.randint(0, 10))
    matriz.append(fila)
    
# print("Matriz Original:")
# mostrar_matriz(matriz)
# matriz_resultado = producto_escalar(matriz, escalar)
# print(f"\nMatriz Resultado (multiplicada por {escalar}):")
# mostrar_matriz(matriz_resultado)

# 5
"""
Suma de Filas y Columnas: crear una función que tome una matriz como entrada y
devuelva una lista con la suma de cada fila y otra lista con la suma de cada columna.
"""

def suma_filas_columnas(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    
    suma_filas = [0] * filas
    suma_columnas = [0] * columnas
    
    for i in range(filas):
        for j in range(columnas):
            suma_filas[i] += matriz[i][j]
            suma_columnas[j] += matriz[i][j]
    
    return suma_filas, suma_columnas

matriz = []
for i in range(3):
    fila = []
    for j in range(3):
        fila.append(random.randint(0, 10))
    matriz.append(fila)
    
# print("Matriz Ej 5:")
# mostrar_matriz(matriz)
# suma_filas, suma_columnas = suma_filas_columnas(matriz)
# print(f"\nSuma de Filas: {suma_filas}")
# print(f"Suma de Columnas: {suma_columnas}")

# 6
"""
Mayor Elemento por Columna: implementar una función que tome una matriz como entrada 
y devuelva una lista con los mayores elementos de cada columna.
"""

def mayor_elemento_por_columna(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    
    mayores_por_columnas = [matriz[0][j] for j in range(columnas)]
    
    for j in range(columnas):
        for i in range(filas):
            if matriz[i][j] > mayores_por_columnas[j]:
                mayores_por_columnas[j] = matriz[i][j]
    
    return mayores_por_columnas

matriz = []
for i in range(3):
    fila = []
    for j in range(3):
        fila.append(random.randint(0, 10))
    matriz.append(fila)
    
print("\nMatriz Ej 6:")
mostrar_matriz(matriz)
mayores_columnas = mayor_elemento_por_columna(matriz)
print("\nMayor Elemento por Columna son: ")
print(f"En la columna {matriz[0]}: {mayores_columnas[0]}")
print(f"En la columna {matriz[1]}: {mayores_columnas[1]}")
print(f"En la columna {matriz[2]}: {mayores_columnas[2]}")





