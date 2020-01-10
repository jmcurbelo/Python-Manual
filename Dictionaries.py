# borrar todas las variables
import sys
sys.modules[__name__].__dict__.clear()

# Formas de crear un diccionario
#1
{1:'1',2:'yyyy'}

#2
D = {}
D['llave1'] = 23

#3
dict(name='Jose', age= 28)  # Requiere que todas las lllaves sean strings

#4
dict([('naAME','jose'),('last name','moya')])

#5 Creando un diccionario con diferentes llaves pero mismos valores
dict.fromkeys(['a','b'], 0)  # llaves a, b valor cero


D = {'food': 'Spam', 'quantity': 4, 'color': 'pink'}

D['food']        # Agregar un valor

D['color'] = 'ROSA'

del D['color']    # borrar por llave

list(D.values())   # Devulve los valores de las llaves

list(D.items())    # Devuelve las llaves:valor

# verificar que existe no una llave para asi agregarla
D.get('color'), D.get('colores')    # devulve None si la llave no existe

D1 = {'1':'rosa', '2':'verde', '3':'azul'}
D2 = {'5':'negro', '6':'violeta'}

D1.update(D2)   # Merge(une) el diccionario dos al diccionario 1

D1.pop('3')  # Borra por valor de la llave


D['quantity'] += 1  # Add 1 to 'quantity' value

# creando un diccionario vacío
D = {}

# Agregando elementos
D['name'] = 'Bob'
D['job'] = 'dev'
D['age'] = 40

# Nesting Revisited (Anidamiento Revisado)

rec = {'name':{'firts':'Bob', 'last':'Smith'},
       'job':['dev','mgr'],
       'age':40.5}

rec['name']
rec['name']['last']
rec['job'][-1]

rec['job'].append('janitor')  # Expand Bob's job description in-place

rec = 0

#####################################################################
# Sorting Keys: for Loops
#####################################################################

D = {'a':1, 'b':2, 'c':3}

Ks = list(D.keys())

Ks.sort()

for key in Ks:
       print(key, '=>',D[key])
# otra forma

D = {'a':1, 'c':3, 'b':2}

for key in sorted(D):
       print(key,'=>',D[key])


# Recorriendo un diccionario con un for loop

table = {'Python': 'Guido van Rossum',
         'Perl': 'Larry Wall',
         'Tcl': 'John Ousterhout'}

for lang in table:
       print(lang, '\t', table[lang])

D = {1:'rosa',
     2:'verde',
     3:'azul',
     4:'marron',
     5:'violeta'}

for key in D:
       print(key, '\t', D[key])

# Los diccionarios admiten como llaves culquier objeto inmutable. Ej enteros, string y
# hasta tuplas
# Ejemplo de matriz multidimensional

Matriz = {}
Matriz[(2,3,4)] = 88
Matriz[(7,8,9)] = 99

Matriz[(2,3,7)]  # error de llave perdida, no existe

# Para matrices multidimesionales sparse (sparciadas) podemos utilizar las isguientes
# sentencias para evitar el error de lave perdida

if (2,3,7) in Matriz:
       print(Matriz[(2,3,7)])
else:
       print(0)

# Otra forma
try:
       print(Matriz[(2,3,7)])
except KeyError:
       print(0)

# otra forma más (la más concisa en términos de requerimiento de código)
Matriz.get((2,3,4), 0)   # Obten en valor de la llave (2,3,4) sino devuelve cero
Matriz.get((2,3,6), 0)



###########################################
# Iteration and Optimization
###########################################

squares = [x**2 for x in range(1,6)] # Es mucho más eficiente que utilizar un for

squares = []

for x in range(1,6):
       squares.append(x**2)

# verificar si falta una llave en el diccionario

if not 'f' in D:
       print('Missing')

# Evitar errores a la hora de chequear una indexacion

value = D.get('x',0) # el valor del key 'x' sino devuelve cero

# Otra forma
value = D['x'] if 'x' in D else 0

#########################################################################
# Dictionary comprehensions
#########################################################################
list(zip(['a', 'b', 'c'], [1, 2, 3])) # Zip together keys and values

D = dict(zip(['a', 'b', 'c'], [1, 2, 3])) # Make a dict from zip result

D = {k: v for (k, v) in zip(['a', 'b', 'c'], [1, 2, 3])}

# Parecido a inizializar el diccionario con un mismo valor dict.fromkeys()

D = {k : 0 for k in ['a','b','c','d']}

# otra forma de inicializarlo con valores None
 D = dict.fromkeys('spam') # llaves s,p,a,m valores None

# Similar
 D = {k : None for k in 'spam'}


# creando diccionarios con la funcion zip y for loops

keys = ['a','b','c','d']
values = [1,2,3,4]

D ={}                                # Creando un diccionario vacío
for (k,v) in zip(keys, values):
    D[k] = v

# omitiendo el for loop se puede hacer con:

D1 = dict(zip(keys,values))

# Si queremos iterar sobre un objeto pero a la vez guardar un índice entero podríamos hacer los siguiente

c = 0
for item in 'spam':
    print(item, 'es la pos', c)
    c += 1

# En Python 3.0 podemos hacer lo siguiente

S = 'spam'

for (c, item) in enumerate(S):
    print(item, 'es la pos', c)

# Nota: enumerate() devuelve un tupla (index, value)  por eso se puede utilizar aquí