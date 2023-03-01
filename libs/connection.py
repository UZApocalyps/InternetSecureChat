import socket
import threading
from enum import Enum

encoding = "utf8"
decoding = encoding

class MessageType(Enum):
    TEXT = 1
    IMAGE = 2

class Connection:
    started = False
    thread = None
    recSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sendSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connected = False
    def __init__(self, hostname:str, port:int):
        try:
            self.recSock.connect((hostname, port))
            self.sendSock.connect((hostname, port))
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
            msg = self.recSock.recvmsg(128)
            if(msg[0].decode(decoding) != ""):
                print(msg)

    def send(self, toSend:bytes or str, type:MessageType):
        #Protocol is 'ISC'
        # Then either i for image or t for text
        #
        # if t -> 'ISCt' + length on 2 bytes + message encoded in utf8
        # if i -> 'ISCi' + (width <= 128) + (heigh <= 128) + pixels value in RGB
        header = "ISC".encode(encoding)
        data = None
        if(type == MessageType.TEXT):
            header += 't'.encode(encoding)

            # Checking data size
            if(data.__len__ > 99):
                print("Please send a message smaller than 100 char")
                return
            
            # Converting to byte if it's a string
            if(toSend is str):
                toSend = toSend.encode(encoding)

            # Adding length to header
            header += toSend.__len__().to_bytes(2, 'big')
        elif (type == MessageType.IMAGE):
            print("Not supported yet")
            return
        message = header + toSend
        self.sendSock.send(message)
        