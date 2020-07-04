# Tarea 3: DCCuatro 🃏


Estimado ayudante:

Creo haber implementado la mayoría de lo que se pedía de la tarea en mi programa 😃. Espero que no sea difícil de corregir la tarea.
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
* **Servidor**: El módulo principal a ejecutar es  ```main.py```. 
* **Cliente**: El módulo principal a ejecutar es  ```main.py```. 

## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:
* **Servidor**:
   1. ```json```: ```dumps```,```loads```,```load```
   2. ```socket```: ```socket```, ```bind```, ```listen```, ```accept```
   3. ```threading```: ```Thread```, ```Lock```
   4. ```base64```: ```b64enconde```,```b64encodebytes```
   5. ```time```: ```sleep```
   6. ```random```: ```choice```

* **Cliente**:
   1. ```sys```: ```exit()```
   2. ```PyQt5.QtWidgets```: ```QLabel```, ```QApplication```
   3. ```PyQt5```: ```uic```
   4. ```PyQt5.QtCore```: ```pyqtSignal```, ```QTimer```, ```QObject```
   5. ```PyQt5.QtGui```: ```QPixmap```, ```QTransform```
   6. ```json```: ```dumps```,```loads```,```load```
   7. ```threading```: ```Thread```
   8. ```socket```: ```socket```, ```connect```
   9. ```base64```: ```b64decodebytes```

### Librerías propias
Por otro lado, los módulos que fueron creados fueron los siguientes:
* **Servidor**:
   * ```servidor.py```: Contiene la clase ```Servidor```, que forma toda la lógica detrás del juego. Recibe, analiza y envía mensajes al cliente.
   * ```tabla.py```: Contiene la clase ```Tabla```,que le da forma a los logs del servidor de una manera más ordenada.
   * ```turnos.py```: Contiene la clase ```Turnos```, la cual permite ordenar de mejor manera a los jugadores del juego, desde cambiar el turno, invertir el orden y eliminar a jugadores.

* **Cliente**:
   * ```cliente.py```: Contiene la clase ```Cliente```y es la encargada de recibir y enviar mensajes entre el cliente y el servidor y transmitir los mensajes por señales al front-end.
   * ```error.py```: Ventana emergente que avisa si el servidor se desconectó a cada uno de los clientes.
   * ```ventana_color.py```: Ventana emergente que aparece al jugar la carta color para decidir el nuevo color.
   * ```ventana_espera.py```: Ventana que visualiza la sala de espera mientras faltan jugadores.
   * ```ventana_final.py```: Ventana final del juego que señala a cada jugador si fue ganador o perdedor.
   * ```ventana_juego.py```: Ventana principal del front-end. Muestra el juego en sí y mantiene actualizado a todos los clientes.

## Supuestos y consideraciones adicionales :thinking:
Los supuestos que realicé durante la tarea son los siguientes:

1. Recomiendo jugarlo en pantalla completa, ya que al agregar cartas la pantalla a veces cambia de tamaño, lo que es molesto. 
2. Al comenzar el juego y cargar las cartas iniciales, las cartas de los contrincantes se demoran un poco más en salir que las del propio cliente, lo que visualmente no es tan bonito, pero afecta el juego. 
3. Si el juego empieza con una carta color, decidí que se escogiera un color al azar inicial, el cual es informado.
4. Si se empieza con un +2, también se considera que el primer jugador tendrá que sacar 2 cartas.
5. Si se empieza con un cambio de sentido, cambia el sentido inicial.
5. El orden inicial de la partida es según el orden de llegada a la sala de espera.
6. Si se quiere sacar una carta del mazo, se debe apretar la ilustración del mazo a la derecha de la ventana.
7. IMPORTANTE: Consideré la carpeta sprites dentro del directorio del servidor para el envío de cartas y en el caso del logo del juego, este se encuentra afuera de los dos directorios. Es decir, cuando el cliente busca el logo busca en el directorio externo (ver parámetros del cliente).


## Referencias de código externo :book:

Para realizar mi tarea saqué código de:
1. La estructura de envíos mediante los socket fue sacada desde un módulo de jupyter de la semana de Networking, solo que a este le agregué el formato JSON (esto es para todos los mensajes excepto el envío de cartas).
2. http://josbalcaen.com/maya-python-pyqt-delete-all-widgets-in-a-layout/: Utilizo este código para limpiar completamente los Layouts creados de manera más fácil. Es decir, elimina todo QLabel creado dentro del Layout. Se encuentra desde la línea 221 a la 227 del módulo ```ventana_juego.py```.
3. http://www.3engine.net/wp/2015/11/pyqt-como-hacer-que-qlabel-sea-clicable/: Utilizo este código para hacer clicleable un QLabel, lo cual no viene por defecto. Es utilizado para las cartas. Se ecnuentra entre la línea 231 a la 243 del módulo ```ventana_juego.py```.
