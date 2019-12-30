import sys
sys.modules[__name__].__dict__.clear()

type(True) # bool
isinstance(True, int)  # True porque el bool es una subclase de los enteros son 1 y 0

True == 1 # True
True is 1  # Falso no son los mismo tipos de objetos

