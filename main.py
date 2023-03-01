"""""
Author: Gabriel Rossier le fameux lécheur des deux sphères d'un mec
Date: 2023-02-22
Description: This is the main file of InternetSecureChat project.
"""""
import sys
from modules.uiLoader import UILoader
from PyQt6.QtWidgets import QApplication, QLabel,QListWidgetItem
from libs.connection import Connection
import libs.encryption as encryption

app = UILoader.UILoader("ui/form.ui")

app.window.btnSend.clicked.connect(lambda:send())
app.window.inptMessage.returnPressed.connect(lambda:send())
app.window.btnAddKey.clicked.connect(lambda: addKey())
keyWindow = UILoader.UILoader("ui/addKey.ui")

connection = Connection("vlbelintrocrypto.hevs.ch",6000)
connection.setListeningCallback(lambda msg:received(msg))
connection.startListening()

encrypt = encryption.Encrypt

def received(message):   
    message = message[0].decode("utf8")
    addToMessageLog("server > " + message) 
    return
    
def send():
    message = app.window.inptMessage.text()
    
    if(message != ""):
        connection.send(encrypt.formatString(str(message)))
        addToMessageLog("You > "  + message)
        app.window.inptMessage.setText("")

def addKey():
    keyWindow.window.btnSave.clicked.connect(lambda:savekey(keyWindow.window.txtkey.toPlainText(),keyWindow.window.txtKeyName.toPlainText()))
    keyWindow.window.show()

def savekey(key,name):
    
    with open('storedKey/'+name+'.key', 'w') as f:
        f.write(key)
    return

def addToMessageLog(message):
    message = message.replace("\0","")
    app.window.listWidget.addItem(message)

app.show()
sys.exit(app.exec())
