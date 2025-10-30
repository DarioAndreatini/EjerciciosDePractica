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


def cantidadDeDigitos (numero):
    
    n = abs(numero)  
    
    if n < 10:
        return 1
    else:
        return 1 + cantidadDeDigitos(n // 10)
    
print(cantidadDeDigitos(1234))

# 2. Escribir una funcion que devuelva la suma de los N primeros digitos naturales

def sumaNaturales(n):
    if n == 0:
        return 0
    else:
        return n + sumaNaturales(n - 1)

print(sumaNaturales(2))

# 3. Tenemos una lista de libros con la cantidad de paginas de cada uno. Queremos saber cuantas paginas tenemos en total.

libros = [2, 2, 2, 2]

def sumarPaginas(libros):
    if not libros:
        return 0
    else:
        return libros[0] + sumarPaginas(libros[1:])
    
print(sumarPaginas(libros))

# 4. Convertir un numero Decimal a Binario. Por ejemplo, el 10 en decimal es 1010 es binario. El 15 es 1111 en binario.

def decimalABinario(n):
    if n == 0:
        return "0"
    elif n == 1:
        return "1"
    else:
        return decimalABinario(n // 2) + str(n % 2)
    
print(decimalABinario(123))