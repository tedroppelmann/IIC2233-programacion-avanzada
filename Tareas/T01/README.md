# Tarea 1: DCCriaturas Fantásticas 🔮

Estimado ayudante:

Creo haber implementado todo lo que se pedía de la tarea en mi programa 😃. Intenté que cada función dentro del programa esté explicada dentro de esta con la descripción de lo que hace. 

### Cosas implementadas y no implementadas :white_check_mark: :x:

NOTA: La explicación de los atributos y métodos de cada clase están en el archivo ```explicacion_diagrama.md```

* **Programación orientada a objetos**: 
    * **Juego**: ✅ Clase que inicia el comienzo del juego y pobla las otras clases desde los archivos .csv.
  
    * **Magizoologo**: ✅ Es una clase abstracta que representa a cada magizoólogo. Además de los atributos provenientes del archivo .csv, agregue ```energia_actual```y ```nivel_aprobacion```. De esta clase heredan 3 subclases: ```Docencio```, ```Tareo```y ```Híbrido```. Los métodos de las subclases que hacen overriding de los métodos de la clase padre son: ```alimentar_criatura```, ```recuperar_criatura``` y ```usar_habilidad_especial```.
    
    * **Criatura**: ✅ Es una clase absatracta que representa a cada criatura creada en el juego. Además de los atributos provenientes del archivo .csv, agregue ```comio_hoy``` (booleano que es True si la criatura comió hoy) y ```precio```. De esta clase heredan 3 subclases: ```Augurey```, ```Niffler```y ```Erkling```. Los métodos de las subclases que hacen overriding de los métodos de la clase padre son: ```cambiar_hambre``` y ```habilidad_comienzo_dia```.
    
    * **Alimento**: ✅  Es una clase abstracta que representa los tipos de alimento que existen en el juego. Posee los atributos ```nombre```,```efecto_salud```y ```precio```. De esta clase heredan 3 subclases: ```TartaDeMelaza```, ```HigadoDeDragon```y ```BunueloDeGusarajo```.  Los métodos de las subclases que hacen overriding de los métodos de la clase padre son: ```particularidad_alimento```(representa la característica especial que otorga el alimento al ser utilizado).
    
    * **Dcc**: ✅ Es la clase que maneja casi todo dentro del juego. Posee como atributos diccionarios con la información de los magizoólogos creados, las criaturas creadas y los alimentos que existen. Posee gran parte de los métodos que moldean el juego, desde crear un usuario hasta pasar al día siguiente. 
    
* **Partidas**:
   * **Crear partida**:
      * **Verificar nombre válidos y únicos**: ✅ 
      * **Perimite elegir tipo de Magizoólogo y DCCriatura**: ✅ 
      * **Se instancia correctamente el Magizoólogo seleccionado, considerando los valores iniciales de sus atributos**: ✅ 
      * **Se instancia correctamente la DCCriatura seleccionada, considerando los valores iniciales de sus atributos**: ✅ 
      * **Se muestra mensaje de error cuando el nombre que se ingresa no es válido y se deja volver a ingresar, volver atrás o salir**: ✅
   * **Cargar partida**:
      * **Se logra cargar un Magizoologo existente**: ✅ 
      * **Poblar el sistema desde los archivos (magizoologo.csv y criaturas.csv) con las instancias correspondientes**: ✅ 
      * **Se muestra mensaje de error cuando el nombre que se ingresa no es válido y se deja volver a ingresar, volver atrás o salir**: ✅ 
   * **Guardar**:
      * **Se actualiza correctamente la información de la partida en los archivos correspondientes (magizoologos.csv, criaturas.csv)**: ✅ 
* **Acciones**:
   * **Cuidar DCCriaturas**:
      * **Se puede elegir a una criatura para alimentar y el alimento a utilizar correctamente. Se actualiza correctamente el estado de la DCCriatura**: ✅ La implementación aquí no es tan práctica, ya que el programa te pedirá los nombres de las criaturas y los alimentos (no hace diferencia entre mayúsculas y minúsculas pero los tildes hay que ponerlos).
      * **Se aplica correctamente los efectos de los alimentos**: ✅ 
      * **Se implementa correctamente la posibilidad de ataque de las DCCriaturas sus dueños**: ✅ 
      * **Se muestra las criaturas que se han escapado y se puede elegir una para recuperar correctamente. Se actualiza correctamente el estado de la DCCriatura**: ✅ 
      * **Se muestran todas las DCCriaturas que se han enfermado y se puede elegir una para sanar correctamente. Se actualiza correctamente el estado de la DCCriatura**: ✅ 
      * **Se implementa correctamente la habilidad especial según el tipo de Magizoólogo**: ✅ 
      * **Se descuenta el costo de energía mágica correspondiente a las acciones alimentar, recuperar y sanar**: ✅ 
      * **Se notifica en caso de no tener energía suficiente para realizar la acción**: ✅ 
   * **DCC**:
* ...
* <Nombre item pauta<sub>n</sub>>: Me faltó hacer <insertar qué cosa faltó>

## Ejecución :computer:
El módulo principal de la tarea a ejecutar es  ```archivo.py```. Además se debe crear los siguientes archivos y directorios adicionales:
1. ```archivo.ext``` en ```ubicación```
2. ```directorio``` en ```ubicación```
3. ...


## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:

1. ```librería_1```: ```función() / módulo```
2. ```librería_2```: ```función() / módulo``` (debe instalarse)
3. ...

### Librerías propias
Por otro lado, los módulos que fueron creados fueron los siguientes:

1. ```librería_1```: Contiene a ```ClaseA```, ```ClaseB```, (ser general, tampoco es necesario especificar cada una)...
2. ```librería_2```: Hecha para <insertar descripción **breve** de lo que hace o qué contiene>
3. ...

## Supuestos y consideraciones adicionales :thinking:
Los supuestos que realicé durante la tarea son los siguientes:

1. <Descripción/consideración 1 y justificación del por qué es válido/a> 
2. <Descripción/consideración 2 y justificación del por qué es válido/a>
3. ...

PD: <una última consideración (de ser necesaria) o comentario hecho anteriormente que se quiera **recalcar**>

menu error solo cuando np es numero
-------



**EXTRA:** si van a explicar qué hace específicamente un método, no lo coloquen en el README mismo. Pueden hacerlo directamente comentando el método en su archivo. Por ejemplo:

```python
class Corrector:

    def __init__(self):
          pass

    # Este método coloca un 6 en las tareas que recibe
    def corregir(self, tarea):
        tarea.nota  = 6
        return tarea
```

Si quieren ser más formales, pueden usar alguna convención de documentación. Google tiene la suya, Python tiene otra y hay muchas más. La de Python es la [PEP287, conocida como reST](https://www.python.org/dev/peps/pep-0287/). Lo más básico es documentar así:

```python
def funcion(argumento):
    """
    Mi función hace X con el argumento
    """
    return argumento_modificado
```
Lo importante es que expliquen qué hace la función y que si saben que alguna parte puede quedar complicada de entender o tienen alguna función mágica usen los comentarios/documentación para que el ayudante entienda sus intenciones.

## Referencias de código externo :book:

Para realizar mi tarea saqué código de:
1. \<link de código>: este hace \<lo que hace> y está implementado en el archivo <nombre.py> en las líneas <número de líneas> y hace <explicación breve de que hace>



## Descuentos
La guía de descuentos se encuentra [link](https://github.com/IIC2233/syllabus/blob/master/Tareas/Descuentos.md).
