import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(("127.0.0.1", 12345))
print("Listening on 127.0.0.1:12345")
s.listen(5)

while True:
    print("Waiting for connection")
    (clientSocket, address) = s.accept()
    print(address)
    clientSocket.send(bytes("Hello from the server", "utf-8"))