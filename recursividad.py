# Recursividad - Es la manera de resolver problemas sin bucles

# def cuentaRegresiva (numero):
#     
#     if numero > 0:
#         print(numero)
#         cuentaRegresiva(numero-1) # Llamado recursivo
#     else:
#         print("STOP") # Caso Base
# 
# 
# cuentaRegresiva(4)

# 1. Escribi una funcion que devuelva la cantidad de digitos de un numero


def cantidadDeDigitosDeNumero(numero):
    
    n = abs(numero)
    
    if n < 0:
        numero = -numero
    elif n < 10:
        return 1
    else:
        return print(1 + cantidadDeDigitosDeNumero(n // 10))
    

# cantidadDeDigitosDeNumero(12)
    

# 2. Desarrollar una función que devuelva el producto de dos números enteros por sumas sucesivas.

def productoDeEnteros (n, cantidad):
    
    if n == 0:
        return 0
    else: 
        # print(n, cantidad)
        return cantidad + productoDeEnteros(n-1, cantidad)

    
# print(productoDeEnteros(5, 4))
    

# 3. Escribir una función que devuelva la suma de los N primeros números naturales.

def sumaDeNPrimeros (n):
    
    if n <= 0:
        return n
    else:
        return n + sumaDeNPrimeros(n-1)

# print(sumaDeNPrimeros(1))

# 4. Convertir un numero Decimal a Binario. Por ejemplo, el 10 en decimal es 1010 es binario. El 15 es 1111 en binario.

def convertirDeDecimalABinario (n):
    
    if n == 0:
        return ""
    else:
        return str(convertirDeDecimalABinario(n // 2)) + str(n % 2)
    
# print (convertirDeDecimalABinario(10))

# 5. Escriba un programa, utilizando recursividad, que pueda retornar el resultado de la multiplicación mediante el método ruso, que consiste en:
# •	Escribir los números (A y B) que se desea multiplicar en la parte superior de sendas columnas.
# •	Dividir A entre 2, sucesivamente, ignorando el residuo, hasta llegar a la unidad. Escribir los resultados en la columna A.
# •	Multiplicar B por 2 tantas veces como veces se ha dividido A entre 2. Escribir los resultados sucesivos en la columna B.
# •	Sumar todos los números de la columna B que estén al lado de un número impar de la columna A. Éste es el resultado.

def metodoRuso (a, b):
    
    if a == 0 or b == 0:
        return 0
    
    if a % 2 != 0:
        return b + metodoRuso(a // 2, b * 2)
    else:
        return metodoRuso(a // 2, b * 2)
    
# print(metodoRuso(11,33))

# 6. Explique cuál es el objetivo de la siguiente función. Realice una explicación y verifique los resultados.
def f(x):
    if (x > 100):
        return (x-10)
    else:
        return (f(f(x+11)))

# print( f(2) )

# El objetivo es que un numero es mayor a 100 re reste 10 pero si no, le tiene que sumar 11 hasta que cumpla la condicion inicial.

# 7. Programe una función recursiva para verificar si una palabra es un palíndromo.

def palindromo (palabra):
    
    if len(palabra) <= 1:
        return True
    
    if palabra[0] == palabra[-1]:
        print(palabra[1:-1])
        return palindromo(palabra[1:-1])
    else: 
        return False
        
print( palindromo ("looppool") )