import sys
sys.modules[__name__].__dict__.clear()

S = 'spam'
I = iter(S)

I.__next__() # es equivalente a
next(I)

# Nota: next(I) invoca al metodo __next__