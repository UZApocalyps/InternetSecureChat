"""""
Author: Gabriel Rossier le fameux lécheur des deux sphères d'un mec
Date: 2023-02-22
Description: This is the main file of InternetSecureChat project.
"""""
import sys
from modules.uiLoader import UILoader
from PyQt6.QtWidgets import QApplication, QLabel,QListWidgetItem

app = UILoader.UILoader("ui/form.ui")

app.window.btnSend.clicked.connect(lambda:send())
app.window.inptMessage.returnPressed.connect(lambda:send())
app.window.btnAddKey.clicked.connect(lambda: addKey())
keyWindow = UILoader.UILoader("ui/addKey.ui")

def received(message):    
    return
    
def send():
    message = app.window.inptMessage.text()
    if(message != ""):
        app.window.listWidget.addItem("YOU > " + message)
        app.window.inptMessage.setText("")

def addKey():
    keyWindow.window.btnSave.clicked.connect(lambda:savekey(keyWindow.window.txtkey.toPlainText()))
    keyWindow.window.show()

def savekey(key):
    f = open("keys.txt", str(key))
    return

app.show()
sys.exit(app.exec())
