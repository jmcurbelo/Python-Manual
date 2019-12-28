import math

math.pi

math.e

math.sin(0)

math.sqrt(144)

pow(2,5)

abs(-35)

sum([1,3,6])

min((2,7,0))

max([1,4,12,4])

# Redondeo al siguiente entero más pequeño
math.floor(2.567), math.floor(-2.567)

# Truncar
math.trunc(2.567), math.trunc(-2.567)

# Truncar con una conversion a enteros
int(2.567), int(-2.567)

# Redondeo
round(2.567), round(2.467), round(2.567, 2)

# Redondeo para mostrar resultados retorna strings
'%.1f' % 2.567, '{0:.2f}'.format(2.567)


##########################################################
# El modulo random
##########################################################
import random

random.random()  # Devuelve un numero aleatorio entre 0 y 1
random.randint(1,10)  # Devuelve un numero entero aleatorio entre 1 y 10
random.choice(['Life of Brian', 'Holy Grail', 'Meaning of Life']) # selecciona un elemento aleatorio de la lista

# Numeros decimales
0.1+0.1+0.1-0.3    # debería ser cero pero no lo imprime como tal
print(0.1+0.1+0.1-0.3)   # tampoco esta expresion

from decimal import Decimal
Decimal('0.1')+Decimal('0.1')+Decimal('0.1')-Decimal('0.3') # Esto si produce el cero

# La funcion recibe un string como decimal con el numero de digitos deseados como decimales
# si existen decimales de diferentes tamaños convertirá los de menor tamaño a un
# tamaño similar al mayor

Decimal('0.1') + Decimal('0.10') + Decimal('0.10') - Decimal('0.30')

# Otra posiblidad es convertir a decimal un float con

Decimal.from_float(1.25)


##########################################################
# Estbleciendo los decimales deseados en el script completo
##########################################################
import decimal
decimal.getcontext().prec = 4

decimal.Decimal(1) / decimal.Decimal(7)   # Redondeará los resultados a 4 digitos


##########################################################
# Estbleciendo los decimales deseados en un contexto with
##########################################################
import decimal

with decimal.localcontext() as ctx:
    ctx.prec = 2
    print(decimal.Decimal('1.00')/decimal.Decimal('3.00'))


########################################
# Fracciones
########################################
from fractions import Fraction

x = Fraction(1,3)
y = Fraction(4,6)

print(x)  #  imprime la fraccion tal cual

x+y    # Suma de fracciones puden realizarse otras operaciones
x-y
x*y

# Obtener la fraccion de un decimal
Fraction('0.4'), Fraction('1.25')

Fraction('0.25')+Fraction('1.25')  # devuelve la suma pero en fraccion

# Usar un float en ocasiones pierde precision por el hadware de la pc, por lo tanto
# para obtener mayor exactitud a veces es preferible usar Decimales o Fracciones para
# no perder precision pero a costa de rapidez, ejemplo

0.1+0.1+0.1-0.3 # No es cero exactamente

from fractions import Fraction

Fraction(1,10)+Fraction(1,10)+Fraction(1,10)-Fraction(3,10) # es cero

from decimal import Decimal

Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3')  # es cero

# Fraction(a,b) automaticamente simplifica la fraccion