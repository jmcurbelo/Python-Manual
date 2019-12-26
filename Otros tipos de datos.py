
import  sys
sys.modules[__name__].__dict__.clear()

1/3  # Floating-point

import decimal    # Decimals: fixed precision

d = decimal.Decimal('3.141')

d+1

decimal.getcontext().prec = 2   # Establece la precision en dos
decimal.Decimal('1.00')/decimal.Decimal('3.00')

# Fracciones
from fractions import Fraction

f = Fraction(2,3)
f+1



# Varias formas de verificar el tipo de un objeto
L = [1,2,23,4]
#1
if type(L) == type([]):
    print('yes')

#2
if type(L) == list:
    print('yes')

#3
if isinstance(L,list):
    print('yes')
