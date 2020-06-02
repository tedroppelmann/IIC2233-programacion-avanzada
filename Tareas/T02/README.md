# Tarea 2: DCCafé ☕️

Estimado ayudante:

Creo haber implementado la mayoría de lo que se pedía de la tarea en mi programa 😃. Para una mayor facilidad en la correción, dentro del código voy explicando varias cosas que utilicé y su funcionamiento. También agregue prints explicativos a medida que se va desarrollando el juego. 

### Cosas implementadas y no implementadas :white_check_mark: :x:

* **Ventana de Inicio**: 
    * **La ventana de inicio se visualiza correctamente. Los elementos no se superponen entre sí.** ✅ 
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
   * **Bocadillos**:
      * **El tiempo de preparación cambia según la fórmula establecida.** ✅  
      * **La calidad del bocadillo cambia según la fórmula establecida.** ✅  Está implementado en la clase Mesero
   * **Clientes**: 
      * **Los clientes cambian de estado cuando corresponde.** ✅
      * **Los clientes desaparecen después de recibir su bocadillo o una vez que se acabe el tiempo de espera.** ✅  
      * **Los clientes cambian de sprite dependiendo de su estado de ánimo.** ✅  
   * **DCCafé**: 
      * **Calcula correctamente los clientes por ronda.** ✅
      * **Calcula correctamente la reputación.** ✅  
* **Tiempo**: 
   * **Los procesos internos del DCCafé respetan el reloj del juego.** ✅ 
   * **Esta implementado el botón Pausa y la letra P, al seleccionarlo no aumenta el tiempo de juego, y se detienen todas las animaciones.** ❌ Intenté de muchas formas pero ninguna daba un resultado satisfactorio. El botón está implementado pero no hace nada.

* **Funcionalidades Extra**: Se activan al presionar las teclas al mismo tiempo.
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
4. ```time```: ```sleep()```
5. ```random```: ```randint```, ```choice```
6. ```math```: ```floor()```
7. ```PyQt5```: ```uic```
8. ```PyQt5.QtGui```: ```QPixmap```
9. ```PyQt5.QtWidgets```: ```QLabel```, ```QApplication```
10. ```PyQt5.QtCore```: ```pyqtSignal```, ```Qt```, ```QRect```, ```QThread```, ```QObject```, ```QMimeData```

### Librerías propias
Por otro lado, los módulos que fueron creados fueron los siguientes:

1. ```DCCafe.py```: Es el módulo principal del back-end del programa. Contiene la mayoría del funcionamiento del juego.
2. ```drag_and_drop.py```: Contiene las clases ```DropLabel```y ```DraggableLabel```que permiten el funcionamineto básico del Drag and Drop. 
3. ```entidades.py```: Contiene las clases ```Mesero```, ```Chef```y ```Cliente```con sus respectivos métodos. 
4. ```parametros.py```: Contiene todos los parámetros que se utilizan en el programa. 
5. ```reloj.py```: Contiene a la clase ```Reloj``` que permite manejar los tiempos de las funcionalidades del juego.
6. ```ventana_juego.py```: Es el front-end de la página principal del juego.
7. ```ventanas.py```: Contiene el front-end de las otras ventanas del juego, como la ventana de inicio, la de post ronda y la ventana final. 

## Supuestos y consideraciones adicionales :thinking:
Los supuestos que realicé durante la tarea son los siguientes:

1. El mapa que se carga es el mapa que no contiene bordes y tiene la pared en la parte superior. Para que se vea mejor, el mesero se puede mover dentro del piso en un espacio un poco más pequeño que el tamaño del mapa
2. Los objetos arrastrables tienen limitaciones al poder ubicarse. Además de no poder sobreponerse, agregué que las mesas no puedan quedar tan pegadas y los chefs no pueden ponerse tan a la orilla del mapa para que no quedara un pedazo de la imagen afuera. 
3. Como los clientes siempre salen a la izquierda de la mesa, en algunos casos se impide que las mesas puedan quedar tan juntas, como al crear un nuevo juego con mesas aleatorias o en Drag and Drop.
4. Encontré un bug que no sé cómo solucionarlo 😞. Si es que aparece un cliente justo cuando el mesero está en esa posición, este queda "atrapado" hasta que desaparezca el cliente. 

## Referencias de código externo :book:

Para realizar mi tarea saqué código de:
1. https://recursospython.com/guias-y-manuales/drag-and-drop-con-pyqt-4/: modela el Drag and Drop (con algunas modificaciones propias) y está implementado en el archivo ```drag_and_drop.py``` en las líneas 12 y 55. La clase ```DropLabel``` crea el "lugar" en donde caerán los arrastrables. La clase ```DraggableLabel```permite hacer los objetos arrastrables.
2. https://stackoverflow.com/questions/50232639/drag-and-drop-qlabels-with-pyqt5: al igual que el anterior, modela el Drag and Drop (con algunas modificaciones propias) y está implementado en el archivo ```drag_and_drop.py``` en las líneas 12 y 55. La clase ```DropLabel``` crea el "lugar" en donde caerán los arrastrables. La clase ```DraggableLabel```permite hacer los objetos arrastrables.
3. https://www.daniweb.com/programming/software-development/code/485072/count-seconds-in-the-background-python: modela la creación del reloj del juego y está implementado en el archivo ```reloj.py``` en las líneas 8 y 37. Crea la clase ```Reloj```que genera un thread que va contando el tiempo que pasa según una velocidad dada por el intervalo que se le da a cada instancia.

