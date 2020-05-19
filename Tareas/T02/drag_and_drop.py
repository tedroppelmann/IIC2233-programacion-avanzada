
# https://recursospython.com/guias-y-manuales/drag-and-drop-con-pyqt-4/
# https://stackoverflow.com/questions/50232639/drag-and-drop-qlabels-with-pyqt5

# Las clases de este módulo fueron sacadas de los link señalados arriba.
# Se les hizo algunas modificaciones para la tarea.

from PyQt5.QtCore import Qt, QMimeData, pyqtSignal
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QDrag, QPainter, QPixmap

class DropLabel(QLabel):

    signal_drag_and_drop = None

    def __init__(self, *args, **kwargs):
        QLabel.__init__(self, *args, **kwargs)
        self.setAcceptDrops(True)  # Aceptar objetos

    def dragEnterEvent(self, event):
        # Ignorar objetos arrastrados sin información
        if event.mimeData().hasText():
            event.acceptProposedAction()

    def dropEvent(self, event):
        # Establecer el widget en una nueva posición
        pos = event.pos()
        print(f'Posición: {pos.x()},{pos.y()}')
        nombre = event.mimeData().text()
        print(nombre)
        self.signal_drag_and_drop.emit(pos.x(), pos.y(), nombre)

        #Eliminar y cambiar por la condiciones en backend


class DraggableLabel(QLabel):
    name = str()
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drag_start_position = event.pos()

    def mouseMoveEvent(self, event):
        if not (event.buttons() & Qt.LeftButton):
            return
        if (event.pos() - self.drag_start_position).manhattanLength() < QApplication.startDragDistance():
            return
        drag = QDrag(self)
        mimedata = QMimeData()
        mimedata.setText(self.name)
        drag.setMimeData(mimedata)
        pixmap = QPixmap(self.size())
        painter = QPainter(pixmap)
        painter.drawPixmap(self.rect(), self.grab())
        painter.end()
        drag.setPixmap(pixmap)
        drag.setHotSpot(event.pos())
        drag.exec_(Qt.CopyAction | Qt.MoveAction)

class Window(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setWindowTitle("Drag and Drop")
        self.resize(600, 300)

        self.dropbox1 = DropLabel(self)
        self.dropbox1.setGeometry(10, 10, 580, 130)
        self.dropbox2 = DropLabel(self)
        self.dropbox2.setGeometry(10, 150, 580, 130)

        self.label = DraggableLabel(self.dropbox1)
        self.label.setGeometry(10, 10, 150, 20)
        self.label.setText("Hazme click y mueveme")


if __name__ == "__main__":
    app = QApplication([])
    window = Window()
    window.show()
    app.exec_()