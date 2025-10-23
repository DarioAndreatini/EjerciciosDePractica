def encontrarNombre():
    dd = 9 + 9 
    mm = 6 * 2
    aaaa = 2000 + 22
    
    nombreArchivo = str(dd) + str(mm) + str(aaaa) + '.txt'
    #print(nombreArchivo)

    try:
        archivo = open(nombreArchivo, 'r')

        lista = []
        for linea in archivo:
            lista.append(linea[0])

        nombreArchivo = ''.join(lista) + '.txt'
       # print(nombreArchivo)

        return nombreArchivo
    except Exception as e:
        print('Se produjo un error', e)
    finally: 
        archivo.close()


def encontrarSolucion(nombreArchivo,nombreArchivoFinal):
    try:
        archivo = open(nombreArchivo,'r')
        archivoFinal = open(nombreArchivoFinal,'a') 

        nombreBuscado = '' 
        for linea in archivo:
            nombreBuscado = linea
        
        solucion = nombreBuscado[::-1]
    #    print(solucion)

    #    archivoFinal.write(solucion + '\n')
        print(solucion,file = archivoFinal)
    except Exception as e:
        print('Se produjo un error', e)
    finally:
        archivo.close() 
        archivoFinal.close()



nombreArchivo =  encontrarNombre()
encontrarSolucion(nombreArchivo,'NombreEncontrado.txt')

