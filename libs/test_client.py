from encryption import Encrypt

import connection

realServerIp = "vlbelintrocrypto.hevs.ch"
realServerPort = 6000
encr = Encrypt()
test = connection.Connection(realServerIp, realServerPort)
test.startListening()
test.send(encr.formatString("test"))
while True:
    a = 4