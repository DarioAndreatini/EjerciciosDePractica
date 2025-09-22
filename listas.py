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

N = int(input("Ingrese la cantidad de números a generar (N): "))
lista1 = generar_lista_sin_repetidos(N)       
print("Lista sin repetidos (método 1):", lista1)
lista2 = generar_lista_y_eliminar_duplicados(N)
print("Lista sin repetidos (método 2):", lista2)



