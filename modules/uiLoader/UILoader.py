import sys
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6 import uic
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QIODevice

class UILoader(QApplication):
    ui_file_name = ""
    ui_file = None
    window = None

    def __init__(self, uiFile):
        super().__init__(sys.argv)
        self.ui_file_name = uiFile
        self.ui_file = QFile(self.ui_file_name)
        loader = QUiLoader()
        self.window = loader.load(self.ui_file)
        self.ui_file.close()
    
    def show(self):
        self.window.show()
    
    def getUI(self):
        return self.ui
