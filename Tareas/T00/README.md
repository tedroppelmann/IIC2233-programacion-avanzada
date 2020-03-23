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

1. Cuando el usuario pide ver los prograspost que ha creado, el programa los visualiza en forma de lista con los siguientes elementos: [FECHA, MENSAJE].
2. Cuando el usuario pide ver los prograspost de sus seguidores, el programa los visualiza en forma de lista con los siguientes elementos: [FECHA, USUARIO, MENSAJE].
3. Para eliminar algún post creado, enumero cada uno de los posts del usuario y le pregunto después cual es el número de post que desea eliminar.
