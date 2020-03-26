from classtools import AttrDisplay

class Person(AttrDisplay):
    """
    Crea y procesa el registro de una persona
    """

    def __init__(self, name, job = None, pay = 0):  # Constructor takes 3 arguments
        self.name = name                            # Fill out fields when created
        self.job = job                              # self is the new instance object
        self.pay = pay

    def lastName(self):                             # Behavior methods
        return self.name.split()[-1]                # self is implied subject

    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))    # Must change here only

    #def __str__(self):                                     #es comentado pq sera importado
    #    return '[Person %s, %s]' % (self.name, self.pay)

class Manager(Person):
    """
    Una persona especial con requerimientos especiales
    """

    def __init__(self, name, pay):
        Person.__init__(self, name, 'mgr', pay)

    def giveRaise(self, percent, bonus = 0.10):
        Person.giveRaise(self, percent + bonus)      # Good: augment original

# Testeando el código
"""
Al agregar la siguiente condicion siguiente garantizamos que cuando corramos el script
se muestren los resultados pero si se importa el script no se muestran las pruebas.

Ahora, obtenemos exactamente el comportamiento que buscamos: ejecutar el archivo 
como un script de nivel superior lo prueba porque su __nombre__ es __principal__, 
pero importarlo luego como una biblioteca de clases no:
"""

if __name__ == '__main__':
    bob = Person('Bob Smith')                         # Test the class
    sue = Person('Sue Jones', job='dev', pay=100000)  # Runs __init__ automatically
    print(bob)                          # Fetch attached attributes
    print(sue)                          # sue's and bob's attrs differ
    print(bob.lastName(), sue.lastName())             # Use the new methods
    sue.giveRaise(.10)                                # instead of hardcoding
    print(sue)
    #tom = Manager('Tom Jones', 'mgr', 50000)          # Make a Manager: __init__
    tom = Manager('Tom Jones', 50000)                 # Job name not needed:
    tom.giveRaise(.10)                                # Runs custom version
    print(tom.lastName())                             # Runs inherited method
    print(tom)                                        # Runs inherited __str__

    #print('--All three--')
    #for object in (bob, sue, tom):                    # Process objects generically
    #    object.giveRaise(.10)                         # Run this object's giveRaise
    #    print(object)                                  # Run the common __str__