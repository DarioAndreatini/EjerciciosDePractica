# 1
"""
Desarrolle un programa que almacene datos de canciones en formato MP3:
Artista, Título, Duración (en segundos), Tamaño del fichero (en KB). Un programa
debe pedir los datos de una canción al usuario y después mostrarlos en pantalla.
Debe interrumpirse la carga cuando el artista ingresado sea vacío.
"""

def cargar_canciones():
    canciones = []
    artista = input("Ingrese el nombre del artista (ponga fin para terminar): ")

    while artista != "fin":
        titulo = input("Ingrese el título de la canción: ")
        duracion = int(input("Ingrese la duración en segundos: "))
        tamano = int(input("Ingrese el tamaño del fichero en KB: "))
        
        cancion = {
            "Artista": artista,
            "Título": titulo,
            "Duración": duracion,
            "Tamaño (KB)": tamano
        }
        canciones.append(cancion)

        artista = input("Ingrese el nombre del artista (ponga fin para terminar): ")

    return canciones

# canciones = cargar_canciones()
# print("Canciones cargadas:")
# for cancion in canciones:
#     print(cancion)

# 2
"""
Escriba un programa que ingrese (por teclado) los datos de diez personas (nombre,
edad, genero, dirección, teléfono), los almacene en un diccionario y los muestre. Al
realizar dicha muestra, destacar la persona más joven en edad.
"""

def cargar_personas():
    personas = []
    for _ in range(2): # Pongo 2 para que sea mas corto pero deberia ir 10.
        nombre = input("Ingrese el nombre: ")
        edad = int(input("Ingrese la edad: "))
        genero = input("Ingrese el género: ")
        direccion = input("Ingrese la dirección: ")
        telefono = input("Ingrese el teléfono: ")

        persona = {
            "Nombre": nombre,
            "Edad": edad,
            "Género": genero,
            "Dirección": direccion,
            "Teléfono": telefono
        }
        personas.append(persona)
    
    return personas

def mostrar_personas(personas):
    if not personas:
        print("No hay personas para mostrar.")
        return

    persona_mas_joven = min(personas, key=lambda x: x["Edad"]) # Obtienen el numero mas bajo de la clave edad 

    for persona in personas:
        if persona == persona_mas_joven:
            print(f"* {persona} (La persona más joven)")
        else:
            print(persona)
            
# personas = cargar_personas()
# mostrar_personas(personas)

# 3
"""
Hacer un programa que registre 10 alumnos y guarde: nombre, nombre de la asignatura
y 4 notas. Calcular y mostrar el promedio de las notas.
"""

def cargar_alumnos():
    alumnos = []
    for _ in range(2): # Pongo 2 para que sea mas corto pero deberia ir 10.
        nombre = input("Ingrese el nombre del alumno: ")
        asignatura = input("Ingrese el nombre de la asignatura: ")
        notas = []
        for i in range(4):
            nota = float(input(f"Ingrese la nota {i+1}: "))
            notas.append(nota)
        
        promedio = sum(notas) / len(notas)
        
        alumno = {
            "Nombre": nombre,
            "Asignatura": asignatura,
            "Notas": notas,
            "Promedio": promedio
        }
        alumnos.append(alumno)
    
    return alumnos

def mostrar_alumnos(alumnos):
    for alumno in alumnos:
        print(alumno)         
        
# alumnos = cargar_alumnos()
# mostrar_alumnos(alumnos)  

# 4
"""
Realice un programa que pida datos de personas: nombre, día de nacimiento, mes de nacimiento, y año de nacimiento. 
Después deberá repetir lo siguiente: preguntar un 
número de mes y mostrar en pantalla los datos de las personas que cumplan los años durante ese mes. 
Terminará de repetirse cuando se teclee vacío en el nombre. 
"""

def cargar_personas_cumpleanos():
    personas = []
    nombre = input("Ingrese el nombre (deje vacío para terminar): ")

    while nombre:  # se repite mientras no esté vacío
        dia = int(input("Ingrese el día de nacimiento: "))
        mes = int(input("Ingrese el mes de nacimiento: "))
        anio = int(input("Ingrese el año de nacimiento: "))

        persona = {
            "Nombre": nombre,
            "Día": dia,
            "Mes": mes,
            "Año": anio
        }
        personas.append(persona)

        nombre = input("Ingrese el nombre (deje vacío para terminar): ")

    return personas

def mostrar_cumpleanos(personas):
    mes_consulta = input("Ingrese un número de mes para consultar (deje vacío para terminar): ")

    while mes_consulta:  # se repite mientras no esté vacío
        mes_consulta = int(mes_consulta)

        if 1 <= mes_consulta <= 12:
            cumpleaneros = [p for p in personas if p["Mes"] == mes_consulta]

            if cumpleaneros:
                print(f"\nPersonas que cumplen años en el mes {mes_consulta}:")
                for persona in cumpleaneros:
                    print(f"{persona['Nombre']} - {persona['Día']}/{persona['Mes']}/{persona['Año']}")
            else:
                print(f"\nNo hay personas que cumplan años en el mes {mes_consulta}.")
        else:
            print("El mes debe estar entre 1 y 12.")

        mes_consulta = input("\nIngrese un número de mes para consultar (deje vacío para terminar): ")


# personas = cargar_personas_cumpleanos()
# mostrar_cumpleanos(personas)

# 5
"""
Se debe gestionar los datos de stock de una tienda de comestibles, la información a recoger será: nombre del producto, precio, cantidad en stock. 
La tienda dispone de 10 productos distintos. El programa debe ser capaz de:
▪ Dar de alta un producto nuevo.
▪ Buscar un producto por su nombre.
▪ Modificar el stock y precio de un producto dado.
"""

def cargar_productos():
    productos = []
    for _ in range(2): # Pongo 2 para que sea mas corto pero deberia ir 10.
        nombre = input("Ingrese el nombre del producto: ")
        precio = float(input("Ingrese el precio del producto: "))
        cantidad = int(input("Ingrese la cantidad en stock: "))

        producto = {
            "Nombre": nombre,
            "Precio": precio,
            "Cantidad": cantidad
        }
        productos.append(producto)
    
    return productos

def buscar_producto(productos, nombre):
    for producto in productos:
        if producto["Nombre"].lower() == nombre.lower():
            return producto
    return None

def modificar_producto(productos, nombre):
    producto = buscar_producto(productos, nombre)
    if producto:
        nuevo_precio = float(input("Ingrese el nuevo precio del producto: "))
        nueva_cantidad = int(input("Ingrese la nueva cantidad en stock: "))
        producto["Precio"] = nuevo_precio
        producto["Cantidad"] = nueva_cantidad
        print("Producto modificado exitosamente.")
    else:
        print("Producto no encontrado.")
        
# productos = cargar_productos()
# print("Productos cargados:")
# for producto in productos:
#     print(producto)
# nombre_buscar = input("Ingrese el nombre del producto a buscar: ")
# producto_encontrado = buscar_producto(productos, nombre_buscar)
# if producto_encontrado:
#     print("Producto encontrado:", producto_encontrado)
# else:
#     print("Producto no encontrado.")
# nombre_modificar = input("Ingrese el nombre del producto a modificar: ")
# modificar_producto(productos, nombre_modificar)
# print("Productos actualizados:")
# for producto in productos:
#     print(producto)

# 8
"""
Sistema de calificaciones: Escribe un programa que permita a los profesores registrar las calificaciones de sus alumnos y 
les permita calcular la nota final. 
Crea un diccionario para cada alumno, con su legajo como clave y una lista de notas como valor. 
Luego, el programa debe permitir al usuario ingresar las notas para cada alumno y calcular su nota final, 
basándose en un sistema de pesos predeterminado.
"""

def cargar_calificaciones():
    alumnos = {}
    while True:
        legajo = input("Ingrese el legajo del alumno (ENTER para terminar): ")
        if not legajo:
            break

        notas = []
        notas.append(float(input("Ingrese nota del Parcial: ")))
        notas.append(float(input("Ingrese nota del Trabajo Práctico: ")))
        notas.append(float(input("Ingrese nota del Examen Final: ")))

        alumnos[legajo] = notas

    return alumnos


def calcular_notas_finales(alumnos, pesos):
    finales = {}
    for legajo, notas in alumnos.items():
        # Producto escalar entre notas y pesos
        nota_final = sum(n * p for n, p in zip(notas, pesos))
        finales[legajo] = round(nota_final, 2)
    return finales


# Definimos pesos: Parcial 40%, TP 30%, Final 30%
pesos = [0.4, 0.3, 0.3]

# alumnos = cargar_calificaciones()
# finales = calcular_notas_finales(alumnos, pesos)

#print("\nNotas finales:")
#for legajo, nota in finales.items():
#    print(f"Legajo {legajo}: {nota}")

# 9
"""
Supongamos que un coleccionista de figuras Funko Pop de Rick y Morty tiene un carrito
de compras con las siguientes figuras y sus respectivas cantidades:
carrito = {
 "Rick Sanchez" : 2,
 "Morty Smith" : 3,
 "Summer Smith" : 1,
 "Mr. Meeseeks" : 4
}
Y además, el coleccionista conoce los precios unitarios (en dólares) de estas figuras:
precios = {
 "Rick Sanchez" : 15,
 "Morty Smith" : 12,
 "Summer Smith" : 10,
 "Mr. Meeseeks" : 20
}

Cree una función llamada precioTotal que calculará el monto total de la compra en
función de estos datos. Cuando se llame a la función precioTotal(carrito, precios) con los
diccionarios proporcionados, se debe obtener el monto total de la compra basado en la
multiplicación de la cantidad de cada figura por su precio unitario en dólares.
"""

carrito = {
 "Rick Sanchez" : 2,
 "Morty Smith"  : 3,
 "Summer Smith" : 1,
 "Mr. Meeseeks" : 4
}

precios = {
 "Rick Sanchez" : 15,
 "Morty Smith"  : 12,
 "Summer Smith" : 10,
 "Mr. Meeseeks" : 20
}

def precioTotal(carrito, precios):
    total = 0
    for figura, cantidad in carrito.items():
        if figura in precios:
            total += cantidad * precios[figura]
            print(total)
    return total

# monto_total = precioTotal(carrito, precios)
# print(f"El monto total de la compra es: ${monto_total}")

# 11
"""
 Se tienen dos variables del tipo diccionario, en una de ella se almacena la información
de los artículos y la cantidad que tiene una persona en un carrito de compras:
carrito = {
"lapiceras" : 12,
"borrador" : 1,
"carpeta" : 2
}
En una segunda variable, se almacenan el stock (cantidad de artículos disponibles) de
cada uno de los artículos:
stock = {
"lapiceras" : 13,
"borrador" : 10,
"carpeta" : 3
}

Con relación a dicha información, se deberán elaborar las siguientes funciones:

• hayStock(articulo, cantidad, stock): Recibe un artículo y verifica si hay stock
disponible (retorna True en caso de que exista; False en caso contrario).
hayStock("borrador", 1, stock) => True
hayStock("borrador", 13, stock) => False

• procesarPedido(carrito, stock): Recibe los artículos solicitados en carrito y
realiza el descuento de stock correspondiente. Debe retornar como resultado
el stock actualizado. No afectar la variable recibida como parámetro. Utilizando
las variables anteriores como ejemplo, debería retornar:
{'lapiceras': 1, 'borrador': 9, 'carpeta': 1}
"""

carrito = {
    "lapiceras" : 12,
    "borrador" : 10,
    "carpeta" : 2
}

stock = {
    "lapiceras" : 13,
    "borrador" : 10,
    "carpeta" : 3
}

def hayStock(articulo, cantidad, stock):
    return stock.get(articulo, 0) >= cantidad

def procesarPedido(carrito, stock):
    stock_actualizado = stock.copy()  # Crear una copia del stock original
    for articulo, cantidad in carrito.items():
        if hayStock(articulo, cantidad, stock_actualizado):
            stock_actualizado[articulo] -= cantidad
        else:
            print(f"No hay suficiente stock para {articulo}.")
    return stock_actualizado

# print(hayStock("borrador", 1, stock))  # True
# print(hayStock("borrador", 13, stock)) # False
# stock_actualizado = procesarPedido(carrito, stock)
# print("Stock actualizado:", stock_actualizado)  # {'lapiceras': 1, 'borrador': 9, 'carpeta': 1}
# print("Stock original:", stock)  # Verificar que el stock original no se ha modificado

# 13
"""
En un sistema de recetas de cocinas, se tiene dos variables. En una de ellas, se
almacena en un conjunto la información de los ingredientes que tiene una persona en
su casa a disposición:
ingredientes = { "huevo", "aceite", "papas"}

En una segunda variable, se encuentran parametrizadas las recetas existentes
indicando que ingredientes se requieren para cada preparación:
recetas = {
 "Papas fritas" : { "aceite", "papas" },
 "Huevo frito" : { "huevo", "aceite" },
 "Pure de papas" : { "papas", "manteca" }
}
Conociendo dicha información, se deberán elaborar las siguientes funciones (que
deben incluir dentro de la misma operaciones de conjunto en su resolución):

• recetasPosibles (ingredientes, recetas), que retorne una lista con el nombre de
las recetas que son posibles de realizar con los ingredientes indicados.
Resultado esperado con los ejemplos dados:
['Papas fritas', 'Huevo frito']

• ingredientesFaltantes (ingredientes, recetas), que retorne un diccionario
donde, por cada receta existente, indique la lista de ingredientes faltantes para
realizar la receta. Si no falta ningún ingrediente, debería mostrarse la lista
vacía. Resultado esperado con los ejemplos dados:
{'Papas fritas': [], 'Huevo frito': [], 'Pure de papas': ['manteca']}
"""

ingredientes = { "huevo", "aceite", "papas"}

recetas = {
 "Papas fritas" : { "aceite", "papas" },
 "Huevo frito" : { "huevo", "aceite" },
 "Pure de papas" : { "papas", "manteca" }
}

def recetasPosibles(ingredientes, recetas):
    posibles = []
    for nombre, requiere in recetas.items():
        if requiere.issubset(ingredientes): # Si todos los ingredientes requeridos estan en los ingredientes disponibles
            posibles.append(nombre)
    return posibles

def ingredientesFaltantes(ingredientes, recetas):
    faltantes = {}
    for nombre, requiere in recetas.items():
        faltantes[nombre] = list(requiere - ingredientes) # Devuelve los ingredientes que están en requiere pero no en ingredientes. 
    return faltantes

print("Recetas posibles:", recetasPosibles(ingredientes, recetas))  # ['Papas fritas', 'Huevo frito']
print("Ingredientes faltantes:", ingredientesFaltantes(ingredientes, recetas))  # {'Papas fritas': [], 'Huevo frito': [], 'Pure de papas': ['manteca']}