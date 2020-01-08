import sys
sys.modules[__name__].__dict__.clear()

spam = 'Spam'   # Asignacion comun

spam, ham = 'yum','YUM'

[spam, ham] = ['yum','YUM']

a,b,c,d = 'spam'    # Asignación sequencial a=s, b=p ....

a, *b = 'spam'   # extended sequence unpacking a='s', b=['p','a','m']

W = S = 'spam'

spam = 0
spam += 42   # equivalente a spam = spam + 42

[a,b,c] = (1,2,3)  # Asigna los numeros

(a,b,c) = 'ABC' # Asigna cada letra a la mayuscula

red, blue, green = range(3)



seq = [1,2,3,4,5]

a, *b = seq  # primera forma

*a, b = seq  # Segunda forma

a, *b, c = seq  # Tercera forma

# Ejemlo
L = [1,2,3,4]
while L:
    a, L = L[0], L[1:]
    print(a, L)

# Ejemplo simplificado
L = [1,2,3,4]
while L:
    a, *L = L
    print(a, L)

# Nota: *a simpre asignara una lista, sino hay nada que apilar asignará una lista vacía
# y no se puede utilizar más de un apilamiento en la mismsa asignación

L = [1,2,3]
a, b, c, *d = L

##############################################
# augmented assignment (asignación aumentada)
##############################################
x = 1

x = x +1 # más lento

x += 1  # augmented assignmaent (más rapido)


L = [1,2,3,4]

L = L + [5,6] # asignacion mas lento concatenacion (devuelve una nueva lista)

L += [8,9]  # más rapido concatenacion (similar a L.extend([8,9])) (hace cambion in-place)



