# borrar todas las variables
import sys
sys.modules[__name__].__dict__.clear()

D = {'food': 'Spam', 'quantity': 4, 'color': 'pink'}

D['food']

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