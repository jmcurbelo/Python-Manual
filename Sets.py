import sys
sys.modules[__name__].__dict__.clear()

X = set('spam')
Y = {'h','a','m'}

X,Y

X & Y # Interseccion de conjuntos
X | Y # union
X-Y # diferencia

# Comprehension in Sets

{x**2 for x in range(1,5)}