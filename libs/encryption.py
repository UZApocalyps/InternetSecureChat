
class Encrypt():
    def formatString(data:str)->bytes:
        final = ""
        for c in data:
            for x in range(4-len(c.encode("utf8"))):
                final += '\0'
            final += c
        return final.encode("utf8")

class OffsetEncrypt():
    offset=None

    def __init__(self, offset:int):
        self.offset = offset

    def encrypt(self, data:str)->bytes:
        text = data
        finalData = b''
        for c in text:
            newChar = chr(ord(c) + self.offset).encode("utf8")
            while newChar.__len__() < 4:
                newChar = newChar + "\0".encode("utf8")
            finalData += newChar
        return finalData

    def decrypt(self, data:bytes)->str:
        print(data)
        text = data.decode("utf8")
        finalText = ""
        for c in text:
            if(c != "\0"):
                try:
                    finalText += chr(ord(c) - self.offset)
                except ValueError:
                    print("Found char not in range with current offset")
        return finalText
