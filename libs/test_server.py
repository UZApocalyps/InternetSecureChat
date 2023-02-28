import socket
import threading

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(("127.0.0.1", 12345))
print("Listening on 127.0.0.1:12345")
s.listen(5)

def echo(self, clientSocket:socket):
    print("Starting echo thread with socket")
    while True:
        try:
            data: tuple = clientSocket.recvmsg(128)
            if(not data[0]):
                print("Client disconnected")
                break
            print("Got a message : ")
            print(data)
            clientSocket.send(data[0])
        except Exception as e:
            print("An error has occured... :(")
            print(e)
            break
    clientSocket.close()
    print("Ending thread loop")

while True:
    print("Waiting for connection")
    (clientSocket, address) = s.accept()
    print(address)
    clientSocket.send(bytes("Hello from the server", "utf-8"))
    thread = threading.Thread(target=echo, args=(1, clientSocket), daemon=True)
    thread.start()
