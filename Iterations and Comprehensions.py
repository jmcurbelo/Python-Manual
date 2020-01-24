import sys
sys.modules[__name__].__dict__.clear()

#######################################################################
# List Comprehesions
#######################################################################
res = list(map(ord, 'spam'))  #con map

res = [ord(x) for x in 'spam']  #list comprehesion

[x for x in range(5) if x%2==0] #list comprehesion con clausulas if

list(filter((lambda x: x%2==0), range(5))) #mismo resultado pero con funciones lambda

[x**2 for x in range(5) if x % 2 == 0] #combinación de map y filter con list comprehesion

list( map((lambda x: x**2), filter((lambda x: x % 2 == 0), range(5))) )  #equivalente con map y filter

"""
Estructura general de list comprehesions

[ expression for target1 in iterable1 [if condition1]
             for target2 in iterable2 [if condition2] ...
             for targetN in iterableN [if conditionN] ]
"""
[x + y for x in [0,1,2] for y in [100,200,300]] #ejemplo de fors anidados con list comprehesions

[(x, y) for x in range(5) if x % 2 == 0 for y in range(5) if y % 2 == 1] #list comprehesions con fors anidados y condiciones

################################################################
# List comprehesions and Matrixes
################################################################
M = [[1,2,3],
     [4,5,6],
     [7,8,9]]

N = [[2,2,2],
     [3,3,3],
     [4,4,4]]

[row[1] for row in M] #da la segunda columna

"""
>>> [line.rstrip() for line in open('myfile')]
['aaa', 'bbb', 'ccc']
>>> list(map((lambda line: line.rstrip()), open('myfile')))
['aaa', 'bbb', 'ccc']

estos ejemplos son utilizados para leer archivos y eliminar el salto de línea al final \n
"""

##############################################################
# Generators
##############################################################




[M[i][i] for i in range(len(M))] #da la diagonal


