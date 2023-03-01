

import connection

realServerIp = "vlbelintrocrypto.hevs.ch"
realServerPort = 6000

test = connection.Connection("127.0.0.1", 12345)
test.startListening()
test.send("Let's gooo".encode("utf8"))
while True:
    a = 4