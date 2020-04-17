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
      * **Se puede adoptar una DCCriatura correctamente, si se cumplen las condiciones**: ✅ 
      * **Se puede comprar cualquiera de los alimentos disponibles correctamente**: ✅ 
      * **Se descuenta el valor de sickles corespondiente al adoptar DCCriaturas y se notifica en caso de no poder realizarse la acción**: ✅ 
      * **Se descuenta el valor de sickles corespondiente al comprar alimentos y se notifica en caso de no poder realizarse la acción**: ✅ 
      * **Se pueden visualizar los datos actualizados del estado del Magizoólogo y de las DCCriaturas correctamente**: ✅ 
   * **Pasar al día siguiente**:
      * **Se aplican correctamente las habilidades especiales de cada DCCriatura**: ✅ 
      * **Se actualizan los puntos de salud de las DCCriaturas dependiendo de su hambre y estado de salud**: ✅ 
      * **Se actualiza el estado de hambre de cada DCCriatura dependiendo del tiempo que lleva sin comer**: ✅ 
      * **Se actualiza correctamente el estado de salud de las DCCriaturas**: ✅ 
      * **Se actualiza correctamente la cantidad de DCCriaturas escapadas**: ✅ 
      * **Se actualiza correctamente el nivel de aprobación y el estado de la licencia del Magizoólogo**: ✅ 
      * **Se paga correctamente la cantidad de sickles al Magizoólogo y se actualiza la cantidad de sickles que tiene**: ✅ 
      * **La fiscalización se realiza correctamente: se calculan multas según los eventos de DCCriaturas**: ✅ 

* **Consola**:
   * **Menú de inicio**: ✅ 
   * **Menú de acciones**: ✅ 
   * **Menú DCCriaturas**: ✅ 
   * **Menú DCC**: ✅ 
   * **Pasar al día siguiente**: ✅ 
   * **Robustez**: ✅ 

* **Manejo de archivos**:
   * **Trabaja correctamente con todos los archivos CSV entregados**: ✅ 
   * **Utiliza e importa correctamente parametros.py**: ✅ 
   * **Archivo parametros.py contiene todos los parámetros especificados en el enunciado**: ✅ 

* **Bonus**: ❌ No alcancé a hacer ningún bonus 😞

## Ejecución :computer:
El módulo principal de la tarea a ejecutar es  ```main.py```. 

## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:

1. ```sys```: ```exit()```
2. ```os```: ```path.join()```
3. ```collections```: ```defauldict()```
4. ```abc```: ```ABC```, ```abstractmethod```
5. ```random```: ```randint```, ```choice```

### Librerías propias
Por otro lado, los módulos que fueron creados fueron los siguientes:

1. ```actualizaciones.py```: Contiene las funciones que permiten actualizar los archivos .csv.
2. ```alimentos.py```: Contiene la clase ```Alimento```y sus subclases ```TartaDeMelaza```, ```HigadoDeDragon```y ```BunueloDeGusarajo```.
3. ```cargas.py```: Contiene las funciones que permiten cargar y poblar las clases desde los archivos .csv. 
4. ```criaturas.py```: Contiene la clase ```Criatura```y sus subclases ```Augurey```, ```Niffler```y ```Erkling```.
5. ```DCC.py```: Contiene a la clase ```Dcc```.
6. ```magizoologos.py```: Contiene a la clase ```Magizoologo```y sus subclases ```Docencio```, ```Tareo```y ```Híbrido```. Además posee la función ```sickles_suficientes(sickles, precio)```.
7. ```menus.py```: Contiene todas las funciones que representan menús dentro del programa.
8. ```parametros.py```: Contiene todos los parámetros que se utilizan en el programa. 

## Supuestos y consideraciones adicionales :thinking:
Los supuestos que realicé durante la tarea son los siguientes:

1. No se si es un supuesto o un requisito de la tarea pero al mostrar los datos al pasar de día solo se notifican los nuevas criaturas que enfermaron, escaparon y que hambrientas desde hoy.
2. Los menús del tipo numeración (donde tú eliges un número entre opciones) no doy la opción de volver atrás porque se da esa opción en otras instancias. Por ejemplo, al alimentar una criatura se da la opción de volver atrás cuando te equivocas al poner en el nombre. En todo caso, en todas las opciones del programa es imposible quedar "atrapado" dentro de un menú. 
