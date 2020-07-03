# Tarea 3: DCCuatro 🃏


Estimado ayudante:

Creo haber implementado la mayoría de lo que se pedía de la tarea en mi programa 😃. Para una mayor facilidad en la correción, dentro del código voy explicando varias cosas que utilicé y su funcionamiento.

### Cosas implementadas y no implementadas :white_check_mark: :x:

* **Networking**: 
    * **Correcto uso de TCP/IP.** ✅ 
    * **Instancia y conecta los sockets de manera correcta.** ✅ 
    * **Las aplicaciones pueden trabajar concurrentemente sin bloquearse por escuchar un socket.** ✅ 
    * **La conexión es sostenida en el tiempo y de propósito general para todos los tipos de mensajes que pueden intercambiar.** ✅ 
    * **Se pueden conectar múltiples clientes sin afectar el funcionamiento del programa.** ✅ 
    * **Se pueden desconectar múltiples clientes, de forma esperada, sin afectar el funcionamiento del programa.** ✅ 
    * **Se pueden desconectar múltiples clientes, de forma inesperda, sin afectar el funcionamiento del programa.** ✅ 
    
* **Arquitectura Cliente-Servidor**:
   * **Roles**:
      * **Correcta separación de recursos entre Cliente y Servidor.** ✅ 
      * **Las responsabilidades de cada cliente son consistentes al enunciado.** ✅ 
      * **Las responsabilidades del servidor son consistentes al enunciado.** ✅ 
   * **Consistencia**:
      * **Se mantiene actualizada la información en todos los clientes y en el servidor.** ✅ 
      * **Se utilizan locks cuando es necesario.** ✅ 
   * **Logs**:
      * **Se implementan logs del servidor, que permiten visualizar la información indicada en el enunciado.** ✅ 
* **Manejo de Bytes**:
    * **Codificación Cartas**: 
      * **Se utiliza little y big endian cuando corresponde para transformar a bytes valores enteros.** ✅ 
      * **Correcta implementación y manejo de la estructura de bytes.** ✅ 
   * **Decodificación Cartas**:
      * **Se utiliza little y big endian cuando corresponde para transformar de bytes a valores enteros.** ✅ 
      * **Correcta implementación y manejo de la estructura de bytes.** ✅ 
   * **Integración**:
      * **Utiliza correctamente el protocolo para el envío de mensajes.** ✅  Utilizo JSON para todos los mensajes excepto para el envío de cartas
* **Interfaz Gráfica**: 
   * **Existe una correcta separación entre front-end y back-end en el caso del cliente.** ✅ 
   * **Se visualiza correctamente la información.Los elementos no se superponen entre sí.** ✅ Al comienzo del juego no todos los labels aparecen al mismo tiempo, lo que visualmente no es tan bonito pero no afecta el flujo del programa.
   * **Solo se puede ingresar con un usuario válido, mientras hayan cupos y no se esté realizando la partida. Si es inválido se le avisa al usuario.** ✅ Envío un mensaje a través del box del nombre.
   * **Se visualizan todos los usuarios conectados.La información se actualiza correctamente para todos los clientes.** ✅ 
   * **Sala de Juego**:
      * **Se visualizan correctamente las cartas propias y de los otros jugadores. La información se actualiza correctamente para todos los clientes.** ✅ 
      * **Se visualiza correctamente la última carta jugada. La información se actualiza correctamente para todos los clientes.** ✅ 
      * **Se visualiza correctamente el jugador actual del turno y el color actual en juego. La información se actualiza correctamente para todos los clientes.** ✅ 
      * **Existe un mecanismo para jugar una carta.Manda correctamente la información al servidor y este responde apropiadamente.** ✅ 
      * **Existe un botón para sacar cartas del mazo y otro para gritar ¡DCCuatro! Manda correctamente la información al servidor y este responde apropiadamente.** ✅ El botón para sacar cartas del mazo es la carta reverso que esta a la derecha de la sala de juego.
      * **Existe un mecanismo para seleccionar un color cuando se juego un Cambio de color. Manda correctamente la información al servidor y este responde apropiadamente.** ✅ 
      * **Se implementa correctamente el Modo espectador.** ✅ 
      * **Se puede cerrar la ventana y salir del programa.** ✅ 
   * **Se informa correctamente si el jugador ganó o perdió la partida.** ✅ Aparece una ventana emergente con los resultados para cada jugador conectado.
   * **Hay un botón que redirige a la Ventana de Inicio y funciona correctamente.** ✅ 

* **Reglas del DCCuatro**: 
   * **Al inicio de la partida se reparten las cartas que corresponden a cada jugador.** ✅ 
   * **Jugar una carta**:
      * **Se implementan correctamente las cartas regulares.** ✅ 
      * **Se implementa correctamente el +2.** ✅ 
      * **Se implementa correctamente el Cambio de sentido.** ✅ 
      * **Se implementa correctamente el Cambio de color.** ✅ 
      * **El usuario puede seleccionar una carta de su mano y jugarla.** ✅ 
      * **El servidor comprueba que la carta sea válida y toma las medidas que corresponden.** ✅ 
      * **Después de jugar una carta se termina el turno del jugador.** ✅ 
   * **Robar una carta**:
       * **Se implementa correctamente el mecánismo para robar cartas.** ✅
       * **Después de robar una o multiples cartas se termina el turno del jugador.** ✅
   * **Al gritar ¡DCCuatro! se suman las cartas al jugador que corresponde.** ✅ 
   * **Término del juego**:  
       * **Si un jugador se queda sin cartas gana la partida y el resto pierde.** ✅
       * **Si un jugador supera el máximo de cartas, pierde la partida y pasa a modo espectador.** ✅
* **General**: 
   * **Todos los parametros se encuentran en alguno de los parametros.json. Se utiliza y carga correctamente parametros.json.** ✅ 
   * **Se utiliza correctamente al función `sacar_cartas()`, para sacar cartas del mazo. Se importa correctamente la función.**: ✅ 
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
5. Cuando la reputación llega a 0 al final del juego, se muestra una ventana nueva que solo deja salir y te informa que el juego finalizó. Creo que es lo más coherente. 

## Referencias de código externo :book:

Para realizar mi tarea saqué código de:
1. https://recursospython.com/guias-y-manuales/drag-and-drop-con-pyqt-4/: modela el Drag and Drop (con algunas modificaciones propias) y está implementado en el archivo ```drag_and_drop.py``` en las líneas 12 y 55. La clase ```DropLabel``` crea el "lugar" en donde caerán los arrastrables. La clase ```DraggableLabel```permite hacer los objetos arrastrables.
2. https://stackoverflow.com/questions/50232639/drag-and-drop-qlabels-with-pyqt5: al igual que el anterior, modela el Drag and Drop (con algunas modificaciones propias) y está implementado en el archivo ```drag_and_drop.py``` en las líneas 12 y 55. La clase ```DropLabel``` crea el "lugar" en donde caerán los arrastrables. La clase ```DraggableLabel```permite hacer los objetos arrastrables.
3. https://www.daniweb.com/programming/software-development/code/485072/count-seconds-in-the-background-python: modela la creación del reloj del juego y está implementado en el archivo ```reloj.py``` en las líneas 8 y 37. Crea la clase ```Reloj```que genera un thread que va contando el tiempo que pasa según una velocidad dada por el intervalo que se le da a cada instancia.
