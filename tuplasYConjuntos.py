# Conjuntos -> Conjuntos de elementos iterables mutables no ordenados. Se puede decir que es una lista que tiene valores unicos.

conjuntos = {1, 2, 3, 4}

conjunto2 = set({10,12,13,14})

conjuntoVacio = set()

print(conjuntoVacio)

conjuntoVacio.add(1)
conjuntoVacio.add(1)
conjuntoVacio.add(2)

print(conjuntoVacio)

listarConjunto = list(conjuntoVacio)

print(conjuntoVacio)

# Remove y discard, el remove si no lo encuentra rompe y el discard no

conjuntoVacio.discard(2)

print(conjuntoVacio)


conjuntoNumeros1 = {1, 2, 7, "Ruben"}
conjuntoNumeros2 = {1, 2, 3, 4}

# Se puede trabajar con Union, no modifica el original

nuevoConjunto = conjuntoNumeros1.union(conjuntoNumeros2)

print(nuevoConjunto)

# Se puede trabajar con Interseccion

nuevoConjunto2 = conjuntoNumeros1.intersection(conjuntoNumeros2)

print(nuevoConjunto2)

# Se puede trabajar con Diferencia

nuevoConjunto3 = conjuntoNumeros1.difference(conjuntoNumeros2)

print(nuevoConjunto3)


# Tuplas - es un tipo de estructura de datos que puedo contener N elementos dentro de uno mismo. Es ordenada. 
# No se puede modificar en tiempo de ejecuccion.
# Es buena practica poner parentesis

coor = (1, 2)
cumpleanios = (12, 6, 2001)




