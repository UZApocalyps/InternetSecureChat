import socket
import threading

class connection:
    started = False
    thread = None
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connected = False
    def __init__(self, hostname:str, port:int):
        try:
            self.sock.connect((hostname, port))
            self.connected = True
        except:
            print("Connection failed !")
    
    def startListening(self):
        if(not self.started): 
            self.thread = threading.Thread(target=self.__listeningFunction, args=(), daemon=True)
            self.thread.start()
            self.started = True

    def __listeningFunction(self):
        print("Starting listening...")
        while self.connected:
            msg = self.sock.recvmsg(128)
            if(msg[0].decode("utf-8") != ""):
                print(msg)

    def send(self, data:bytes):
        print("Sending : " + data.decode("utf-8"))
        self.sock.send(data)
        