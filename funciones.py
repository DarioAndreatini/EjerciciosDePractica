# 1
"""
Escribir una función que reciba como parámetros dos números enteros. Calcular
y devolver el resultado de la multiplicación de ambos valores utilizando solamente sumas. Por ejemplo 4 * 3 = 4 + 4 + 4 .

"""

def multiplicar(a, b):
    resultado = 0
    negativo = False
    
    if b < 0:
        b = -b
        negativo = True
    
    for _ in range(b):
        resultado += a
    
    return -resultado if negativo else resultado
# 
# 
# 
# a = int(input("Ingrese el primer número: "))
# b = int(input("Ingrese el segundo número: "))
# 
# print(f"{multiplicar(a, b)}")

# 2
"""
Dados dos parámetros enteros A y B, obtener AB
(A elevado a la B) mediante
multiplicaciones sucesivas, utilizando la función del ejercicio anterior para multiplicar. Por ejemplo 43
 = 4 * 4 * 4.
"""

# def potencia(base, exponente):
#     if exponente == 0:
#         return 1
#     
#     resultado = base
#     for _ in range(exponente - 1):
#         resultado = multiplicar(resultado, base)
#     
#     return resultado
# 
# 
# a = int(input("Ingrese el primer número: "))
# b = int(input("Ingrese el segundo número: "))
# 
# print(f"{potencia(a, b)}")

# 3
"""
Imprimir una columna de asteriscos, donde su altura se recibe como parámetro.
"""

# def hacer_columna(altura):
#     for _ in range(altura):
#         print("*")
#         
# a = int(input("Ingrese la altura de la columna: "))
# 
# hacer_columna(a)

# 4
"""
Devolver True si el número entero recibido como primer parámetro es múltiplo
del segundo, o False en caso contrario. Ejemplo: esmultiplo(40, 8) devuelve True
y esmultiplo(50, 3) devuelve False.
"""

def es_multiplo(a, b):
    return a % b == 0
# 
# a = int(input("Ingrese el primer número: "))
# b = int(input("Ingrese el segundo número: "))
# 
# print(es_multiplo(a, b))

# 5
"""
Desarrollar la función signo(n), que reciba un número entero y devuelva 1, -1 o
0 según el valor recibido sea positivo, negativo o nulo.
"""

def signo(n):
    if n > 0:
        return 1
    elif n < 0:
        return -1
    else:
        return 0
    
# n = int(input("Ingrese un número: "))
# 
# print(signo(n))

# 6
"""
Escribir la función comparar(a, b) que reciba como parámetros dos números enteros y devuelva 1 si el primero es mayor que el segundo, 0 si son iguales o -1 si
el primero es menor que el segundo. En este ejercicio debe aprovecharse la función del ejercicio anterior. Ejemplo: comparar(4, 2) devuelve 1, y comparar(2, 4)
devuelve -1.
"""

def comparar(a, b):
    return signo(a - b)     

# a = int(input("Ingrese el primer número: "))
# b = int(input("Ingrese el segundo número: "))
# 
# print(comparar(a, b))

# 7
"""
Calcular y devolver el Máximo Común Divisor de dos enteros no negativos, basándose en las siguientes fórmulas matemáticas:
· MCD(X,X) = X
· MCD(X,Y) = MCD(Y, X)
· Si X > Y => MCD(X, Y) = MCD(X-Y, Y).
Ejemplo: MCD(40, 15) devuelve 5.
"""

def mcd(x, y):
    if x == y:
        return x
    elif x < y:
        return mcd(y, x)
    else:
        return mcd(x - y, y)
    
# x = int(input("Ingrese el primer número: "))
# y = int(input("Ingrese el segundo número: "))
#         
# print(mcd(x, y))

# 8
"""
La raíz cuadrada de un número positivo n puede calcularse mediante la siguiente
fórmula de Newton: formula: raiz a = (a + n/a) / 2 , donde a es una aproximación a n. 
Al aplicar repetidamente esta fórmula reemplazando a por la aproximación obtenida en el paso anterior, se obtiene cada vez una aproximación mejor. 
Desarrollar un programa que calcule la raíz cuadrada aproximada de un número entero positivo n utilizando como primera aproximación a n/2. 
Detener el proceso cuando la diferencia entre dos cálculos sucesivos sea menor a 0,0001.
"""

def raiz_cuadrada(n):
    a = n / 2.0
    while True:
        nueva_a = (a + n / a) / 2.0
        if abs(nueva_a - a) < 0.0001:
            break
        a = nueva_a
    return a

# n = int(input("Ingrese un número: "))
# print(raiz_cuadrada(n))

# 9
"""
Escribir una función que reciba como parámetros un número de día, un número 
de mes y un número de año y devuelva la cantidad de días que faltan hasta fin de mes. 
Luego desarrollar tres programas para:
· Ingresar una fecha formada por tres enteros (día, mes y año) e imprimir la cantidad de días que faltan hasta fin de año.
· Ingresar una fecha formada por tres enteros (día, mes y año) e imprimir la cantidad de días transcurridos en ese año hasta esa fecha.
· Ingresar dos fechas formadas por tres enteros (día, mes y año) e imprimir cuánto tiempo transcurrió entre ambas, expresando el resultado en
años, meses y días.
Los tres programas deben realizar su trabajo a través de la función indicada al
comienzo.
"""

from datetime import date

def es_bisiesto(anio):
    return (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)

def dias_en_mes(mes, anio):
    if mes in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif mes in [4, 6, 9, 11]:
        return 30
    elif mes == 2:
        return 29 if es_bisiesto(anio) else 28
    else:
        raise ValueError(f"Mes inválido: {mes}")

# Ejercicio principal
def dias_hasta_fin_mes(dia, mes, anio):
    return dias_en_mes(mes, anio) - dia

# Ejercicio 1
def dias_hasta_fin_anio(dia, mes, anio):
    total = dias_hasta_fin_mes(dia, mes, anio)
    for m in range(mes + 1, 13):
        total += dias_en_mes(m, anio)
    return total

# Ejercicio 2
def dias_transcurridos(dia, mes, anio):
    total = dia
    for m in range(1, mes):
        total += dias_en_mes(m, anio)
    return total

# Ejercicio 3
def diferencia_fechas(d1, m1, a1):
    
    d2 = int(input("Ingrese el día: "))
    m2 = int(input("Ingrese el mes: "))
    a2 = int(input("Ingrese el año: "))
    
    f1 = date(a1, m1, d1)
    f2 = date(a2, m2, d2)
    if f1 > f2:
        f1, f2 = f2, f1

    # diferencia total en días
    delta = f2 - f1

    # cálculo en años, meses y días
    anios = f2.year - f1.year
    meses = f2.month - f1.month
    dias = f2.day - f1.day

    if dias < 0:
        meses -= 1
        mes_anterior = f2.month - 1 if f2.month > 1 else 12
        anio_anterior = f2.year if f2.month > 1 else f2.year - 1
        dias += dias_en_mes(mes_anterior, anio_anterior)

    if meses < 0:
        anios -= 1
        meses += 12

    return delta.days


# dia = int(input("Ingrese el día: "))
# mes = int(input("Ingrese el mes: "))
# anio = int(input("Ingrese el año: "))
# 
# print(f"Faltan {dias_hasta_fin_mes(dia, mes, anio)} días para fin de mes.")
# print(f"Faltan {dias_hasta_fin_anio(dia, mes, anio)} días para fin de año.")
# print(f"Han transcurrido {dias_transcurridos(dia, mes, anio)} días en este año.")
# print(f"Han diferencia de {diferencia_fechas(dia, mes, anio)} días entre fechas.")

# 10
"""
Extraer un dígito de un número. La función recibe como parámetros dos números enteros, 
uno será del que se extraiga el dígito y el otro indica qué cifra se desea obtener. 
La cifra de la derecha se considera la número 0. Retornar el valor -1 si no existe el dígito solicitado. Tener en cuenta que el número puede ser positivo o negativo. 
Ejemplo: extraerdigito(12345, 1) devuelve 4, y extraerdigito(12345, 8) devuelve -1.
"""

def extraer_digito(numero, posicion):
    numero = abs(numero)  # ignoramos el signo
    numero_str = str(numero)

    if posicion < 0 or posicion >= len(numero_str):
        return -1

    return int(numero_str[-(posicion + 1)])

# numero = int(input("Ingrese un número: "))
# posicion = int(input("Ingrese la posición del dígito a extraer: "))
# 
# print(extraer_digito(numero, posicion))

# 11
"""
Obtener el dígito central de un número entero pasado como parámetro, sólo si la cantidad de dígitos es impar. 
Si la longitud fuera par devolver -1. Ejemplo:
digitocentral(12345) devuelve 3, y digitocentral(123456) devuelve -1.
"""

def digito_central(numero):
    numero = abs(numero) 
    numero_str = str(numero)
    longitud = len(numero_str)

    if longitud % 2 == 0:
        return -1

    posicion_central = longitud // 2
    return int(numero_str[posicion_central])

numero = int(input("Ingrese un número: "))

print(digito_central(numero))

