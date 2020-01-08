# Redireccionando los print de un script a un fichero

import sys
temp = sys.stdout    # Salvando la direccion por defecto para restaurarla luego
sys.stdout = open('salida.txt', 'a') # Redirrecionamos las salidas a un archivo salida.txt con append 'a'
print('spam')
print(1,2,3,4)
print('asi se redirecciona')

sys.stdout.close()   # cierra la conexion
sys.stdout = temp    # Restableciendo al valor por defecto

print('holaaaa')

# Enviando un solo print a un archivo
path = open('salida1.txt','a')

x = 'así se redirecciona una salida en Python a un fichero'
print(x, file=path)
print('así agremos más texto', file=path) # Agrega al mismo ficheo

path.close() # Importante cerrar sino no se escribe nada en el fichero .txt

print('jose')  #nada cambia despúes

