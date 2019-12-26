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