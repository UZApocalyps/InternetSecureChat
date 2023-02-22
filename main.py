"""""
Author: Gabriel Rossier
Date: 2023-02-22
Description: This is the main file of InternetSecureChat project.
"""""
import sys
from modules.uiLoader import UILoader
from PyQt6.QtWidgets import QApplication, QLabel,QListWidgetItem

app = UILoader.UILoader("ui/form.ui")

app.window.btnSend.clicked.connect(lambda:send())
app.window.inptMessage.returnPressed.connect(lambda:send())

def received(message):    
    return
    
def send():
    message = app.window.inptMessage.text()
    app.window.listWidget.addItem("YOU > " + message)
    app.window.inptMessage.setText("")

app.show()
app.exec()
