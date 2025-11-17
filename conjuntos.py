# 1.	Definir un conjunto con números enteros entre 0 y 9. 
# Luego solicitar valores al usuario y eliminarlos del conjunto mediante el método remove, 
# mostrando el contenido del conjunto luego de cada eliminación. Finalizar el proceso al ingresar -1. 
# Utilizar manejo de excepciones para evitar errores al intentar quitar elementos inexistentes.

import random

def crearConjuntoEnteros():
    return set(range(10))

def eliminarElementosDelConjunto(conjunto):
    
    bandera = True
    
    while bandera:
        try:
            valor = int(input("Ingrese un número entero entre 0 y 9 para eliminar (-1 para finalizar): "))
            
            if valor == -1:
                bandera = False
            
            conjunto.remove(valor)
            print(f"Elemento {valor} eliminado. Conjunto actual: {conjunto}")
        
        except ValueError:
            print("Error: Por favor, ingrese un número entero válido.")
        
        except KeyError:
            print(f"Error: El elemento {valor} no existe en el conjunto.")
            
            
# conjunto_enteros = crearConjuntoEnteros()
# print(f"Conjunto inicial: {conjunto_enteros}")
# eliminarElementosDelConjunto(conjunto_enteros)
# print(f"Conjunto final: {conjunto_enteros}")


# 2.	Crear tres conjuntos:
# •	pares: valores pares entre 0 y 100
# •	impares: valores impares entre 0 y 100
# •	azar: 50 valores al azar entre 0 y 100

# Una vez generados los tres conjuntos, deberá realizar las siguientes acciones:
# •	generar dos nuevos conjuntos: uno con la intersección entre azar y pares; y azar e impares. 
#   Informe de cada uno de ellos: la cantidad, el valor máximo y mínimo.

def generarConjuntos():
    pares = {num for num in range(101) if num % 2 == 0}
    impares = {num for num in range(101) if num % 2 != 0}
    azar = {random.randint(0, 100) for _ in range(50)}
    
    return pares, impares, azar

pares, impares, azar = generarConjuntos()

conjunto_azar_pares = azar.intersection(pares)
conjunto_azar_impares = azar.intersection(impares)

def informarConjunto(conjunto, descripcion):
    if conjunto:
        print(f"{descripcion}: Cantidad = {len(conjunto)}, Máximo = {max(conjunto)}, Mínimo = {min(conjunto)}")
    else:
        print(f"{descripcion}: El conjunto está vacío.")
        
# informarConjunto(conjunto_azar_pares, "Intersección entre azar y pares")
# informarConjunto(conjunto_azar_impares, "Intersección entre azar e impares")

# 3. Crear dos conjuntos con cinco valores generados al azar, que se encuentre entre 1 y 10. Al finalizar, realizar:
# •	    Mostrar los valores que son en común entre ambos conjuntos
# •	    Luego, volcar desde el primer conjunto al segundo, aquellos valores que no se encuentran del primero en el segundo

 
def generConjuntos ():
    conjunto1 = {random.randint(1, 10) for _ in range(5)}
    conjunto2 = {random.randint(1, 10) for _ in range(5)}
    
    return conjunto1, conjunto2

conjunto1, conjunto2 = generConjuntos()

# print(f"Conjunto 1: {conjunto1}")
# print(f"Conjunto 2: {conjunto2}")

comunes = conjunto1.intersection(conjunto2)
# print(f"Valores en común: {comunes}")

valores_a_volcar = conjunto1.difference(conjunto2)
conjunto2.update(valores_a_volcar)
# print(f"Conjunto 2 después de volcar valores: {conjunto2}")


# 4. Crea una función para unir conjuntos: 
# Crea una función que tome dos conjuntos como argumentos y devuelva un conjunto que contenga todos los elementos de ambos conjuntos. 
# Asegúrate de que la función maneje conjuntos con diferentes tipos de elementos, como cadenas y números.

def unirConjuntos(conjuntoA, conjuntoB):
    return conjuntoA.union(conjuntoB)

# 5. Eliminar duplicados de una lista con conjuntos: 
# Crea una función que tome una lista y elimine los elementos duplicados utilizando conjuntos. 
# La función debe devolver una lista sin elementos duplicados.

def eliminarDuplicados(lista):
    conjunto = set(lista) # El set genera un conjunto y, en un conjunto, no pueden existir elementos duplicados
    return list(conjunto)

# lista_con_duplicados = [1, 2, 2, 2, 2, 2, 2, 4, 4, 3, 4, 4, 5]
# lista_sin_duplicados = eliminarDuplicados(lista_con_duplicados)
# print(lista_sin_duplicados)  # Salida: [1, 2, 3, 4, 5]

# 6. Palabras únicas en una cadena: 
# Crea una función que tome una cadena como argumento y devuelva un conjunto que contenga todas las palabras únicas en la cadena.

lista_palabras = "esto es una prueba esto es solo una prueba"

def palabrasUnicas(cadena):
    palabras = cadena.split()  # Dividir la cadena en palabras
    conjunto_palabras = set(palabras)  # Crear un conjunto con las palabras
    return conjunto_palabras

# conjunto_palabras_unicas = palabrasUnicas(lista_palabras)
# print(conjunto_palabras_unicas)  # Salida: {'esto', 'es', 'una', 'prueba', 'solo'}

# 7. Cuenta la cantidad de palabras únicas en una cadena: 
# Crea una función que tome una cadena como argumento y devuelva la cantidad de palabras únicas en la cadena. 
# Para hacerlo, puedes utilizar conjuntos y el método len() de Python.

lista_palabras = "esto es una prueba esto es solo una prueba"

def contarPalabrasUnicas(cadena):
    palabras = cadena.split()  # Dividir la cadena en palabras
    conjunto_palabras = set(palabras)  # Crear un conjunto con las palabras
    return len(conjunto_palabras)

# cantidad_palabras_unicas = contarPalabrasUnicas(lista_palabras)
# print(cantidad_palabras_unicas)  # Salida: 5

# 8. Contar elementos únicos en una lista: 
# Crea una función que tome una lista como argumento y devuelva el número de elementos únicos en la lista.
 
lista_elementos = [1, 2, 2, 3, 4, 4, 5, 5, 5, 'hola', 'mundo', 'hola', 'python', 'python']

def contarElementosUnicos(lista):
    conjunto_elementos = set(lista)  # Crear un conjunto con los elementos de la lista
    return len(conjunto_elementos)

# cantidad_elementos_unicos = contarElementosUnicos(lista_elementos)
# print(cantidad_elementos_unicos)  # Salida: 7

# 9. Crear una lista de valores únicos a partir de un diccionario: 
# Crea una función que tome un diccionario como argumento y devuelva una lista con los valores únicos del diccionario.

diccionario = {
    'a': 1,
    'b': 2,
    'c': 2,
    'd': 3,
    'e': 4,
    'f': 4,
    'g': 5
}

def valoresUnicosDeDiccionario(dic):
    valores = dic.values()  # Obtener los valores del diccionario
    conjunto_valores = set(valores)  # Crear un conjunto con los valores para eliminar duplicados
    return list(conjunto_valores)  # Convertir el conjunto de nuevo a una lista

# lista_valores_unicos = valoresUnicosDeDiccionario(diccionario)
# print(lista_valores_unicos)  # Salida: [1, 2, 3, 4, 5]

# 10. Eliminar elementos comunes de un diccionario: 
# Crea una función que tome dos diccionarios como argumentos y 
# devuelva un nuevo diccionario que contenga solo las claves del primer diccionario que no estén en el segundo diccionario.

diccionario1 = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4
}

diccionario2 = {
    'c': 30, 
    'd': 40,
    'e': 50
}

def eliminarClavesComunes(dic1, dic2):
    conjunto_claves_dic2 = set(dic2.keys())  # Obtener las claves del segundo diccionario como un conjunto
    nuevo_diccionario = {clave: valor for clave, valor in dic1.items() if clave not in conjunto_claves_dic2}
    return nuevo_diccionario    

# nuevo_diccionario = eliminarClavesComunes(diccionario1, diccionario2)
# print(nuevo_diccionario)  # Salida: {'a': 1, 'b': 2}

