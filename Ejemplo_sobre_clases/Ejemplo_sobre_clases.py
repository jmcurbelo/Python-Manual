"""
Indicaciones sobre el ejemplo de clases.

1. crearemos los constructores
1.1 ponemos el segundo y tercer argumento con valores por defaul lo que nos permite
    omitirlos a la hora de instanciar la clase

2. Se agregan los metodos para trabajar con los atributos

3. Se pasa a sobreescribir el metodo print que muestra la clase, esto se hace con
   Add __str__ overload method for printing objects.
   Ahora se puede modificar en las pruebas la forma de mostar los datos con tan solo
   un print(instancia)

4. Creamos un subclase Manager que sobreescribirá el método giveRaise, la manera correcta
   de hacerlo es llamando al método original y añadiendo el bonus extra para el cálculo
   del giveRaise, así garantizamos que el código pueda ser fácilmente mantenido en el
   futuro.

5. Redefineremos el constructor para que una vez instanciada una clase del tipo manager
   automaticamente podamos asignar el tipo de job.

#######################################################
Hasta aquí este ejemplo muestra como hacer estos pasos:
#######################################################
• Instance creation—filling out instance attributes
• Behavior methods—encapsulating logic in class methods
• Operator overloading—providing behavior for built-in operations like printing
• Customizing behavior—redefining methods in subclasses to specialize them
• Customizing constructors—adding initialization logic to superclass steps

6. Hasta aquí tod'o marcha bien pero cuando mostramos los datos de una instancia,
   por ejemplo bob que es manager, lo muestra como Person, que no está mal pero deseariamos
   que lo mostrara como Manager. Para esto vamos a crear un nuevo script llamado
   classtools.py que nos servira para todas las clases.

7. Ahora se guardarán las instancias en archivos en disco que podamos luego leer. Para
   ello crearemos otro script llamado makedb.py

8. Para actualizar la base de datos crearemos otro script llamado updatedb.py. Como
   la actualizacion ocurre luego de que se muestran los archivos en este caso, debemos
   correr una segunda vez el script para ver la actualizacion de los campos

"""

