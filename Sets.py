import sys
sys.modules[__name__].__dict__.clear()

X = set('spam')
Y = {'h','a','m'}

X,Y

X & Y # Interseccion de conjuntos
X | Y # union
X-Y # diferencia

X > Y, X < Y # Superset, subset

X.add('JOSE')

X.remove('m')

for item in set('abc'):
    print(item*3)

# Inicialaizar un conjunto vacío

S = set()

S.add('Jose')

# Nota
# Los conjuntos solo pueden tener objetos inmutables dentro, por ello ni las listas,
# ni los diccionarios pueden estar dentro de los conjuntos pero si las tuplas

############################################
# Comprehension in Sets
############################################

{x**2 for x in range(1,5)}

{x for x in 'spam'}

L = [1,2,1,3,2,4,5]

L = list(set(L))  # Remover duplicados

# operaciones mas realistas

engineers = {'bob', 'sue', 'ann', 'vic'}
managers = {'tom', 'sue'}

'bob' in engineers

engineers & managers