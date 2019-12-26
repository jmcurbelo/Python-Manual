import sys
sys.modules[__name__].__dict__.clear()

T = (1,2,3,4)
T + (5,6)

T[1]

T.index(2) # En que posicion aparece el 2 en la tupla

T.count(3) # Cuantas veces aparece el 3 en la tupla

