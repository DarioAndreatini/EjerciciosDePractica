# 1. Crea un programa que vaya leyendo las frases que el usuario teclea y las guarde en un fichero de texto llamado “frases.txt”. 
# Terminará cuando la frase introducida sea "fin" (esa frase no deberá guardarse en el fichero).

def guardarFrasesEnArchivo():
    with open("frases.txt", "a") as archivo:
        while True:
            frase = input("Introduce una frase (o 'fin' para terminar): ")
            if frase.lower() == "fin":
                break
            archivo.write(frase + "\n")
    print("Frases guardadas en 'frases.txt'.")

# guardarFrasesEnArchivo()

# 2. En base al primer punto, luego de generar la carga de las frases, visualizar el archivo cargado.

def visualizarArchivoFrases():
    try:
        with open("frases.txt", "r") as archivo:
            contenido = archivo.read()
            print("Contenido del archivo 'frases.txt':")
            print(contenido)
    except FileNotFoundError:
        print("El archivo 'frases.txt' no existe.")
        
# visualizarArchivoFrases()

# 3. Crear un archivo que se llame “montos.txt”, en el mismo se almacenarán valores numéricos. 
# Realizar un proceso que visualice su contenido y, al finalizar, muestre el total (sumatoria de los valores) y promedio.

def crearArchivoMontos():
    print("Creando archivo 'montos.txt' de prueba...")
    try:
        with open("montos.txt", "w") as archivo:
            archivo.write("150.50\n")
            archivo.write("300.00\n")
            archivo.write("50.25\n")
            archivo.write("100\n")
        print("Archivo 'montos.txt' creado con éxito.")
    except IOError as e:
        print(f"Error al crear el archivo: {e}")

def procesarMontosArchivo():
    try:
        with open("montos.txt", "r") as archivo:
            
            montos = archivo.read() # Lee todas las líneas del archivo
            lineas = montos.splitlines() # Divide el contenido en líneas
            total = 0.0
            cantidad = 0
            
            for linea in lineas:
                try:
                    monto = float(linea)
                    total += monto
                    cantidad += 1
                except ValueError:
                    print(f"Advertencia: La línea '{linea}' no es un número válido y será ignorada.")
                    
            if cantidad > 0:
                promedio = total / cantidad
                print(f"Total: {total}, Promedio: {promedio:.2f}")
            else:
                print("No se encontraron montos válidos en el archivo.")
            
    except FileNotFoundError:
        print("El archivo 'montos.txt' no existe.")
    
# crearArchivoMontos()
# procesarMontosArchivo()


# 4. Crear un programa que maneje un archivo donde se almacena la siguiente información de una determinada cantidad personas: 
# Nombre, Apellido, Edad y Estatura. El programa deberá almacenar la información a medida que se vayan cargando. 
# El formato a ser almacenado será cada dato separado por el carácter punto y coma (;) en el mismo orden que se carga. 
# Tenga en cuenta que cada vez que se ejecuta el programa, se debe incrementar el contenido del archivo (agregar al final).

def guardarPersonasEnArchivo():
    with open("personas.txt", "a") as archivo:
        
        bandera = True
        
        while bandera:
            nombre = input("Ingrese el nombre (o 'fin' para terminar): ")
            if nombre.lower() == "fin":
                bandera = False
                break
            apellido = input("Ingrese el apellido: ")
            edad = input("Ingrese la edad: ")
            estatura = input("Ingrese la estatura (en cm): ")
            
            archivo.write(f"{nombre};{apellido};{edad};{estatura}\n")
    print("Información guardada en 'personas.txt'.")
    
# guardarPersonasEnArchivo()

# 5. Crear un programa que permita recuperar la información del archivo generado y muestre los promedios de edad y estaturas. 
# Muestre todos los datos al procesar.

def promedioAlturaYEdad():
    try:
        with open("personas.txt", "r") as archivo:
            lineas = archivo.readlines()
            total_edad = 0
            total_estatura = 0
            cantidad = 0
            
            print("Datos de las personas:")
            for linea in lineas:
                nombre, apellido, edad, estatura = linea.strip().split(";")
                edad = int(edad)
                estatura = float(estatura)
                
                print(f"Nombre: {nombre}, Apellido: {apellido}, Edad: {edad}, Estatura: {estatura} cm")
                
                total_edad += edad
                total_estatura += estatura
                cantidad += 1
            
            if cantidad > 0:
                promedio_edad = total_edad / cantidad
                promedio_estatura = total_estatura / cantidad
                print(f"\nPromedio de Edad: {promedio_edad:.2f}")
                print(f"Promedio de Estatura: {promedio_estatura:.2f} cm")
            else:
                print("No hay datos para calcular promedios.")
    except FileNotFoundError:
        print("El archivo 'personas.txt' no existe.")
        
# promedioAlturaYEdad()

# 6. Genere un programa que pregunte un nombre de archivo (ubicación) y muestre en pantalla el contenido de ese archivo. 
# Informe en pantalla si no existe.

def mostrarContenidoArchivo():
    nombre_archivo = input("Ingrese el nombre del archivo (con su ruta si no está en el mismo directorio): ")
    try:
        with open(nombre_archivo, "r") as archivo:
            contenido = archivo.read()
            print(f"Contenido del archivo '{nombre_archivo}':")
            print(contenido)
    except FileNotFoundError:
        print(f"El archivo '{nombre_archivo}' no existe.")
        
# mostrarContenidoArchivo()

# 7.	Crear dos archivos:
# 	.: Paises.txt  Con el contenido de los países de Latinoamérica
# 	.: Provincias.txt  Con el contenido de las provincias de Argentina
# 
# Crear un programa que le pregunte al usuario si quiere ver los países o provincias, 
# de acuerdo a su selección, debe mostrar su contenido en pantalla (que elija 1 o 2 con el teclado).

def generarArchivoPaises():
    paises = ["Argentina", "Brasil", "Chile", "Colombia", "Ecuador", "Perú", "Uruguay", "Venezuela", "Paraguay", "Bolivia"]
    with open("Paises.txt", "w") as archivo:
        for pais in paises:
            archivo.write(pais + "\n")
            
def generarArchivoProvincias():
    provincias = ["Buenos Aires", "Córdoba", "Santa Fe", "Mendoza", "Tucumán", "Salta", "Entre Ríos", "Corrientes", "Chaco", "Formosa"]
    with open("Provincias.txt", "w") as archivo:
        for provincia in provincias:
            archivo.write(provincia + "\n")

def paisesOProvincias():
    opcion = input("Ingrese '1' para ver países de Latinoamérica o '2' para ver provincias de Argentina: ")
    
    if opcion == '1':
        archivo_nombre = "Paises.txt"
    elif opcion == '2':
        archivo_nombre = "Provincias.txt"
    else:
        print("Opción no válida.")
        return
    
    try:
        with open(archivo_nombre, "r") as archivo:
            contenido = archivo.read()
            print(f"Contenido del archivo '{archivo_nombre}':")
            print(contenido)
    except FileNotFoundError:
        print(f"El archivo '{archivo_nombre}' no existe.")
    
# generarArchivoPaises()
# generarArchivoProvincias()
# paisesOProvincias()

# 8. Escribe un programa que lea un archivo txt con información sobre ventas de una tienda 
# (los valores serán fecha, producto, precio, cantidad por cada fila; por ejemplo: 01/01/2023,Pantalones,50,10). 
# El programa debe calcular el total de ventas por día.

def generarArchivoVentas():
    ventas = [
        ["01/01/2023", "Pantalones", 50.0, 10],
        ["01/01/2023", "Camisas", 30.0, 5],
        ["02/01/2023", "Zapatos", 80.0, 2],
        ["02/01/2023", "Sombreros", 20.0, 7],
        ["03/01/2023", "Cinturones", 15.0, 12]
    ]
    
    with open("ventas.txt", "w") as archivo:

        for venta in ventas:
            ventaIndividual = ",".join([str(item) for item in venta])
            archivo.write(ventaIndividual + "\n")

def calcularVentasPorDia(nombre_archivo):
    ventas_por_dia = {}
    productos = []
    
    try:
        with open(nombre_archivo, "r") as archivo:
            for linea in archivo:
                fecha, producto, precio, cantidad = linea.strip().split(",")
                precio = float(precio)
                cantidad = int(cantidad)
                productos.append(producto)
                
                total_venta = precio * cantidad
                
                if fecha in ventas_por_dia:
                    ventas_por_dia[fecha] += total_venta
                else:
                    ventas_por_dia[fecha] = total_venta
                
        
        print("Total de ventas por día:")
        for fecha, total in ventas_por_dia.items():
            print(f"{fecha}: ${total:.2f}")
            
    except FileNotFoundError:
        print(f"El archivo '{nombre_archivo}' no existe.")
    
        
generarArchivoVentas()
calcularVentasPorDia("ventas.txt")
