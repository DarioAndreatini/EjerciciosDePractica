# Excepsiones - son los mensajes que tira el IDE que ocurren durante el tiempo de ejecucion

# Index Error - cuando accedo a una secuencia con un indice que no existe.

# Error de Sintaxis - Error en la escritura

# Errores de semantica - No causan errores durante la ejecucion pero devuelven algo que no es lo buscado

# "Mira antes de saltar" - Evita caer en el error

# "Es mas facil pedir perdon que permiso" - es en el uso de Try y Except


# Opcional - Finally (Limpia)

# Opcional - Else 

# Opcional - as e (Sirve para simplificar todos los casos de excepsion)

# 1. Desarrollar una función para ingresar a través del teclado un número. 
# La función rechazará cualquier ingreso inválido de datos utilizando excepciones y mostrará la razón exacta del error. 
# Devolver el valor ingresado cuando éste sea correcto. 
# Escribir también un programa que permita probar el correcto funcionamiento de la misma.


def ingresarNumero():
    """
    Solicita al usuario un número entero y no se detiene hasta que
    el ingreso sea válido, manejando errores con try-except.
    """

    while True:
        try:
            entrada_usuario = input("Ingrese un número entero: ")
            
            numero_valido = int(entrada_usuario)
            
        except ValueError:
            print(f"Error: '{entrada_usuario}' no es un número entero válido. Intente de nuevo.")
            
        else:
            print("¡Ingreso correcto!")
            return numero_valido 

# print("Iniciando programa de prueba...")
# numero_ingresado = ingresarNumero()
# 
# print(f"\nEl número que ingresaste y fue validado es: {numero_ingresado}")

# 2. Realizar una función que reciba como parámetros dos cadenas de caracteres conteniendo números reales, 
# sume ambos valores y devuelva el resultado como un número real. 
# Devolver None si alguna de las cadenas no contiene un número válido, utilizando manejo de excepciones para detectar el error.

def sumaDeValores (cadena1, cadena2):
    try:
        num1 = float(cadena1)
        num2 = float(cadena2)
        
        return num1 + num2
        
    except ValueError:
        return None


# print( sumaDeValores('hola', '11') )
# print( sumaDeValores('10', '10') )
# print( sumaDeValores('10', 'hola') )

# 3. Desarrollar una función que devuelva una cadena de caracteres con el nombre del mes cuyo número se recibe como parámetro. 
# Los nombres de los meses deberán obtenerse de una tupla de cadenas de caracteres inicializada dentro de la función. 
# Devolver una cadena vacía si el número de mes es inválido. 
# La detección de meses inválidos deberá realizarse a través de excepciones.

def nombreDelMes (nroMes):
    
    nombres_meses = ('Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre')
    
    try:
        if nroMes < 1:
            raise IndexError("El número de mes debe ser 1 o mayor.")
            
        nombre = nombres_meses[nroMes - 1]
        return nombre
    
    except IndexError:
        return ""
        
        
# print( nombreDelMes(6) )        
    

# 4. El método index permite buscar un elemento dentro de una lista, devolviendo la posición que éste ocupa. 
# Sin embargo, si el elemento no pertenece a la lista se produce una excepción de tipo ValueError. 
# Desarrollar un programa que cargue una lista con números enteros ingresados a través del teclado (terminando con -1) y 
# permita que el usuario ingrese el valor de algunos elementos para visualizar la posición que ocupan, utilizando el método index. 
# Si el número no pertenece a la lista se imprimirá un mensaje de error y se solicitará otro para buscar. 
# Abortar el proceso al tercer error detectado. No utilizar el operador in durante la búsqueda.

def cargarLista():
   
    lista = []
    while True:
        try:
            ingreso_str = input("Ingrese valor para la lista (-1 para terminar): ")
            ingreso = int(ingreso_str)
            
            if ingreso == -1:
                break 
            
            lista.append(ingreso)
            
        except ValueError:
            print(f"Error: '{ingreso_str}' no es un entero. Intente de nuevo.")
            
    print(f"Lista cargada: {lista}")
    return lista

def buscarElemento (listaNumeros):
    
    try:
        if len(listaNumeros) == 0:
            return print("La lista esta vacia!")
        
        elemento = int(input("Ingrese elemento buscado (-1 para salir): "))
        
        while elemento != -1:
        
            posicion = listaNumeros.index(elemento)
            print(f"El elemento {elemento} esta en la posicion {posicion+1}")
        
            elemento = int(input("Ingrese elemento buscado (-1 para salir): ")) 
            
    except ValueError:
        return print(f"No esta el '{elemento}' en la lista")


# mi_lista = cargarLista()
# 
# buscarElemento(mi_lista)

# 5. Escribir un programa que juegue con el usuario a adivinar un número. 
# El programa debe generar un número al azar entre 1 y 500 y el usuario debe adivinarlo. 
# Para eso, cada vez que se introduce un valor se muestra un mensaje indicando si el número que tiene que adivinar es mayor o menor que el ingresado. 
# Cuando consiga adivinarlo, se debe imprimir en pantalla la cantidad de intentos que le tomó hallar el número. 
# Si el usuario introduce algo que no sea un número se mostrará un mensaje en pantalla y se lo contará como un intento más.

import random

def adivinarNumero ():
    numero_secreto = random.randint(1, 500)
    contadorIntentos = 0
    adivinado = False
    
    while not adivinado:
        
        contadorIntentos += 1
        
        try:
            entrada_str = input(f"Intento #{contadorIntentos}: Ingresa tu número: ")
            
            entrada_num = int(entrada_str)
            
            if entrada_num < numero_secreto:
                print(f"¡Fallaste! El número secreto es MAYOR que {entrada_num}.")
            elif entrada_num > numero_secreto:
                print(f"¡Fallaste! El número secreto es MENOR que {entrada_num}.")
            else:
                print(f"¡FELICIDADES! ¡Adivinaste el número secreto: {numero_secreto}!")
                print(f"Te tomó {contadorIntentos} intentos.")
                adivinado = True
        
        except ValueError:
            print(f"Error: '{entrada_str}' no es un número válido. Se cuenta como un intento.")

# adivinarNumero()

# 6. Convertir una cadena en un número: 
# Escribe un programa que solicite al usuario una cadena y luego intente convertirla en un número entero. 
# Si la conversión falla, muestra un mensaje de error.

def convertirCadenaEnNumero (cadena):
    
    try:
        cadena = int(cadena)
        
        print(f"La cadena {cadena} ahora es un numero")
        
    except ValueError:
        print (f"No se puede convertir {cadena} en numero")
        
#convertirCadenaEnNumero("1234")
#
#convertirCadenaEnNumero("12c34")

# 7. Escribe una función llamada calcularRaizCuadrada que reciba un número como argumento y calcule su raíz cuadrada. 
# Si el número es negativo, 
# la función debe generar una excepción ValueError con un mensaje 
# indicando que no se puede calcular la raíz cuadrada de un número negativo.

import math

def calcularRaizCuadrada (numero):
    
    if numero < 0:
        raise ValueError (f"No se puede calcular la raíz cuadrada de un número negativo ({numero}).")
    
    return math.sqrt(numero)
   
# numeros_a_probar = [4, 16, -4, 25, -9, 0]
# 
# for num in numeros_a_probar:
#     try:
#         resultado = calcularRaizCuadrada(num)
#         print(f"ÉXITO: La raíz cuadrada de {num} es {resultado}")
# 
#     except ValueError as e:
#         print(f"ERROR: {e}")


# 8. Escribe un programa que pida al usuario que ingrese dos números enteros 
# y muestre el resultado de la división del primer número por el segundo. 
# Si el segundo número es cero, muestra un mensaje de error y vuelve a solicitar el segundo número hasta que sea diferente de cero. 
# Lo mismo si el tipo de dato ingresado no es correcto. 
# Con cada intento de realizar la operación se debe mostrar en pantalla la leyenda: «Se ha intentado realizar una división».

def divisionDeNumeros ():
    
    num1 = None
    num2 = None
    
    while num1 is None:
        try:
            print("Se ha intentado realizar una división (pidiendo dividendo)")
            num1 = int(input("Ingrese el primer número (dividendo): "))
            
        except ValueError:
            print(f"Error: '{num1}' no es un entero válido. Intente de nuevo.")
    
    while num2 is None:
        try:
            print("Se ha intentado realizar una división (pidiendo divisor)")
            num2 = int(input("Ingrese el segundo número (divisor): "))
            
            resultado = num1 / num2
            
        except ValueError:
            print(f"Error: '{num2}' no es un entero válido. Vuelva a ingresar el segundo número.")
            
        except ZeroDivisionError:
            print("Error: El divisor no puede ser cero. Vuelva a ingresar el segundo número.")
        
        else:
            print("\n¡División exitosa!")
            print(f"El resultado de {num1} / {num2} es: {resultado}")

print (divisionDeNumeros())