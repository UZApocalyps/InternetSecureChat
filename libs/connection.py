import socket
import threading

class connection:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connected = False
    def __init__(self, hostname:str, port:int):
        try:
            self.sock.connect((hostname, port))
            self.connected = True
        except:
            print("Connection failed !")
    
    def startListening(self):
        while self.connected:
            msg = self.sock.recvmsg(128)
            if(msg[0].decode("utf-8") != ""):
                print(msg)
        