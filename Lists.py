# Agregar un elemento
l = ['spam',1.23, 'NI']

l.append('aa')

# Borrar un elemento

l.pop(2)

# Ordenar listas(ordenar de reversa)

l= ['a','c','b']

l.sort()

l.reverse()

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