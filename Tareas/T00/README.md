# Tarea 0: DCCahuín

## Consideraciones generales :octocat:

<Descripción de lo que hace y que **_no_** hace la tarea que entregaron junto
con detalles de último minuto y consideraciones como por ejemplo cambiar algo
en cierta línea del código o comentar una función>

### Cosas implementadas y no implementadas :white_check_mark: :x:

* **Menú de inicio**: 

    * **Ingresar usuario**:
      * **Ingresar si usuario existe**: Hecho 
      * **Mostrar si nombre de usuario no existe**: Hecho
      * **Opción de ingresar al menú de prograpost o seguidores**: Hecho
      
    * **Crear usuario**:
      * **Cumplir mínimo de 8 caracteres alfanuméricos**: --
      * **Notificar si nombre de usuario esta registrado**: Hecho
      * **Cumplir mínimo de una letra y un número**: --
      * **Opción de ingresar al menú de prograpost o seguidores**: --
      
    * **Salir**:
      * **Finalización del programa**: Hecho
      
* **Menú de prograpost**:

    * **Crear prograpost**:
      * **Agregar post con fecha, autor y cuerpo**: Hecho
      * **Cumplir mínimo de 1 caracter y notificar si no**: Hecho
      * **Cumplir el máximo de 140 caracteres y notificar si no**: Hecho
      * **Regresar al menú anterior**: Hecho
      
    * **Eliminar prograpost**:
      * **Mostrar posts publicados por el usuario**: Hecho
      * **Dar la opción de señalar cual quiere eliminar**: Hecho. El programa da la opción de seleccionar el número de post.
      * **Eliminar post**: Hecho
      * **Regresar al menú anterior**: Hecho
      
    * **Ver prograposts**:
      * **Dar la opción de mostrar posts de manera ascendente o descendente**: Hecho
      * **Mostrar prograpost con fecha de publicación**: Hecho. El programa muestra en una lista el post [fecha, cuerpo]
      * **Regresar al menú anterior**: Hecho
      
    * **Ver prograprost de los usuarios seguidos**:
      * **Dar la opción de mostrar posts de manera ascendente o descendente**: Hecho
      * **Mostrar prograpost con fecha de publicación y autor**: Hecho. El programa muestra en una lista el post [fecha, autor, cuerpo]
      * **Regresar al menú anterior**: Hecho
      
    * **Regresar al menú anterior**: Hecho
    
* **Menú de seguidores**:

    * **Seguir a un usuario**:
      * **Seguir al usuario**: Hecho
      * **Notificar si nombre de usuario no existe**: Hecho
      * **Notificar si intentas seguirte a ti mismo**: Hecho
      * **Notificar si ya sigues al usuario**: --
      * **Regresar al menú anterior**: Hecho
      
    * **Dejar de seguir a un usuario**:
      * **Dejar de seguir al usuario**: Hecho
      * **Notificar si nombre de usuario no existe**: Hecho
      * **Notificar si no sigues al usuario**: Hecho
      * **Regresar al menú anterior**: Hecho
      
    * **Regresar al menú anterior**: Hecho
      
## Ejecución :computer:
El módulo principal de la tarea a ejecutar es  ```menu.py```.

## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:

1. ```sys```: ```exit()```
2. ```os```: ```path.join()```
3. ```datetime```: ```today()```, ```strftime()``` / ```date```

### Librerías propias
Por otro lado, los módulos que fueron creados fueron los siguientes:

1. ```usuarios.py```: Contiene las funciones básicas en relación a los usuarios como ```agregar``` e```ingresar```.
2. ```prograposts.py```: Contiene las funciones básicas en relación al manejo de posts como ```crear```, ```ver_posts```, ```eliminar``` o ```ver_posts_seguidores```.
3. ```seguidores.py```: Contiene las funciones básicas en relación al manejo de los seguidores del usuario como ```seguir```, ```dejar``` y ```lista_seguidores```.

## Supuestos y consideraciones adicionales :thinking:
Los supuestos que realicé durante la tarea son los siguientes:

1. <Descripción/consideración 1 y justificación del por qué es válido/a> 
2. <Descripción/consideración 2 y justificación del por qué es válido/a>
3. ...

PD: <una última consideración (de ser necesaria) o comentario hecho anteriormente que se quiera **recalcar**>


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
