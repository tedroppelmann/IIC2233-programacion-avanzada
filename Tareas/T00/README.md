# Tarea 0: DCCahuín


Un buen ```README.md``` puede marcar una gran diferencia en la facilidad con la que corregimos una tarea, y consecuentemente cómo funciona su programa, por lo en general, entre más ordenado y limpio sea éste, mejor será 

Para nuestra suerte, GitHub soporta el formato [MarkDown](https://es.wikipedia.org/wiki/Markdown), el cual permite utilizar una amplia variedad de estilos de texto, tanto para resaltar cosas importantes como para separar ideas o poner código de manera ordenada ([pueden ver casi todas las funcionalidades que incluye aquí](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet))

Un buen ```README.md``` no tiene por que ser muy extenso tampoco, hay que ser **concisos** (a menos que lo consideren necesario) pero **tampoco pueden** faltar cosas. Lo importante es que sea claro y limpio 

**Dejar claro lo que NO pudieron implementar y lo que no funciona a la perfección. Esto puede sonar innecesario pero permite que el ayudante se enfoque en lo que sí podría subir su puntaje.**

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
El módulo principal de la tarea a ejecutar es  ```menu.py```. Adicionalmente se pueden abrir los siguientes archivos .py con el resto de la tarea:
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
