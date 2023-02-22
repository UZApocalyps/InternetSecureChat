"""""
Author: Gabriel Rossier
Date: 2023-02-22
Description: This is the main file of InternetSecureChat project.
"""""

from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("InternetSecureChat")
        self.setWindowIcon(QIcon("icon.ico"))
        self.setGeometry(100, 100, 600, 400)
        self.show()

app = QApplication([])
window = MainWindow()
window.show()

app.exec()