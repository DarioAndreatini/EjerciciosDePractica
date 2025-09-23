
import random

numeros = [random.randint(1, 100) for _ in range(5)]

# 1
"""
1.	Crear funciones lambda que resuelvan las siguientes problemáticas:
a.	Calcule la superficie de un rectángulo
b.	Determine si una nota está aprobada o no (mayor o igual que 4 aprueba). Retorna True por aprobado; False por desaprobado.
c.	Que dado un número invierta su signo (de positivo a negativo y viceversa)
d.	Que dado un nombre determine si su longitud es larga (mayor de 10 caracteres). Retorna True o False.
e.	Dado un valor numérico retorne True si es positivo o cero; False en caso contrario.
f.	Escribe una función que tome dos argumentos: a y b y devuelva la multiplicación de ellos.
g.	Que compare dos valores y retorne True si el primer argumento es mayor que el segundo
"""

# a.

superficie_rectangulo = lambda largo, ancho: largo * ancho

# b.

nota_aprobada = lambda nota: nota >= 4

# c.

invertir_signo = lambda numero: -numero

# d.

longitud_larga = lambda nombre: len(nombre) > 10

# e.

es_positivo_o_cero = lambda valor: valor >= 0

# f.

multiplicar = lambda a, b: a * b

# g.

es_mayor = lambda a, b: a > b

# 2
"""
Escriba un programa para generar una función (utilizando filter) y lambdas para separar los números pares e impares de una lista de números. 
La función debe retornar dos valores resultantes.
"""

import random

def separar_pares_impares(numeros):
    pares = list(filter(lambda x: x % 2 == 0, numeros)) # Aplica la función lambda para filtrar los números pares
    impares = list(filter(lambda x: x % 2 != 0, numeros)) # Aplica la función lambda para filtrar los números impares
    return pares, impares


# print("Números generados:")
# numeros = [random.randint(1, 100) for _ in range(10)]
# print(numeros)
# pares, impares = separar_pares_impares(numeros)
# print("Números pares:", pares)
# print("Números impares:", impares)  

# 3
"""
Escriba un programa para contar los números pares e impares en una lista dada de enteros usando Lambda.
"""

def contar_pares_impares(numeros):
    contar_pares = len(list(filter(lambda x: x % 2 == 0, numeros))) # Aplica la función lambda para filtrar los números pares y genera una lista para contar su longitud
    contar_impares = len(list(filter(lambda x: x % 2 != 0, numeros))) # Aplica la función lambda para filtrar los números impares y genera una lista para contar su longitud
    return contar_pares, contar_impares


# print("Números generados:")
# print(numero)
# print ("Números pares:", contar_pares_impares(numero)[0])
# print ("Números impares:", contar_pares_impares(numero)[1])

# 4
"""
Escriba un programa Python para encontrar números divisibles por 3 de una lista de números usando Lambda.
"""

def encontrar_divisibles_por_3(numeros):
    divisibles_por_3 = list(filter(lambda x: x % 3 == 0, numeros)) # Aplica la función lambda para filtrar los números divisibles por 3
    return divisibles_por_3

# print("Números generados:")
# print(numeros) 
# print("Números divisibles por 3:", encontrar_divisibles_por_3(numeros))

# 5
"""
Utilizando map, crear un programa que cargue 10 notas de alumnos y, al finalizar, 
genere una nueva lista indicando el estado de aprobación (reutilice lo creado en el punto 1).
"""

def estado_aprobacion(notas):
    estados = list(map(lambda nota: "Aprobado" if nota_aprobada(nota) else "Desaprobado", notas)) # Aplica por cada nota la función lambda que utiliza la función nota_aprobada
    return estados

# notas = [random.randint(1, 10) for _ in range(10)]
# print("Notas generadas:")
# print(notas)
# print("Estado de aprobación:", estado_aprobacion(notas))

# 6
"""
Modifique la función anterior, haciendo uso de filter, para poder obtener una lista de notas aprobadas y otro de desaprobadas.
"""

def separar_notas_aprobadas_desaprobadas(notas):
    aprobadas = list(filter(lambda nota: nota_aprobada(nota), notas)) # Aplica la función lambda que utiliza la función nota_aprobada para filtrar las notas aprobadas
    desaprobadas = list(filter(lambda nota: not nota_aprobada(nota), notas)) # Aplica la función lambda que utiliza la función nota_aprobada para filtrar las notas desaprobadas
    return aprobadas, desaprobadas

# notas = [random.randint(1, 10) for _ in range(10)]
# print("Notas generadas:")             
# print(notas)
# aprobadas, desaprobadas = separar_notas_aprobadas_desaprobadas(notas)
# print("Notas aprobadas:", aprobadas)
# print("Notas desaprobadas:", desaprobadas)

# 7
"""
Escriba un programa que utilizando map y una función lambda como argumento, permita generar una nueva lista con el resultado de la división
en 1 (es decir, 1/x) de cada elemento de la lista.
"""

def dividir_en_uno(numeros):
    resultados = list(map(lambda x: 1 / x if x != 0 else None, numeros)) # Aplica la función lambda para dividir 1 por cada número, manejando el caso de división por cero
    return resultados

# print("Números generados:")
# print(numeros)
# print("Resultados de la división en 1:", dividir_en_uno(numeros))

# 8
"""
Crea una función doble que acepte una lista de números como argumento y
devuelva una nueva lista con cada número multiplicado por dos. Utiliza la
función map para implementarla.
"""

def multiplicar_por_dos(numeros):
    resultados = list(map(lambda x: x * 2, numeros)) # Aplica la función lambda para multiplicar cada número por 2
    return resultados

# print("Números generados:")
# print(numeros)      
# print("Números multiplicados por dos:", multiplicar_por_dos(numeros))

# 9
"""
Crea una función filtraMayores que acepte una lista de números como argumento y devuelva una nueva lista con los números mayores que 5.
Utiliza la función filter para implementarla.
"""

def filtraMayores(numeros):
    mayores_que_cinco = list(filter(lambda x: x > 5, numeros)) # Aplica la función lambda para filtrar los números mayores que 5
    return mayores_que_cinco

# print("Números generados:")
# print(numeros)        
# print("Números mayores que 5:", filtraMayores(numeros))

# 10
"""
Crea una función dobleSiEsPar que acepte una lista de números como argumento, devuelva una nueva lista con cada número multiplicado por dos
si es par, y elimine todos los números impares de la lista. Utiliza funciones lambda, map y filter para implementarla.
"""

def dobleSiEsPar(numeros):
    pares = list(filter(lambda x: x % 2 == 0, numeros)) # Filtra los números pares
    resultados = list(map(lambda x: x * 2, pares)) # Multiplica por 2 los números pares
    return resultados

# print("Números generados:")
# print(numeros)
# print("Números pares multiplicados por dos:", dobleSiEsPar(numeros))

# 11
"""
Crea una función esDivisible que acepte un número como argumento, y una
lista de números, y devuelva una nueva lista con los números de la lista que son divisibles por el número dado. 
Utiliza funciones lambda y filter para implementarla.
"""

def esDivisible(divisor, numeros):
    divisibles = list(filter(lambda x: x % divisor == 0, numeros)) # Filtra los números divisibles por el divisor dado
    return divisibles

# divisor = int(input("Ingrese un número divisor: "))
# print("Números generados:")
# print(numeros)
# print(f"Números divisibles por {divisor}:", esDivisible(divisor, numeros))

# 12
"""
Crea una función ordenaPalabras que acepte una lista de palabras como
argumento, y devuelva una nueva lista con las palabras ordenadas alfabéticamente en orden inverso. 
Utiliza funciones lambda, map y sorted para implementarla.
"""

def ordenaPalabras(palabras):
    palabras_ordenadas = sorted(palabras, key=lambda x: x.lower(), reverse=True) # Ordena las palabras alfabéticamente en orden inverso, ignorando mayúsculas/minúsculas
    return palabras_ordenadas

# palabras = ["manzana", "Banana", "cereza", "durazno", "Albaricoque"]
# print("Palabras generadas:")
# print(palabras)
# print("Palabras ordenadas alfabéticamente en orden inverso:", ordenaPalabras(palabras))

# 13
"""
Crea una función productoPares que acepte una lista de números como
argumento y devuelva el producto de todos los números pares de la lista.
Utiliza la función reduce y una función lambda para implementarla.
"""

from functools import reduce

def productoPares(numeros):
    pares = list(filter(lambda x: x % 2 == 0, numeros)) # Filtra los números pares
    producto = reduce(lambda x, y: x * y, pares, 2) # Calcula el producto de los números pares, con un valor inicial de 1
    return producto

# print("Números generados:")
# print(numeros)
# print("Producto de los números pares:", productoPares(numeros))

# 14
"""
Crea una función masCorto que acepte una lista de strings como argumento
y devuelva el string más corto de la lista. Utiliza la función reduce y una
función lambda para implementarla.
"""

def masCorto(strings):
    string_mas_corto = reduce(lambda x, y: x if len(x) < len(y) else y, strings) # Encuentra el string más corto utilizando reduce
    return string_mas_corto

# strings = ["manzana", "Banana", "uva2222", "cereza", "durazno", "Albaricoque", "kiwi", "figo"]
# print("Strings generados:")
# print(strings)
# print("String más corto:", masCorto(strings))


    






