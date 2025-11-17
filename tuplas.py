# 1. Crear una variable utilizando tuplas que sea capaz de almacenar los valores de las cartas de la baraja española 
# (48 cartas; del 1 al 12 de basto, copa, espada y oro). 

# a. Crear una función que retorne una lista con una determina cantidad de cartas seleccionadas 
# al azar que será recibida como parámetro (junto con la variable que se creó el mazo).

# b. Utilizando la función anterior, obtenga 10 cartas del mazo e indique la cantidad de cartas que son de oro.

import random

def crearBaraja():
    """
    1. Crea una variable (tupla) que almacena la baraja española de 48 cartas.
    Cada carta es una tupla (numero, palo).
    """

    palos = ('oro', 'copa', 'espada', 'basto')
    
    numeros = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12')
    
    baraja_lista = []

    for palo in palos:
        for numero in numeros:
            carta = (numero, palo)
            baraja_lista.append(carta)
            
    return tuple(baraja_lista)

def repartirCartas (mazo_completo, cantidad):
    """
    1.a. Retorna una lista con una cantidad de cartas seleccionadas al azar.
    Usa random.sample para asegurarse de que las cartas no se repitan.
    """
    
    if cantidad > len(mazo_completo):
        return "Error: No se pueden repartir más cartas de las que hay en el mazo."
        
    mano = random.sample(list(mazo_completo), k=cantidad)
    return mano


# mazo = crearBaraja() # Contiene el mazo creado
# print(f"Mazo creado con {len(mazo)} cartas.")
# print("-" * 30)
# 
# 
# cantidadDeN = int(input("Ingrese la cantidad de cartas de tu mazo: "))
# mazo_de_n = repartirCartas(mazo, cantidadDeN)
# print(f"Mano repartida de {cantidadDeN} cartas: {mazo_de_n}")
# print("-" * 30)
# 
# mano_de_10 = repartirCartas(mazo, 10)
# print(f"Mano repartida de 10 cartas: {mano_de_10}")
# 
# contador_oro = 0
# for carta in mano_de_10:
#     palo_de_la_carta = carta[1]
#     
#     if palo_de_la_carta == 'oro':
#         contador_oro += 1
# 
# print("-" * 30)
# print(f"Resultado (1.b): En la mano de 10 cartas, hay {contador_oro} cartas de 'oro'.")

# 2. Escribir un programa que dadas dos tuplas de tres elementos, 
# realice el producto de cada elemento existente en la primera tupla con todos los restantes del segundo y almacene cada resultado en otra tupla. 
# Por ejemplo, el producto escalar entre (1, 2, 3) y (4, 5, 6); debería retornar: ((4, 5, 6),(8, 10, 12), (12, 15, 18)).

def generarTuplas():
    """
    Pide al usuario 3 valores para cada una de las dos tuplas
    y las retorna.
    """
    print("--- Ingreso Tupla 1 ---")

    tupla1 = (
        int(input("Ingrese valor 1 (T1): ")),
        int(input("Ingrese valor 2 (T1): ")),
        int(input("Ingrese valor 3 (T1): "))
    )
    
    print("\n--- Ingreso Tupla 2 ---")
    
    tupla2 = (
        int(input("Ingrese valor 1 (T2): ")),
        int(input("Ingrese valor 2 (T2): ")),
        int(input("Ingrese valor 3 (T2): "))
    )
    
    return tupla1, tupla2

def productoEscalarDeTuplas (tupla1, tupla2):
    
    tuplaProducto = []
    
    for i in tupla1:
        
        sub_tupla = []
        
        for j in tupla2:
            sub_tupla.append(i * j)
            
        tuplaProducto.append(tuple(sub_tupla))
            
    return tuple(tuplaProducto)

# tupla1, tupla2 = generarTuplas()

# print (productoEscalarDeTuplas(tupla1, tupla2))
    
# 3. Desarrolle un programa que procese una tabla con 10 horarios (hora -de 0 a 23- y minutos) en formato tupla; 
# e indique por cada una de ellas: si es AM o PM y cuántos minutos falta para la próxima hora. 
# El resultado de AM/PM y la cantidad de minutos se debe almacenar en una lista de tuplas con los valores originales y los resultados. 
# Imprimir el resultado final en pantalla.

horarios_a_procesar = [(8, 15), (0, 45), (12, 0), (14, 30), (23, 59), (11, 1)]

def procesadorDeHorarios (listaHoras):
    """
    Procesa una lista de tuplas de horarios (hora, minutos).
    
    Devuelve una lista de tuplas con el formato:
    ( (hora_original, min_original), (AM/PM, minutos_faltantes) )
    """
    
    lista_resultados = []
    
    for horario in listaHoras:
        
        hora, minutos = horario

        if hora < 12:
            am_pm = "AM"
        else:
            am_pm = "PM"
            
        minutos_faltantes = 60 - minutos
        
        resultado_procesado = (am_pm, minutos_faltantes)

        tupla_completa = (horario, resultado_procesado)
        

        lista_resultados.append(tupla_completa)
            
    return lista_resultados
    
        
# print (procesadorDeHorarios(horarios_a_procesar))

# 4. Juego de cartas: crea una función que genere aleatoriamente una mano de cinco cartas de una baraja de póker. 
# Cada carta debe ser representada por una tupla que contenga un número y un palo.

def generarManoPoker ():
    
    palos = ('as', 'pica', 'trebol', 'diamante')
    
    numeros = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', 'j', 'q', 'k')
    
    baraja_lista = []

    for palo in palos:
        for numero in numeros:
            carta = (numero, palo)
            baraja_lista.append(carta)
            
    return tuple(baraja_lista)

def repartirCartasPoker (mazo_completo):
    
    if 5 > len(mazo_completo):
        return "Error: No se pueden repartir más cartas de las que hay en el mazo."
        
    mano = random.sample(list(mazo_completo), 5)
    return mano
    
# mazoDe5 = generarManoPoker()
# print (repartirCartasPoker(mazoDe5))

# 5. Suma de números: crea un programa que lea una lista de tuplas, donde cada tupla contiene dos números enteros, 
# y calcule la suma de los números en cada tupla. 
# Por ejemplo, si llamamos a la función con la lista de tuplas [(1, 2), (3, 4), (5, 6)], 
# la función devolverá el valor 21, que es la suma de los números en todas las tuplas.


listaDeTuplas = [(3, 10), (5, 7), (2, 8), (1, 4)] 
listaDeTuplas2 = [(1, 2), (3, 4), (5, 6)]

def sumaDeTuplas (listaTuplas):
    
    suma_total = 0
    
    for tupla in listaTuplas:
        suma_total += sum(tupla)
        
    return suma_total

# print (sumaDeTuplas(listaDeTuplas2))

# 6. Cálculo de promedio: crea un programa que lea una lista de tuplas, 
# donde cada tupla contiene el nombre de un estudiante y una lista de calificaciones, 
# y calcule el promedio de calificaciones de cada estudiante. 
# Por ejemplo, 
# si llamamos a la función con la lista de tuplas [( 'Juan', [9, 8, 7]), ('Maria', [10, 9, 10]), ('Pedro', [8, 7, 9])], 
# la función devolverá la lista [( 'Juan', 8.0), ('Maria', 9.67), ('Pedro', 8.0)], 
# que contiene el nombre de cada estudiante y su promedio de calificaciones en forma de tuplas.

listaEstudiantes = [( 'Juan', [9, 8, 7]), ('Maria', [10, 9, 10]), ('Pedro', [8, 7, 9])]

def calcularPromedios (listaEstudiantes):
    
    for estudiante in listaEstudiantes:
        
        nombre = estudiante[0],
        calificaciones = estudiante[1]
        
        promedio = sum(calificaciones) / len(calificaciones)
        
        print (f"El promedio de {nombre} es: {promedio:.2f}")
        
        
# calcularPromedios(listaEstudiantes)

# 7. Cálculo de áreas: crea un programa que lea una lista de tuplas, 
# donde cada tupla contiene el nombre de una figura geométrica (cuadrado, rectángulo, triángulo y círculo) y sus dimensiones, 
# y calcule el área de cada figura.

import math

figuras = [
    ('cuadrado', 4),
    ('rectángulo', 4, 6),
    ('triángulo', 3, 5),
    ('círculo', 7)
]

def calcularAreas (listaFiguras):
    for figura in listaFiguras:
        
        nombre_figura = figura[0]
        
        if nombre_figura == 'cuadrado':
            lado = figura[1]
            area = lado ** 2
            
        elif nombre_figura == 'rectángulo':
            base = figura[1]
            altura = figura[2]
            area = base * altura
            
        elif nombre_figura == 'triángulo':
            base = figura[1]
            altura = figura[2]
            area = (base * altura) / 2
            
        elif nombre_figura == 'círculo':
            radio = figura[1]
            area = math.pi * (radio ** 2)
            
        else:
            area = None
            
        print (f"El área de la figura {nombre_figura} es: {area:.2f}")
        
# calcularAreas(figuras)







