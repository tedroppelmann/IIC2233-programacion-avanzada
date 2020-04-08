# Explicación del Diagrama de Clases:

El programa consta de 12 clases, las cuales interactúan entre ellas de cierta forma. Para la creación del diagrama de clases utilizamos las siguientes relaciones: composición, agregación y herencia. Además agregué la cardinalidad cuando era necesario. 

## Clases implementadas:

* **Juego**: Clase que contiene al juego. No posee atributos y contiene el método ```iniciar()```. Esta clase de compone de 3 otras subclases:
    * **DCC**: Es la clase del DCC. Organiza el juego en general. Permite hacer la mayoría de las acciones que puede hacer un magizoólogo, desde ser creado hasta sus respectivas acciones dentro del juego. Posee como atributos diccionarios de los magizoólogos creados, las criaturas creadas y los tipos de alimentos, además de guardar al usuario actual del juego. Posee diferentes métodos que permiten la interracción entre los magizoólogos y el DCC. Esta clase tiene una relación de composición con la ```Magizoologoo```, ya que si no existiera la Clase DCC, tampoco existiría la clase Magizoólogos, debido a que la primera los crea. 
    Posee una relación de agrupación con la clase ```Criaturas```, ya que DCC tiene un conjunto de criaturas creadas.
    También se relaciona mediante agrupación con la clase ```Alimentos```, ya uqe DCC tiene un conjunto de alimentos guardados.
    * **Alimentos**: Esta clase contiene a los alimentos que existen. Posee los atributos nombre, efecto_salud y precio. 
    * **Personajes**: Es la clase que contiene a todos los personajes del juego. Posee los atributos, nombre, tipo y nivel_magico. De esta clase heredan las siguientes:
      * **Magizoologo**: Esta clase representa a todos los magizoólogos y posee todos los atributos de estos. Además, contiene los métodos respecto a las acciones que puede realizar un magizoólogo. De esta clase heredan 3 subclases:
        * **Docencio**: Es un tipo de Magizoólogo. No posee atributos nuevos, ya que comparte todos los de su clase padre, excepto que cambia su valor. Posee todos los métodos de clase padre, pero algunos se modifican, ya que dependen del tipo de Magizoólogo. Estos métodos son ```alimentar_criatura(Criaturas)```,```recuperar_criatura(Criaturas)```y ```habilidad_especial()```. 
        * **Tareo**: Es un tipo de Magizoólogo. No posee atributos nuevos, ya que comparte todos los de su clase padre, excepto que cambia su valor. Posee todos los métodos de clase padre, pero algunos se modifican, ya que dependen del tipo de Magizoólogo. Estos métodos son ```alimentar_criatura(Criaturas)```,```recuperar_criatura(Criaturas)```y ```habilidad_especial()```. 
        * **Híbrido**: Es un tipo de Magizoólogo. No posee atributos nuevos, ya que comparte todos los de su clase padre, excepto que cambia su valor. Posee todos los métodos de clase padre, pero algunos se modifican, ya que dependen del tipo de Magizoólogo. Estos métodos son ```alimentar_criatura(Criaturas)```,```recuperar_criatura(Criaturas)```y ```habilidad_especial()```. 
      * **Criaturas**:  Esta clase representa a todos las criaturas creadas y posee todos los atributos de estas. Además, contiene los métodos respecto a las acciones que puede realizar una criatura. De esta clase heredan 3 subclases:
        * **Augurey**: Es un tipo de Criatura. No posee atributos nuevos, ya que comparte todos los de su clase padre, excepto que cambia su valor. Posee todos los métodos de clase padre y además uno más, el cual es ```buscar_alimento(Magizoologo)```.
        * **Niffler**: Es un tipo de Criatura No posee atributos nuevos, ya que comparte todos los de su clase padre, excepto que cambia su valor. Posee todos los métodos de clase padre y además dos más, el cual es ```entregar_sickles(Magizoologo)``` y ```robar_sickles(Magizoologo)```.
        * **Erkling**: Es un tipo de Criatura No posee atributos nuevos, ya que comparte todos los de su clase padre, excepto que cambia su valor. Posee todos los métodos de clase padre y además uno más, el cual es ```robar_alimento(Magizoologo)```.
        



