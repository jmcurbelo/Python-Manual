import sys
sys.modules[__name__].__dict__.clear()

# Funcion para hallar el intersecto de dos secuencias

def intersect(seq1, seq2):
    res = []
    for x in seq1:
        if x in seq2:
            res.append(x)
    return res

s1 = 'jose'
s2 = 'winner'

intersect(s1, s2)

# Otra alternativa
[x for x in s1 if x in s2]

"""
Esta funcion es polimorfica porque admite otros tipos de objetos que pueden ser 
intersectados
"""
intersect([1,2,3],(1,4))

####################################
# Scope in Python
####################################
