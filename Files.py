import sys
sys.modules[__name__].__dict__.clear()

f = open('data.txt','w') # Crea el fichero
f.write('hello\n') # Escribe en el fichero
f.close() # Cierra el fichero

f = open('data.txt')
text = f.read()
text # esto devuelve el texto con el salto de linea
print(text) # Esto interpreta el salto de línea y no muestra el salto de linea

f = open('data.txt','w')
f.write('Hello\n')
f.write('world\n')
f.close()

f = open('data.txt')
text = f.read()

print(text)

text.split()  # divide el texto en palabras

dir(f) # nos da las funciones que se pueden aplicar a este objeto

# Si queremos ayuda de alguno
help(f.seek)

for line in open('data.txt'):
    print(line, end='')


# Convirtiendo objetos a texto para ser guardado en un fichero

X, Y, Z = 43, 44, 45             # Native Python objects
S = 'Spam'                       # Must be strings to store in file
D = {'a': 1, 'b': 2}
L = [1, 2, 3]

f = open('datafile.txt','w')
f.write(S+'\n')
f.write('%s,%s,%s\n' % (X,Y,Z))
f.write(str(L)+'$'+str(D)+'\n')
f.close()

F = open('datafile.txt','r')
F.readline()
F.close()

############################################
# Guardar objetos en disco
############################################
D = {'a':1, 'b':2}
F = open('datafile.pkl', 'wb')

import pickle
pickle.dump(D,F)

F.close()

# Para leerlos
F = open('datafile.pkl','rb')
E = pickle.load(F)

F.close()