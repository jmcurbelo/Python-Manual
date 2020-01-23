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

# Ejmeplo de funcion minmax

def minmax(test, *args):
    res = args[0]
    for arg in args[1:]:
        if test(arg, res):
            res = arg
    return res

def lessthan(x,y): return x<y
def greatherthan(x,y): return x>y

print(minmax(lessthan, 7,8,3,44,21,1,34))

# Ejemplo: Interseccion de los elementos de un numero desconocido de elementos

def interseccion(*args):
    res = []
    for x in args[0]:
        for arg in args[1:]:
            if x not in arg:
                break
        else:
                res.append(x)
    return res

print(interseccion('jose','sabino','idalmis'))

"""
Ejemplo para emular la función print() de Python 3.0 mediante una función
"""
import sys

def print30(*args, **kargs):
    sep = kargs.get('sep', ' ')  # Keyword arg defaults
    end = kargs.get('end', '\n')
    file = kargs.get('file', sys.stdout)
    output = ''
    first = True
    for arg in args:
        output += ('' if first else sep) + str(arg)
        first = False
    file.write(output + end)

print30(1,2,4)
print30('jose','the','best', sep='-->')

"""
En Python 3.X podríamos reescribir esta función emplendo la característica key/value only
"""

def print30(*args, sep=' ', end='\n', file=sys.stdout):
    output = ''
    first = True
    for arg in args:
        output += ('' if first else sep) + str(arg)
        first = False
    file.write(output + end)

############################################################################
# Advanced Functions Topic
############################################################################
 # Recursion

def mysum(L):
    print(L)
    if not L:
        return 0
    else:
        return L[0] + mysum(L[1:])

mysum([3,3,8,6])

# Otras alternativas
def mysum(L):                                    # Use ternary expression
    return 0 if not L else L[0] + mysum(L[1:])

def mysum(L):                                    # Any type, assume one
    return L[0] if len(L) == 1 else L[0] + L[1:]

def mysum(L):
    first, *rest = L
    return first if not rest else first + mysum(rest)  # Use 3.0 ext seq assign


# Otro ejemplo con while más concreto

L = [2,6,2,14,8]
sum = 0
while L:
    sum += L[0]
    L = L[1:]

print(sum)

# Better yet

L = [23,7,10,10]
sum = 0
for x in L:
    sum += x
print(sum)

"""
Usando recursion para calcular la suma de los elementos de una lista anidada con n niveles
donde ni while ni for funcionan
"""
def sumtree(L):
    tot = 0
    for x in L:                           # For each item at this level
        if not isinstance(x, list):
            tot += x                      # Add numbers directly
        else:
            tot += sumtree(x)             # Recur for sublists

    return tot

L = [1, [2, [3, 4], 5], 6, [7, 8]]

print(sumtree(L))

##################################################################
# Anotaciones en funciones
#################################################################
"""
Para realizar anotaciones en una función se puede hacer sobre los parámetros y sobre el
return de la función. La forma de hacerlo para los parámetros es poner la anotación
detras del nombre del parámetro seguido por dos punto y para el return luego de cerrar el paréntesis
y antes de los dos punto se indica con una flecha ->
Las anotaciones son devueltas como un diccionario
"""
def func(a:'anotacion_1', b:'rango de 1 a 10', c:float) -> int:
    return a+b+c
print(func(2,5,7))

# Para ver las anotaciones
func.__annotations__

# Anotaciones con argumentos por default
def func(a:'anotacion1'=3, b:int=5) -> int:
    return a+b

print(func())
func.__annotations__


#####################################################################
# Function lambda
####################################################################
"""
Sintaxis:
lambda argument1, argument2,... argumentN :expression using arguments
"""
f = lambda a,b,c: a+b+c
f(1,2,3)

"""
los argumentos en las funciones lambda trabajan igual que en las funciones definidas con
def
"""
f = (lambda a = 'jose', b='el mas', c = 'duro': a+b+c)
f()
f('lolo','el mas','flojo')

# Ejemplo

 L = [lambda x: x**2,
      lambda x: x**3,
      lambda x: x**4]
for f in L:
    print(f(2))

# Forma de implementar if/else dentro de lambda

lower = lambda x,y: x if x<y else y

lower('jose','alberto')

# Emplear loops en funciones lambda
import sys
showall = lambda x: list(map(sys.stdout.write, x))

showall(['lolo\n', 'polo\n', 'pepe\n'])

# Otra forma
showall = lambda x: [sys.stdout.write(line) for line in x]

showall(('lolo\n', 'juan\n', 'jacinto\n'))

# lambdas dentro de funciones def
def action(x):
    return(lambda y: x+y)
suma = action(99)
suma(10)  #Suma 10 al 99 con que se creo

# lambdas dentro de lambdas (evitar cuando sea posible)
action = (lambda x: (lambda y: x+y))
suma = action(19)
suma(1)


# Utilidad de lambda en tkinter para crear aplicaciones
import sys
from tkinter import Button, mainloop # Tkinter in 2.6
x = Button(
    text = 'Press me',
    command = (lambda: sys.stdout.write('Hello\n')))

x.pack()
mainloop()

####################################################################################
# La función Map()
####################################################################################
def incremento(x):
    return x + 10
print(list(map(incremento,[1,2,3])))

# Map con lambdas
print(list(map(lambda x: x + 100, [1,2,3])))

"""
Cuando map toma varios argumentos (listas) como entradas este mapea cada elemento de las listas
como un parámetro diferente, ejemplo:
"""
pow(3, 4)    # Tres elevado a la cuatro

print(list(map(pow, [1,2,3], [2,3,4]))) # devuelve 1 al cuadrado, 2 a la 3 y 3 a la 4

##########################################################################
# Funciones filter y reduce
##########################################################################
print(list(filter((lambda x: x>0), range(-5,5)))) # Filtra los valores mayores que cero

from functools import reduce

print(reduce((lambda x,y: x + y), [1,2,3,4])) # Retorma la suma de los elementos de la lista

# El equivalente con una funcion sería
def myreduce(function, sequence):
    tally = sequence[0]
    for next in sequence[1:]:
        tally = function(tally, next)
    return tally

print(myreduce((lambda x, y: x + y), [1, 2, 3, 4, 5]))
