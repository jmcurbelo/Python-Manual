# Ejercicio 1:

def codigo(s):
    suma = 0
    lista = []
    for x in s:
        print(ord(x))
        suma += ord(x)
        lista.append(ord(x))
    print('La suma de los codigos es', suma)
    print('La lista de los codigos es', lista)


codigo('spam')
codigo('José')

# Ejercicio 2:

for i in range(50):
    print('hello %d\n\a' % i)

# Ejercicio 3:

def ord_diccionario(d):
    for key in sorted(d):
        print(key, '=>', d[key])

ord_diccionario({'c':3,'a':1,'b':2})

# Ejercicio 4:

# a
L = [1, 2, 4, 8, 16, 32, 64]
X = 5

i = 0
while i < len(L):
    if 2 ** X == L[i]:
        print('at index',i)
        break
    i += 1
else:
    print(X, 'not found')

# b

L = [1, 2, 4, 8, 16, 32, 64]
X = 5

for x in L:
    if 2**X == x:
        print('at index', L.index(x))
        break
else:
    print(X, 'not found')

# c

L = [1, 2, 4, 8, 16, 32, 64]
X = 5

if (2**X in L):
    print((2**X), 'está en el índice', L.index(2**X))
else:
    print(X,'no se encontó')

# d

L = [1, 2, 4, 8, 16, 32, 64]

potencias = []

for x in L:
    potencias.append(2**x)

print('Las potencias de dos de la lista son', potencias)