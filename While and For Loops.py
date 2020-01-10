import sys
sys.modules[__name__].__dict__.clear()

###############################################################
# While loops
###############################################################

#while <test>: # Loop test
#  <statements1> # Loop body
#else: # Optional else
#  <statements2> # Run if didn't exit loop with break(sino se salio del while con un break)

#####
# break, continue, pass, and Loop else block
#####

# break
######Jumps out of the closest enclosing loop (past the entire loop statement)
# continue
######Jumps to the top of the closest enclosing loop (to the loop’s header line)
#pass
######Does nothing at all: it’s an empty statement placeholder
#Loop else block
######Runs if and only if the loop is exited normally (i.e., without hitting a break)

while <test1>:
<statements1>
if <test2>: break # Exit loop now, skip else
if <test3>: continue # Go to top of loop now, to test1
else:
<statements2> # Run if we didn't hit a 'break'


#########################################################################
# for Loops
#########################################################################

for <target> in <object>: # Assign object items to target
   <statements>
   if <test>: break  # Exit loop now, skip else
   if <test>: continue  # Go to top of loop now
else:
   <statements> # If we didn't hit a 'break'

# Nota: for Loops trabaja en cualquier objeto iterable, ya sea, strings, listas tuplas, etc

# Ejemplo en tuplas

T = [(1,2),(3,4),(5,6)]

for (a,b) in T:
    print(a,b)

# Ejemplo en diccionarios

D = {'a':1, 'b':2, 'c':3}

for key in D:
    print(key, '=>', D[key])

list(D.items())  # devuelve un lista con tuplas con llave:valor del diccionario

for (key, value) in D.items():  # Mismo resultado que el anterior forma diferente
    print(key, '=>', value)

# Podemos hacer el unpack manualmente solo utilizando una variable para iterar la lista
# de tuplas como sigue

T = [(1,2),(3,4),(5,6)]

for i in T:
    a,b = i     # Unpack manual
    print(a,'=>', b)

# Otras secuencias anidadas tambien funcionan

for ((a, b), c) in [((1, 2), 3), ((4, 5), 6)]: print(a, b, c)

# Otro ejemplo con otra estructura

for ((a, b), c) in [([1, 2], 3), ['XY', 6]]: print(a, b, c)

# Recordando la asignacion por lotes o paquetes (starred name)
a, *b, c = (1,2,3,4) # a=1, b=[2,3], c = 4

# Se aplica tambien para un for loop

for (a, *b, c) in [(1, 2, 3, 4), (5, 6, 7, 8)]:
    print(a,b,c)

# Ejemplo de fors anidados

items = ["aaa", 111, (4, 5), 2.01] # A set of objects
tests = [(4, 5), 3.14]             # Keys to search

for key in tests:
    for item in items:
        if key == item:
            print(key, 'fue encontrada como llave')
            break
    else:
        print(key, 'no fue encontrada como una llave')

# Forma más sencilla con con el operador in que verifica si un objeto está dentro de otro

for key in tests:
    if key in items:
        print(key, 'fue encontrada como una llave')
    else:
        print(key, 'no fue encontrada como una llave')

# Otro ejemplo utilizando for loops y el operador in

lista1 = 'locas'
lista2 = 'aomes'

inteseccion = []
for i in lista1:
    if i in lista2:
        inteseccion.append(i)

print(inteseccion)

# Nota: la función range() puede ser utilizada para obtener indices especiales si se desea,
# pero no se debe utilizar a menos que sea necesario, ejemplo

L = [1,'a',2,'b',3,'c',4,'d']

for i in range(0,len(L),2):  #Recorre solo las posiciones de dos en dos
    print(L[i], end=' ')

for i in L[::2]:            # Recordar que L[::2] recorre la lista de principio a fin de dos en dos
    print(i, end=' ')

# En el siguiente caso la vía dos es la preferida sobre la vía uno

#Via 1
S = 'spam'

for i in range(len(S)):
    print(S[i], end=' ')

# Via 2

for i in S:
    print(i, end=' ')

# Cambiando los elemento de una lista la via 1 no funciona solo la via 2

#via 1

L = [1,2,3,4,5]

for item in L:  # Aquí los elementos de la lista no cambian e item guarda 6 al final
    item +=1

#via2

for i in range(len(L)): # esta alternativa si agrega 1 a cada elemento de la lista
    L[i] += 1

######################
# The Zip function
######################

L1 = [1,2,3,4]
L2 = [5,6,7,8]

zip(L1, L2)  # devuelve una tupla con los elementos pareados
list(zip(L1, L2))  # Para verlos como una lista [(1, 5), (2, 6), (3, 7), (4, 8)]

# Utilizando zip en for loops

for (x,y) in zip(L1, L2):
    print(x, y, '--', x+y)

#######