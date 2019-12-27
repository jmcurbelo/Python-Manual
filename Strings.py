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
