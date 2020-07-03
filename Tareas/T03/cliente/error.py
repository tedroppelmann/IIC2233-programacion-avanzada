
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QPixmap
import json
import os
import sys

with open('parametros.json') as file:
    data = json.load(file)

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