
from PyQt5 import uic

WINDOW_NAME, BASE_CLASS = uic.loadUiType("ventana_error.ui")

class VentanaError(WINDOW_NAME, BASE_CLASS):

    signal_error = None

    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def init_signal(self):
        self.signal_error.connect(self.init_gui)

    def init_gui(self):
        self.show()