import sys
sys.modules[__name__].__dict__.clear()

# Funcion para hallar el intersecto de dos secuencias

def intersect(seq1, seq2):
    res = []
    for x in seq1:
        if x in seq2:
            res.append(x)
    return res

s1 = 'jose'
s2 = 'winner'

intersect(s1, s2)

# Otra alternativa
[x for x in s1 if x in s2]

"""
Esta funcion es polimorfica porque admite otros tipos de objetos que pueden ser 
intersectados
"""
intersect([1,2,3],(1,4))

####################################
# Factory Functions
####################################

# Ejemplo 1
def maker(N):
    def action(X):  # Make and return action
        return X ** N  # action retains N from enclosing scope

    return action

f = maker(2)      # f lo que guarda es una función que retiene el parametro pasado para posteriores aciiones

f(3) # 3 al cuadrado por está reteniendo el dos con que fue creado

# Ejmeplo 2
# Otro ejemplo donde podemos referenciar a otra funcion
def f1():
    x = 88
    f2(x)

def f2(x):
    print(x)

f1()

# Ejemplo 3, realiza lo mismo que el ejemplo 1 pero con la función lambda

def func():
    x = 4
    action = lambda n: x**n  # recuerda a x del scope y estable una nueva función que recibe n
    return action

x = func()  # crea una función que devolverá 4 elevado al parámetro
print(x(2))

# Otra opción utilizando clases

class tester:
    def __init__(self, start):
        self.state = start
    def nested(self, label):
        print(label, self.state)
        self.state += 1

F = tester(0)      guarda el estado 0 con que se crea el objeto
F.nested('spam')   # hace un print pero a la vez incrementa el estado
F.nested('lolo')

G = tester(42)
G.nested('estado')
G.nested('estado mas uno')

# haciendo la clase que parezaca una función callable

class tester:
    def __init__(self, start):
        self.state = start
    def __call__(self, label):
        print(label, self.state)
        self.state += 1

H = tester(10)
H('primer estado calable como funcion')
H('se incrementa el estado')

#######################################################
# Argumentos de funciones
#######################################################
"""
Los argumentos pasado a una función son referencias aun objeto
Si pasamos como parámetro un objeto no mutable y asiganamos dentro de la funcion otro valor
a este parametro no cambiará en el scope global pero si por otra parte se pasa un objeto
mutable y dentro de la funcion se cambia este si cambiará en el scope global, una forma
de evitar estos cambios es pasar una copia del objeto mutable y no el objeto(referencia)
en sí
"""
def changer(L):
    L[0] = 'lolo'

L = [1,2,3]

changer(L) # si lo pasamos de esta manera cambiara la lista L en el scope global

L = [1,2,3]
changer(L[:]) # esta es una copia de la lista que no cambiará L en el scope global

###########################################
# Return option
###########################################
"""
return puede devolver tuplas u otro conjunto de objetos
"""

def multiples(x,y):
    x = 2
    y = [3,4]
    return x,y    # retorna una tupla

multiples(33, [33,44])

numero, tupla = multiples(22,[11,22]) # asiga los valores debido al desempaquetado de tuplas

################################################
# Argumentos (Parámetros)
################################################
def funcion(a, b = 2, c = 3):  # parámetros por defecto
    print(a,b,c)

funcion(1)

########################################################################################
# Colectando argumentos con *argumento1 y **argumento2 (en la contrucción de la función)
########################################################################################

def f(*a):
    print(a)

f() # Imprime tupla vacía
f(1)    #Imprime (1,)
f(1,2,3,4,5,'hola')  #imprime (1,2,3,4,5,'hola')

# Colectando llave/valor con nombre=valor
def f(**a):
    print(a)

f()  #Imprime un diccionario vacío
f(a=1, b=2)  #Imprime el diccionario {'a': 1, 'b': 2}

"""
el orden de los argumentos debe ser: argumento tradicional, *arg1, **arg2
"""

def f(a,*b, **c):
    print(a,b,c)

f(1, 2, 3, x=1, y=2)  # Imprime   1 (2, 3) {'x': 1, 'y': 2} porque a toma 1, b toma la tupla (2,3) y c toma el diccionario con key/value


###########################################################################################
# Desempaquetando argumentos con *argumento1 y **argumento2 (en el llamado de la función)
###########################################################################################

def f(a,b,c,d):
    print(a,b,c,d)

T = (3,6,9,3)
f(*T)    # desempaqueta los valores d ela tupla y los pasa como argumentos simples

D = {'a':1, 'b':33, 'c':77, 'd':100}

f(**D)  # desempaqueta el diccionario atendiendo a key/value

# Combinando ambos desempaquetados
f(*(1, 2), **{'d': 4, 'c': 4})

# Combinando desempaquetados y valores de parámetros normales
f(1, *(2, 3), **{'d': 4})

f(1, c=3, *(2,), **{'d': 4})

f(1, *(2, 3), d=4)

f(1, *(2,), c=3, **{'d':4})


##########################################################
# Argumentos pasados solo por referencia (keyword)
##########################################################
"""
Estos argumentos son aquellos que van despúes de los argumentos *argumento y solo pueden 
ser llamados por su nombre (keyword)
"""

def kwonly(a, *b, c): # c solo podrá ser llamado por su nombre
    print(a, b, c)

kwonly(1, (33,45,23,45), c = 'jose')

kwonly(1,2,3)  # esto dará error porque no se especifica C = 3

# otra forma de hacerlo sin empaquetar un argumentop es:

def kwonly(a, *, b, c):
    print(a,b,c)

kwonly(12, b = 'jose', c = 'duro') # b y c son referenciadas por keyword

kwonly(22, c = 'mama', b = 'mia') # igual no hay problema

kwonly(1, 2,3) #error b y c no son referenciados por el nombre keyword

# Argumentos por referencia tambien pueden ser establecido por default
def kwonly(a, *, b = 'jose', c = 'duro'):
    print(a,b,c)

kwonly(1) #funciona con b y c por defecto
kwonly(1, c = 'el mas lindo') #funciona c fue referenciado

"""
Los argumentos keywords only simpre deben ser pasados despues de *argumento pero no despúes
de **argumento, esto sería un error
"""