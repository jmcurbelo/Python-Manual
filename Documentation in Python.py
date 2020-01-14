import sys
sys.modules[__name__].__dict__.clear()

# The dir() function

dir(sys)

# Para ver los atributos de una lista o un string

dir([]) # el equivalente es dir(list)
dir('') # el equivalente es dir(str)

# Para crear la documentacion de un script, de una clase, una función, etc, escribimos
# al inicio de estas y luego llamamos como sigue

def cuadrado(x):
    """
    esta es una funcion que devuleve el cuadrado de un numero
    Parametros: recibe un unico parametro numerico

    """
    return x**2

print(cuadrado.__doc__)  # esto imprime la documentacion de lo que se halla creado

"""
cuando sea documentación de todo un script y se importe desde otro scritp se debe
hacer lo siguiente

import script

print(script.__doc__)

para ver la documentacion dentro de una funcion de ese script se hace como sigue

print(script.nomb_funcion.__doc__)

Lo mismo puede ser utilizado para ver la documentacion de un modulo y sus atributos

Ejemplo: print(sys.__doc__)
         print(sys.getrefcount.__doc__) 
         
Igual podemos obtener documentacion para un tipo de dato u función
Ejemplo: print(int.__doc__)
         print(map.__doc__)
         

"""
############################################
#  PyDoc: the help() function
############################################

import sys

help(sys)   # Esto brinda la ayuda necesaria

# se puede aplicar a un tipo de objeto o incluso a un método de un objeto

help(dict)
help(str.replace)

# igual que ejemplo anterior podemos acceder a la documentacion de un script y sus funciones
"""
 import script
 help(script.cuadrado)
"""

###########################################
# PvDoc: HTML Reports
###########################################

