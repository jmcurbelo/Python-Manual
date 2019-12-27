import sys
sys.modules[__name__].__dict__.clear()


class Worker:
    def __init__(self, name, pay):   # Initialize when created
        self.name = name             # self is the new object
        self.pay = pay
    def lastName(self):
        return self.name.split()[-1]  # self is the new object
    def giveRaise(self, percent):
        self.pay *= (1.0 + percent)   # Update pay in-place


# Esta clase define un nuevo tipo de objeto que tendrá atributos de nombre y pago
# (a veces llamado información de estado), así como dos bits de comportamiento
# codificados como funciones (normalmente llamados métodos). Llamar a la clase como
# una función genera instancias de nuestro nuevo tipo, y los métodos de la clase
# reciben automáticamente la instancia que se procesa mediante una llamada a un
# método dado (en el argumento propio):

bob = Worker('Bob Smith',50000)  # Make two instances
sue = Worker('Sue Jones', 60000) # Each has name and pay attrs
bob.lastName()                   # Call method: bob is self
sue.lastName()

sue.giveRaise(.10)               # # Updates sue's pay
sue.pay


# Otra clase creada por mi

class Boy:
    def __init__(self, Nombre, edad, estatura):
        self.Nombre = Nombre
        self.edad = edad
        self.estatura = estatura
    def escuela(self):
        if self.edad < 12:
            esc = 'Primaria'
        else:
            esc = 'Secundaria'
        return (print(self.Nombre,'debe ir a la',esc))
    def medicina(self):
        if self.estatura < 1.50:
            med = 'Debe tomar medicina'
        else:
            med = 'No debe tomar medicina'
        return (print(self.Nombre,med))

jose = Boy('Jose',15,1.70)

jose.escuela()
jose.medicina()

ali = Boy('Aliannys',4,1.45)
ali.escuela()
ali.medicina()


