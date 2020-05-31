# Tarea 2: DCCafé ☕️

Estimado ayudante:

Creo haber implementado la mayoría de lo que se pedía de la tarea en mi programa 😃. Para una mayor facilidad en la correción, dentro del código voy explicando varias cosas que utilicé y su funcionamiento. 

### Cosas implementadas y no implementadas :white_check_mark: :x:

* **Ventana de Inicio**: 
    * **La ventana de inicio se visualiza correctamente. Los elementos no se superponen entre sí."** ✅ 
    * **Se puede crear una partida nueva o cargar una existente.** ✅ 
    * **Se cargan correctamente los datos de una partida guardada.** ✅ 
    * **Se reinician correctamente los datos de una partida.** ✅ 
    
* **Ventana de Juego**:
   * **Generales**:
      * **Se visualizan correctamente las tres áreas del juego. Los elementos no se superponen entre sí.** ✅ 
      * **Se visualizan correctamente las estadísticas del juego. Los elementos no se superponen entre sí.** ✅ 
      * **Se carga el mapa correctamente respetando las dimensiones.** ✅ 
      * **Información de la ronda, clientes y dinero se actualizan a lo largo del juego.** ✅ 
   * **Ventana de pre-ronda**:
      * **Se pueden comprar objetos de forma correcta.** ✅ 
      * **Se muestran todos los elementos que se pueden comprar en la tienda junto a sus precios. Los elementos no se superponen entre sí.** ✅ 
      * **Las mesas y el chef se pueden eliminar haciendo click. Se impide que el jugador se quede sin elementos en el mapa.** ✅ 
   * **Ventana de ronda**:
      * **Los clientes aparecen sentados en las mesas.** ✅ Siempre aparecen en el lado izquierdo de la mesa
      * **La ronda termina cuando ya no quedan clientes.** ✅ 
   * **Ventana de post-ronda**:
      * **Se visualiza una ventana con los resultados y botones.Los elementos no se superponen entre sí.** ✅ 
      * **Se puede continuar, guardar y salir.** ✅ 
      * **Las estadisticas post-ronda son correctas y reflejan el resultado de la ronda.** ✅ 
      * **Si la reputación llega a 0, el juego se termina.** ✅ 
* **Entidades**:
    * **Jugador**: 
      * **El movimiento del jugador es fluido, continuo y animado.** ✅ 
      * **Movimiento respeta colisiones no especiales.** ✅ A veces visualmente pareciera que el jugador esta bastante lejos de los objetos que colisiona, pero los label si se tocan.
      * **Movimiento respeta colisión especial con chef y clientes.** ✅ 
      * **El jugador cambia de sprite al cambiar de estado.** ✅ 
   * **Chef**:
      * **El chef cambia de estado cuando corresponde.** ✅ 
      * **Sube de nivel según la cantidad de bocadillos que haya preparado.** ✅ 
      * **Implementa la probabilidad de equivocarse correctamente. Al equivocarse se reinicia su estado.** ✅ 
      * **El chef cambia de sprite según su estado: esperando, cocinando, terminado.** ✅ 
   * **Bocadillos**: No implementé una clase Bocadillo como tal, pero sus métodos si están integrados en el programa. 
      * **El tiempo de preparación cambia según la fórmula establecida.** ✅  Está en la clase Chef
      * **La calidad del bocadillo cambia según la fórmula establecida.** ✅  Está en la clase Mesero
   * **Clientes**: 
      * **Los clientes cambian de estado cuando corresponde.** ✅
      * **Los clientes desaparecen después de recibir su bocadillo o una vez que se acabe el tiempo de espera.** ✅  
      * **Los clientes cambian de sprite dependiendo de su estado de ánimo.** ✅  
   * **DCCafé**: 
      * **Calcula correctamente los clientes por ronda.** ✅
      * **Calcula correctamente la reputación.** ✅  
* **Tiempo**: ✅ 
   * **Los procesos internos del DCCafé respetan el reloj del juego.** ✅ 
   * **Esta implementado el botón Pausa y la letra P, al seleccionarlo no aumenta el tiempo de juego, y se detienen todas las animaciones.** ❌

* **Funcionalidades Extra**:
   * **M + O + N** ✅ 
   * **F + I + N** ✅ 
   * **R + T + G** ✅ 

* **Bonus**: ❌ No alcancé a hacer ningún bonus 😞

## Ejecución :computer:
El módulo principal de la tarea a ejecutar es  ```main.py```. 

## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:

1. ```sys```: ```exit()```
2. ```os```: ```path.join()```
3. ```collections```: ```defauldict()```
4. 
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


## Referencias de código externo :book:

Para realizar mi tarea saqué código de:
1. \<link de código>: este hace \<lo que hace> y está implementado en el archivo <nombre.py> en las líneas <número de líneas> y hace <explicación breve de que hace>



## Descuentos
La guía de descuentos se encuentra [link](https://github.com/IIC2233/syllabus/blob/master/Tareas/Descuentos.md).
