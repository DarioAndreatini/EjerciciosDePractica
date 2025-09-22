# 1
"""
Escribir una función para ingresar desde el teclado una serie de números entre A y B y guardarlos en una lista. 
En caso de ingresar un valor fuera de rango la función mostrará un mensaje de error y solicitará un nuevo número. 
Para finalizar la carga se deberá ingresar -1. 
La función recibe como parámetros los valores de A y B, y devuelve la lista cargada (o vacía, si el usuario no ingresó nada) como valor de retorno. 
Tener en cuenta que A puede ser mayor, menor o igual a B.
"""

def cargar_lista(A, B):
    lista = []
    minimo = min(A, B)
    maximo = max(A, B)

    n = int(input(f"Ingrese un número entre {minimo} y {maximo} (-1 para terminar): "))
    while n != -1:
        if minimo <= n <= maximo:
            lista.append(n)
        else:
            print("Error: número fuera de rango.")
        n = int(input(f"Ingrese un número entre {minimo} y {maximo} (-1 para terminar): "))
    return lista


# A = int(input("Ingrese el valor de A: "))
# B = int(input("Ingrese el valor de B: "))

# numeros = cargar_lista(A, B)
# print("Lista cargada:", numeros)

# 2
"""
Calcular la suma de los números de la lista
"""

def suma_lista(numeros):
    return sum(numeros)

# print("Suma de los números en la lista:", suma_lista(numeros))

# 3
"""
Determinar si la lista es capicúa (palíndromo). Una lista capicúa se lee de igual
modo de izquierda a derecha y de derecha a izquierda. Por ejemplo, [2, 7, 7, 2]
es capicúa, mientras que [2, 7, 5, 2] no lo es.
"""

def es_capicua(numeros):
    return numeros == numeros[::-1] # Comparando la lista con su reverso.

# print("La lista es capicúa." if es_capicua(numeros) else "La lista no es capicúa.")

# 4
"""
Escribir una función para contar cuántas veces aparece un valor dentro de la lista. 
La función recibe como parámetros la lista y el valor a buscar, y devuelve un número entero.
"""

def contar_ocurrencias(numeros, valor):
    return numeros.count(valor) # Usando el método count de listas de Python para contar ocurrencias.

# valor_a_buscar = int(input("Ingrese el valor a buscar en la lista: "))
# print(f"El valor {valor_a_buscar} aparece {contar_ocurrencias(numeros, valor_a_buscar)} veces en la lista.")

# 5
"""
Desarrollar una función que reciba la lista como parámetro y devuelva una nueva lista con los mismos elementos de la primera, pero en orden inverso. 
Por ejemplo, si la función recibe [5, 7, 1] debe devolver [1, 7, 5].
"""

def invertir_lista(numeros):
    return numeros[::-1] # Usando slicing para invertir la lista.

# print(f"Lista origirnal: {numeros} Lista invertida:", invertir_lista(numeros))

# 6
"""
Escribir una función para devolver una lista con todas las posiciones que ocupa un valor pasado como parámetro, 
utilizando búsqueda secuencial en una lista desordenada. 
La función debe devolver una lista vacía si el elemento no se encuentra en la lista original.
"""

def posiciones_valor(numeros, valor):
    posiciones = []
    for indice, numero in enumerate(numeros):
        if numero == valor:
            posiciones.append(indice)
    return posiciones

# valor_a_buscar = int(input("Ingrese el valor a buscar en la lista: "))
# print(f"El valor {valor_a_buscar} se encuentra en las posiciones: {posiciones_valor(numeros, valor_a_buscar)}")

# 7
"""
Ídem anterior, utilizando búsqueda binaria sobre una lista ordenada.
"""

def posiciones_valor_binaria(numeros, valor):  
    posiciones = []
    izquierda, derecha = 0, len(numeros) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if numeros[medio] == valor:
            # Encontrado el valor, buscar todas las ocurrencias
            # Buscar hacia la izquierda
            i = medio
            while i >= 0 and numeros[i] == valor:
                posiciones.append(i)
                i -= 1
            # Buscar hacia la derecha
            i = medio + 1
            while i < len(numeros) and numeros[i] == valor:
                posiciones.append(i)
                i += 1
            break
        elif numeros[medio] < valor:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return sorted(posiciones) # Devolver las posiciones ordenadas.

# valor_a_buscar = int(input("Ingrese el valor a buscar en la lista ordenada: "))
# numeros_ordenados = sorted(numeros)
# print(f"Lista ordenada: {numeros_ordenados}")
# print(f"El valor {valor_a_buscar} se encuentra en las posiciones: {posiciones_valor_binaria(numeros_ordenados, valor_a_buscar)}")

# 8
"""
Rellenar una lista con números enteros entre 0 y 100 obtenidos al azar e imprimir el valor mínimo y el lugar que ocupa. 
Tener en cuenta que el mínimo puede estar repetido, en cuyo caso deberán mostrarse todas las posiciones en las que se encuentre. 
La carga de datos termina cuando se obtenga un 0 como número al azar, el que no deberá cargarse en la lista.
"""

import random

def generar_lista():
    lista = []
    n = random.randint(0, 100)

    while n != 0:
        lista.append(n)
        n = random.randint(0, 100)

    return lista

def posiciones_minimo(lista):
    if not lista:  # lista vacía
        return None, []
    minimo = min(lista)
    posiciones = [i for i, valor in enumerate(lista) if valor == minimo]
    return minimo, posiciones


# Programa principal
# lista = generar_lista()
# print("Lista generada:", lista)
# 
# minimo, posiciones = posiciones_minimo(lista)
# if minimo is not None:
#     print(f"El valor mínimo es {minimo} y aparece en las posiciones {posiciones}")
# else:
#     print("La lista está vacía (salió 0 en el primer intento).")

# 9
"""
Crear una lista de N números generados al azar entre 0 y 100 pero sin elementos repetidos. 
El valor de N se ingresa por teclado. Resolver este problema utilizando dos estrategias distintas:
· Impidiendo el agregado de elementos repetidos
· Eliminando los duplicados luego de generar la lista. Asegurarse que la cantidad final de elementos sea la solicitada.
"""

def generar_lista_sin_repetidos(N):
    if N > 101:
        raise ValueError("N no puede ser mayor que 101, ya que los números son entre 0 y 100.")
    
    lista = []
    while len(lista) < N:
        n = random.randint(0, 100)
        if n not in lista:
            lista.append(n)
    return lista

def generar_lista_y_eliminar_duplicados(N):
    if N > 101:
        raise ValueError("N no puede ser mayor que 101, ya que los números son entre 0 y 100.")
    
    lista = [random.randint(0, 100) for _ in range(N * 2)]  
    lista_sin_duplicados = list(set(lista))  # Eliminar duplicados usando un set
    while len(lista_sin_duplicados) < N:  
        n = random.randint(0, 100)
        if n not in lista_sin_duplicados:
            lista_sin_duplicados.append(n)
    return lista_sin_duplicados[:N] 

# N = int(input("Ingrese la cantidad de números a generar (N): "))
# lista1 = generar_lista_sin_repetidos(N)       
# print("Lista sin repetidos (método 1):", lista1)
# lista2 = generar_lista_y_eliminar_duplicados(N)
# print("Lista sin repetidos (método 2):", lista2)

# 10 
"""
Eliminar de una lista de números enteros los valores que se encuentren en una segunda lista. 
Imprimir la lista original, la lista de valores a eliminar y la lista resultante. 
Ambas listas deben rellenarse con números al azar. La cantidad y el rango de los valores los decide el programador. 
"""

def eliminar_valores(lista_original, lista_a_eliminar):
    return [valor for valor in lista_original if valor not in lista_a_eliminar]

# n = int(input("Ingrese la cantidad de números en la lista original: "))
# m = int(input("Ingrese la cantidad de números en la lista a eliminar: "))
# cantidad_maxima = int(input("Ingrese el valor máximo para los números aleatorios (mínimo 20): "))

# Generar listas de ejemplo
# lista_original = [random.randint(0, cantidad_maxima) for _ in range(n)]
# lista_a_eliminar = [random.randint(0, cantidad_maxima) for _ in range(m)]
# lista_resultante = eliminar_valores(lista_original, lista_a_eliminar)
# print("Lista original:", lista_original)
# print("Lista de valores a eliminar:", lista_a_eliminar)
# print("Lista resultante:", lista_resultante)

# 11
"""
Cargar dos listas de números A y B con N números al azar entre 1 y 100, donde N se ingresa por teclado. 
Mostrar ambas listas por pantalla. Luego construir e imprimir tres nuevas listas C, D y E que contengan:
· La concatenación de los valores pares de A con los impares de B. (valores pares o valores impares se refiere a los elementos propiamente dichos y no a sus posiciones).
· La concatenación de los valores impares de A con el reverso de los valores pares de B.
· La intercalación de los elementos de A y B.
"""

A = []
B = []
# N = int(input("Ingrese la cantidad de números a generar en cada lista (N): "))

def generar_lista_azar(N):
    return [random.randint(1, 100) for _ in range(N)]

#A = generar_lista_azar(N)
#B = generar_lista_azar(N)
#print("Lista A:", A)
#print("Lista B:", B)

# Lista C: pares de A + impares de B
C = [x for x in A if x % 2 == 0] + [x for x in B if x % 2 != 0]
# print("Lista C (pares de A + impares de B):", C)    

# Lista D: impares de A + reverso de pares de B
D = [x for x in A if x % 2 != 0] + [x for x in B if x % 2 == 0][::-1]
# print("Lista D (impares de A + reverso de pares de B):", D)

# Lista E: intercalación de A y B
E = []
for a, b in zip(A, B):    # se usa para iterar hasta la longitud de la lista más corta
    E.append(a)
    E.append(b)
# print("Lista E (intercalación de A y B):", E)

# 12
"""
Dada una lista ordenada de números llamada A y un nuevo número N, desarrollar un programa que agregue el elemento N dentro de la lista A, 
respetando el ordenamiento existente. 
El programa deberá detectar automáticamente si el ordenamiento es ascendente o descendente antes de realizar la inserción. No se
permite añadir el elemento al final y reordenar la lista. 
"""

A = [] 

def cargar_lista(A):
    n = int(input("Ingrese un número para agregar a la lista ordenada (-1 para terminar): "))
    while n != -1:
        A.append(n)
        n = int(input("Ingrese un número para agregar a la lista ordenada (-1 para terminar): "))
    return A
    

# N = int(input("Ingrese el número a insertar en la lista ordenada: "))

def insertar_en_lista_ordenada(A, N):
    if not A:  # Si la lista está vacía, simplemente agregar N
        A.append(N)
        return A

    ascendente = A[0] < A[-1]  # Determinar si la lista está en orden ascendente o descendente

    for i in range(len(A)):
        if (ascendente and N < A[i]) or (not ascendente and N > A[i]):
            A.insert(i, N)
            return A

    A.append(N)  # Si N es mayor (o menor en caso descendente) que todos los elementos, agregar al final
    return A

# lista = cargar_lista(A)
# print("Lista original:", lista)
# A = insertar_en_lista_ordenada(lista, N)
# print("Lista después de insertar el número:", A)

# 13
"""
Leer dos listas de números M y N y ordenarlas de menor a mayor. 
Luego se solicita generar e imprimir una tercera lista que resulte de intercalar los elementos de M y N. 
La nueva lista también debe quedar ordenada, sin utilizar ningún método de ordenamiento en ella.
"""

M = []
N = []

def ordernar_lista(lista):
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] > lista[j]:
                lista[i], lista[j] = lista[j], lista[i]
    return lista

def intercalar_listas(M, N):
    P = []
    i = j = 0
    while i < len(M) and j < len(N):
        if M[i] < N[j]:
            P.append(M[i])
            i += 1
        else:
            P.append(N[j])
            j += 1
    while i < len(M):
        P.append(M[i])
        i += 1
    while j < len(N):
        P.append(N[j])
        j += 1
    return P

# M = [random.randint(0, 100) for _ in range(5)]
# N = [random.randint(0, 100) for _ in range(5)]        
# print("Lista M :", M)
# print("Lista N :", N)
# 
# print("Lista M ordenada:", ordernar_lista(M))
# print("Lista N ordenada:", ordernar_lista(N))   
# 
# P = intercalar_listas(M, N)
# print("Lista P (intercalada y ordenada):", P)

# 14
"""
Una escuela necesita conocer cuántos alumnos cumplen años en cada mes del año, con el propósito de ofrecerles un agasajo especial en su día. 
Desarrollar un programa que lea el número de legajo y fecha de nacimiento (día, mes y año) de cada uno de los alumnos que concurren a dicha escuela.}
La carga finaliza con un número de legajo igual a -1. 
Emitir un informe donde aparezca -mes por mescuántos alumnos cumplen años a lo largo del año. 
Imprimir también una leyenda que indique cuál es el mes con mayor cantidad de cumpleaños.
"""

lista_alumnos = []

def cargar_alumnos():
    legajo = int(input("Ingrese el número de legajo del alumno (-1 para terminar): "))
    while legajo != -1:
        dia = int(input("Ingrese el día de nacimiento: "))
        mes = int(input("Ingrese el mes de nacimiento (1-12): "))
        anio = int(input("Ingrese el año de nacimiento: "))
        lista_alumnos.append((legajo, dia, mes, anio))
        legajo = int(input("Ingrese el número de legajo del alumno (-1 para terminar): "))
    return lista_alumnos

def contar_cumpleanos_por_mes(alumnos):
    meses = [0] * 12  # Lista para contar cumpleaños por mes
    for alumno in alumnos:
        mes = alumno[2]
        if 1 <= mes <= 12:
            meses[mes - 1] += 1
    return meses

def mes_con_mas_cumpleanos(meses):
    max_cumpleanos = max(meses)
    mes = meses.index(max_cumpleanos) + 1  # +1 para ajustar al número de mes (1-12)
    return mes, max_cumpleanos

# Programa principal
cargar_alumnos()
meses = contar_cumpleanos_por_mes(lista_alumnos)
print("Cantidad de cumpleaños por mes:", meses)
print(f"Mes con mayor cantidad de cumpleaños: {mes_con_mas_cumpleanos(meses)[0]} con {mes_con_mas_cumpleanos(meses)[1]} cumpleaños.")


