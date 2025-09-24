# 1
"""
Desarrollar cada una de las siguientes funciones y escribir un programa que permita verificar su 
funcionamiento imprimiendo la lista luego de invocar a cada función:

a.	Cargar una lista con números al azar de cuatro dígitos. La cantidad de elementos también será un número al azar de dos dígitos. 
    Realice la composición de la lista por comprensión y de la forma habitual (tendrá dos funciones distintas).
    
b.	Calcular y devolver la sumatoria de todos los elementos de la lista anterior.

c.	Eliminar todas las apariciones de un valor en la lista anterior. 
    El valor a eliminar se ingresa desde el teclado y la función lo recibe como parámetro. Utilice comprensión de listas para resolverlo.
    
d.	Determinar si el contenido de una lista cualquiera es capicúa, sin usar listas auxiliares. Un ejemplo de lista capicúa es [50,17,91,17,50].
"""

# a

import random

def cargar_lista_comprension():
    cantidad = random.randint(10, 99)  # Número al azar de dos dígitos
    lista = [random.randint(1000, 9999) for _ in range(cantidad)]  # Números al azar de cuatro dígitos
    return lista

# b

def sumatoria(lista):
    return sum(lista)

# c

def eliminar_valor(lista, valor):
    return [x for x in lista if x != valor]

# d

def es_capicua(lista):
    izquierda = 0
    derecha = len(lista) - 1
    while izquierda < derecha:
        if lista[izquierda] != lista[derecha]:
            return False
        izquierda += 1
        derecha -= 1
    return True

# 2
"""
Escribir funciones para:
a.	Generar una lista de 50 números aleatorios del 1 al 100. Utilice comprensión de listas para generar el resultado.
b.	Recibir una lista como parámetro y devolver True si la misma contiene algún elemento repetido. La función no debe modificar la lista.
c.	Recibir una lista como parámetro y devolver una nueva lista con los elementos únicos de la lista original, sin importar el orden.
Combinar estas tres funciones en un mismo programa.
"""

# a

def generar_lista_aleatoria():
    return [random.randint(1, 100) for _ in range(50)]

# b

def tiene_repetidos(lista):
    return len(lista) != len(set(lista))

# c

def elementos_unicos(lista):
    return list(set(lista))

# 3
"""
Crear una lista con los cuadrados de los números entre 1 y N (ambos incluidos), donde N se ingresa desde el teclado. 
Luego se solicita imprimir los últimos 10 valores de la lista utilizando segmentación de listas.
"""

def cuadrados_hasta_n(n):
    return [i**2 for i in range(1, n+1)]    

# N = int(input("Ingrese un número N: "))
# lista_cuadrados = cuadrados_hasta_n(N)
# print("Últimos 10 valores de la lista de cuadrados:", lista_cuadrados[-10:])

# 4
"""
Eliminar de una lista de palabras las palabras que se encuentren en una segunda lista. 
Imprimir la lista original, la lista de palabras a eliminar y la lista resultante.}
"""

def eliminar_palabras(lista_original, lista_a_eliminar):
    return [palabra for palabra in lista_original if palabra not in lista_a_eliminar]

# lista_original = ["manzana", "banana", "naranja", "pera", "uva"]
# lista_a_eliminar = ["banana", "pera"]
# lista_resultante = eliminar_palabras(lista_original, lista_a_eliminar)
# print("Lista original:", lista_original)
# print("Lista a eliminar:", lista_a_eliminar)
# print("Lista resultante:", lista_resultante)

# 6
"""
Intercalar los elementos de una lista entre los elementos de otra. 
La intercalación deberá realizarse exclusivamente mediante la técnica de rebanadas 
y no se creará una lista nueva sino que se modificará la primera. 
Por ejemplo, si lista1 = [8, 1, 3] y lista2 = [5,9,7], lista1 deberá quedar como [8,5,1,9,3,7].
"""

def intercalar_listas(lista1, lista2):
    lista1[:] = [elem for par in zip(lista1, lista2) for elem in par]
    return lista1

lista1 = [8, 1, 3]
lista2 = [5, 9, 7]
# lista_intercalada = intercalar_listas(lista1, lista2)
# print("Lista intercalada:", lista_intercalada)
# print("Lista original modificada:", lista1)  # Verificar que lista1 ha sido modificada
# print("Lista 2:", lista2)  # Verificar que lista2 no ha sido modificada

# 8
"""
Generar e imprimir una lista por comprensión entre A y B con los múltiplos de 7 que no sean múltiplos de 5. 
A y B se ingresan desde el teclado.
"""

def multiplos_de_7_no_de_5(a, b):
    return [x for x in range(a, b+1) if x % 7 == 0 and x % 5 != 0]

# A = int(input("Ingrese el valor de A: "))
# B = int(input("Ingrese el valor de B: "))
# lista_multiplos = multiplos_de_7_no_de_5(A, B)
# print("Lista de múltiplos de 7 que no son múltiplos de 5 entre A y B:", lista_multiplos)

# 10
"""
Una clínica necesita un programa para atender a sus pacientes. 
Cada paciente que ingresa se anuncia en la recepción indicando su número de afiliado (número entero de 4 dígitos) 
y además indica si viene por una urgencia (ingresando un 0) o con turno (ingresando un 1). 
Para finalizar se ingresa -1 como número de socio. 

Luego se solicita:

a.	Mostrar un listado de los pacientes atendidos por urgencia y un listado de los pacientes atendidos por turno en el orden
    que llegaron a la clínica.
b.	Realizar la búsqueda de un número de afiliado e informar cuántas veces fue atendido por turno y cuántas por urgencia.

Repetir esta búsqueda hasta que se ingrese -1 como número de afiliado.
"""

def atender_pacientes():
    urgencias = []
    turnos = []
    
    numero_afiliado = int(input("Ingrese el número de afiliado (4 dígitos) o -1 para finalizar: "))
    while numero_afiliado != -1:
        tipo_atencion = int(input("Ingrese 0 para urgencia o 1 para turno: "))
        if tipo_atencion == 0:
            urgencias.append(numero_afiliado)
        elif tipo_atencion == 1:
            turnos.append(numero_afiliado)
        else:
            print("Tipo de atención inválido. Intente nuevamente.")

        numero_afiliado = int(input("Ingrese el número de afiliado (4 dígitos) o -1 para finalizar: "))

    print("\nListado de pacientes atendidos por urgencia:", urgencias)
    print("Listado de pacientes atendidos por turno:", turnos)

    busqueda = int(input("\nIngrese un número de afiliado para buscar (o -1 para finalizar): "))
    while busqueda != -1:
        atenciones_urgencia = urgencias.count(busqueda)
        atenciones_turno = turnos.count(busqueda)
        print(f"Número de afiliado {busqueda} fue atendido {atenciones_urgencia} veces por urgencia y {atenciones_turno} veces por turno.")

        busqueda = int(input("\nIngrese un número de afiliado para buscar (o -1 para finalizar): "))
        
atender_pacientes()





