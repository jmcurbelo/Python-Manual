import sys
sys.modules[__name__].__dict__.clear()

# creando una Tupla de un elemento
X =  (40,)

T = (1,2,3,4)

# Otra forma de crear la Tupla cuando no existe ambiguedad
T = 2,5,7

T + (5,6)

T[1]

T = (1,2,3,4,2)

T.index(2) # En que posicion aparece el 2 en la tupla

T.index(2,2) # devuelve 4 la posicion donde aparece el 2 por segunda vez

T.count(3) # Cuantas veces aparece el 3 en la tupla

# Ordenar una Tupla
T = ('cc','dd','aa','bb')

temp = list(T)
temp.sort()

T = tuple(temp)

# Nota: la inmutablidad de las tuplas funciona a un alto nivel, si por ejemplo tenemos
# una lista dentro de una Tupla esta si puede ser cambiada

T = (2,['spam',3,5],'huevo')

T[0] = 'carne'   # da error

T[1][1] = 'carne'  # asigna carne a la pos 1 de la lista