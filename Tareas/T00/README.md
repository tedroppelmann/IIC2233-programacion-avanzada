# Tarea 0: DCCahuín 🐦

## Consideraciones generales❗️

Estimado ayudante:

Creo haber implementado todo lo que se pedía en la tarea en mi programa. Cada función está explicada dentro de esta con la descripción de lo que hace.

### Cosas implementadas y no implementadas :white_check_mark: :x:

* **Menú de inicio**: 

    * **Ingresar usuario**:
      * **Ingresar si usuario existe**: ✅ 
      * **Mostrar si nombre de usuario no existe**: ✅ 
      * **Opción de ingresar al menú de prograpost o seguidores**: ✅ 
      
    * **Crear usuario**:
      * **Cumplir mínimo de 8 caracteres alfanuméricos**: ✅ 
      * **Notificar si nombre de usuario esta registrado**: ✅ 
      * **Cumplir mínimo de una letra y un número**: ✅ 
      * **Opción de ingresar al menú de prograpost o seguidores**: ✅ 
      
    * **Salir**:
      * **Finalización del programa**: ✅ 
      
* **Menú de prograpost**:

    * **Crear prograpost**:
      * **Agregar post con fecha, autor y cuerpo**: ✅ 
      * **Cumplir mínimo de 1 caracter y notificar si no**: ✅ 
      * **Cumplir el máximo de 140 caracteres y notificar si no**: ✅ 
      * **Regresar al menú anterior**: ✅ 
      
    * **Eliminar prograpost**:
      * **Mostrar posts publicados por el usuario**: ✅ 
      * **Dar la opción de señalar cual quiere eliminar**: ✅ El programa da la opción de seleccionar el número de post.
      * **Eliminar post**: ✅ 
      * **Regresar al menú anterior**: ✅ 
      
    * **Ver prograposts**:
      * **Dar la opción de mostrar posts de manera ascendente o descendente**: ✅ 
      * **Mostrar prograpost con fecha de publicación**: ✅ El programa muestra en una lista el post [fecha, cuerpo]
      * **Regresar al menú anterior**: ✅ 
      
    * **Ver prograprost de los usuarios seguidos**:
      * **Dar la opción de mostrar posts de manera ascendente o descendente**: ✅ 
      * **Mostrar prograpost con fecha de publicación y autor**: ✅ El programa muestra en una lista el post [fecha, autor, cuerpo]
      * **Regresar al menú anterior**: ✅ 
      
    * **Regresar al menú anterior**: ✅ 
    
* **Menú de seguidores**:

    * **Seguir a un usuario**:
      * **Seguir al usuario**: ✅ 
      * **Notificar si nombre de usuario no existe**: ✅ 
      * **Notificar si intentas seguirte a ti mismo**: ✅ 
      * **Notificar si ya sigues al usuario**:✅ 
      * **Regresar al menú anterior**: ✅ 
      
    * **Dejar de seguir a un usuario**:
      * **Dejar de seguir al usuario**: ✅ 
      * **Notificar si nombre de usuario no existe**: ✅ 
      * **Notificar si no sigues al usuario**: ✅ 
      * **Regresar al menú anterior**: ✅ 
      
    * **Regresar al menú anterior**: ✅ 
      
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

## Referencias de código externo :book:

Para realizar mi tarea saqué código de:
1. \<link de código>: este hace \<lo que hace> y está implementado en el archivo <nombre.py> en las líneas <número de líneas> y hace <explicación breve de que hace>



## Descuentos
La guía de descuentos se encuentra [link](https://github.com/IIC2233/syllabus/blob/master/Tareas/Descuentos.md).
