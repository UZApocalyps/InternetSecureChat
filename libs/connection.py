import socket
import threading
from enum import Enum

encoding = "utf8"
decoding = encoding

class Connection:
    started = False
    thread = None
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connected = False
    callback = None
    def __init__(self, hostname:str, port:int):
        try:
            self.sock.connect((hostname, port))
            self.connected = True
        except Exception as e:
            print(e)
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
            if(msg[0].decode(decoding) != ""):
                print("Received : " + msg[0].decode(decoding))
                if(self.callback is not None):
                    self.callback(msg)

    def setListeningCallback (self, callback):
        self.callback = callback
    
    def __printErrorMessage(self):
        print("Please ensure that the socket is opened !")

    def sendPicture(self, toSend:bytes, width:int, height:int):
        if(not self.connected):
            self.__printErrorMessage()
            return
        header = "ISCi".encode(encoding)
        data = None
        header += width.to_bytes(2, 'big')
        header += height.to_bytes(2, 'big')
        data = header + toSend
        self.sock.send(data)

    def send(self, toSend:bytes or str):
        #Protocol is 'ISC'
        # Then either i for image or t for text
        #
        # if t -> 'ISCt' + length on 2 bytes + message encoded in utf8
        # if i -> 'ISCi' + (width <= 128) + (heigh <= 128) + pixels value in RGB
        if(not self.connected):
            self.__printErrorMessage()
            return
        header = "ISCt".encode(encoding)
        data = None

        # Checking data size
        if(toSend.__len__() > 99):
            print("Please send a message smaller than 100 char")
            return
        
        # Converting to byte if it's a string
        if(toSend is str):
            toSend = toSend.encode(encoding)

        # Adding length to header
        header += toSend.__len__().to_bytes(2, 'big')
        message = header + toSend
        self.sock.send(message)
        