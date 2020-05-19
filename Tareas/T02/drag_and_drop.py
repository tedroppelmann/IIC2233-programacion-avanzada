
#https://recursospython.com/guias-y-manuales/drag-and-drop-con-pyqt-4/
#https://stackoverflow.com/questions/50232639/drag-and-drop-qlabels-with-pyqt5

from PyQt5.QtCore import Qt, QMimeData
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QDrag

class DropLabel(QLabel):
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
        self.label = event.source()
        self.label.setParent(self)
        self.label.move(pos.x(), pos.y())
        self.label.show()

        event.acceptProposedAction()

class DraggableLabel(QLabel):
    def __init__(self, parent):
        QLabel.__init__(self, parent)

    def mousePressEvent(self, event):
        # Inicializar el arrastre con el botón derecho
        if event.button() == Qt.LeftButton:
            self.drag_start_position = event.pos()

    def mouseMoveEvent(self, event):
        # Chequear que se esté presionando el botón derecho
        if not (event.buttons() and Qt.LeftButton):
            return

        # Verificar que sea una posición válida
        if ((event.pos() - self.drag_start_position).manhattanLength()
                < QApplication.startDragDistance()):
            return

        drag = QDrag(self)
        mime_data = QMimeData()

        # Establecer el contenido del widget como dato
        mime_data.setText(self.text())
        drag.setMimeData(mime_data)

        # Ejecutar la acción
        self.drop_action = drag.exec_(Qt.CopyAction | Qt.MoveAction)

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