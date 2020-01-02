# the string find method is the basic substring search operation (it returns
# the offset of the passed-in substring, or −1 if it is not present)

s = 'Spam'

s.find('pa')
s.replace('pa','XYZ')

line = 'aa,bb,cc,ddddddd'

line.split(',')

s.upper()

line = 'aa,bb,cccc,dd\n'
line = line.rstrip() # Remove whitespace characters on the right side

'%s, eggs, and %s' % ('spam', 'SPAM!') # sustituye donde aparezca %s lo que hay en la tupla

# Para saber los metodos disponibles para un objeto utilizamos lo siguiente

s = 'Spam'

dir(s)

# The dir function simply gives the methods’ names. To ask what they do, you can pass
# them to the help function:

help(s.replace)

# Pattern Matching
# we import a module called re. This module has analogous calls for searching, splitting,
# and replacement, but because
# we can use patterns to specify substrings, we can be much more general:

############
# Texto Raw
############

# Si queremos que Python interprete el texto en bruto (raw) debemos anteponer una r

path = r'E:\SALVAS' # Si imprimes la variable o muestra con doble \\ pero si lo imprimes
# con un print muestra un solo \

# Nota: Incluso un string raw no puede acabar en backslash

#################################
# Triple comillas (block string)
#################################

texto = '''Hoy en día es muy difícil
hacer algo con los trabajos.
El punto es que, no hay trabajo
'''
# Se interpretan los saltos de línea con \n

texto #interprta los saltos con \n
print(texto)  # lo imprime tal cual lo tecleamos


ord('q') # Devuelve el codigo ASCII de la letra
chr(113) # Devuelve la letra de este codigo ASCII

#####################
# Format expresions
#####################
'Eso es %d %s pintada' % (1,'casa')  # %d digit, %s string
'eso es {0} {1} pintada'.format(1,'casa')  # mismo efecto

excamation = 'Ni'
'The knigths who say %s!' % excamation

# Nota: Para ver el formato %s, %d vea tabla 7-4 pag 181 pdf

#################################################
# Dictionary-Based String Formatting Expressions
#################################################

"%(n)d %(x)s" % {"n":1, "x":"spam"} # Sustituye el valor de n como digito y el valor de x como string

reply = """ # Template with substitution targets
Greetings...
Hello %(name)s!
Your age squared is %(age)s
"""

values = {'name': 'Bob', 'age': 40}
print(reply % values)

food = 'spam'
age = 30
vars() # recoge las variables del enviroment

'%(age)d %(food)s' % vars()

#####################################
# String Formatting Method Calls
#####################################
template = '{0}, {1} and {2}'     # Por posición
template.format('spam','ham','eggs')

template = '{moto}, {pork}, and {food}'   # por llave
template.format(moto = 'spam', pork = 'ham', food = 'milk')

template = '{moto},{0},{food}'   # Ambos
template.format('ham', moto = 'spam', food = 'milk')

texto = '{} mundo, ya estamos en {}, {}'
texto.format('Hola',2020, 'Felicidades')

############################
# metodos
############################

s = 'aaaaaXXXbbbbbbXXXcccccc'
s.replace('XXX','OOO') # reemplaza todas las posiciones
s.replace('XXX','OOO',1) # reeplaza solo la primera coincidencia

S = list(s) # convierte a lista el sgtring para reaizar operaciones in-place
s = ''.join(S) # vuelve a unir la lista en un string para su uso

j = 'PREUBA'.join(['hola','mira','la']) # hace un join del string con la lista pasada

################################
# Parsing Text
################################

line = 'aa bb cc dd'
line.split() # los separa por el especio default

line = 'hola,40,M,trabajador'
line.split(',')

line = "The knights who say Ni!\n"
line.rstrip() # elimina el salto de linea
line.upper() # mayuscula
line.isalpha() #testea
line.endswith('Ni!\n') #testea si termona con la expresion
line.startswith('The') # analogo

