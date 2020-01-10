import sys
sys.modules[__name__].__dict__.clear()

# Agregar un elemento
l = ['spam',1.23, 'NI']

l.append('aa')

l.extend([2,6,89])

# Borrar un elemento

l.pop(2)

# Ordenar listas(ordenar de reversa)

l= ['a','c','b']

l.sort()

l.reverse()

L = ['abc','ABD','aBe']
L.sort()                          # Ordena por la mayuscaula primero

L = ['abc','ABD','aBe']
L.sort(key=str.lower)              # ordena por la miniscula primero

L.sort(key=str.lower, reverse=True)

L = ['eggs','spam','ham']

L.index('eggs')                   # Da el indice dende esta el elemento

L.insert(1, 'uva')                   # Inserta en la posicion sin borrar el existente, hace un desplazamient

L.remove('uva')            # Borrar por valor

L.pop(1)                  # Borrar por posicion

L = ['hola','mundo','python','pelota']

del L[0]                  # Borrar la primera posicion

del L[1:]               # Borrar tdo a partir de la posicion seleccionada

L = ['hola','mundo','python','pelota']

L[0:3] = []        # Borra tambien porque primero borra la seleccion y luego asigna una lista vacía




# Nesting
m = [[1,2,3],
     [4,5,6],
     [7,8,9]]
################################################################################
# List comprehensions (Giveme row[1] for each row in matrix M, in a new list)
################################################################################
col2 = [row[1] for row in m]

[row[1]+1 for row in m]   # Add 1 to each item in column 2

[row[1] for row in m if row[1] % 2 ==0]  # Filter out odd items

diag = [m[i][i] for i in [0,1,2]]  # Collect a diagonal from matrix

doubles = [c*2 for c in 'spam']  # Repeat characters in a string

# Supongamos que queremos leer un archivo de texto y luego ponerlo en una lista donde
# cada posicion es una linea de texto, lo podemos hacer como sigue

lines = [line.rstrip() for line in open('file.txt')] #rstrip() elimina los espacios en blanco al final de la linea
lines = [line.rstrip().upper() for line in open('text.txt')]

# Filtrando con list comprehesion
#Siguiendo el ejemplo anterior imaginemos que queremos solo las líneas que comiencen con p

line = [line.rstrip() for line in open('text.txt') if line[0] == 'p']

# Otro ejemplo de list comprehesion con dos for loop

[x + y for x in 'abc' for y in 'lmn']

# comprehension syntax in
# parentheses can also be used to create generators that produce results on demand (the
# sum built-in, for instance, sums items in a sequence):

G = (sum(row) for row in m)  # crea un generador

next(G) # Corre el generador sobre la primera fila
next(G) # Corre el generador sobre la segunda fila etc....

list(map(sum,m))  # Map sum over items in M

{sum(row) for row in m}  # Create a set of row sums

{i : sum(m[i]) for i in range(3)}  # Creates key/value table of row sums

# lists, sets, and dictionaries can all be built with comprehensions
[ord(x) for x in 'spaam']  # List of character ordinals

{ord(x) for x in 'spaam'}  # Sets remove duplicates

{a : ord(a) for a in 'spaam'}

3 in [1,2,3,4] # inclusion

for x in [1,2,3]:             # Iteración
     print(x, end=' ')


# Map function
list(map(abs, [-1,-2,0,1,2,3]))

