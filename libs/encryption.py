
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
        text = data.decode("utf8")
        finalText = ""
        for c in text:
            if(c != "\0"):
                try:
                    finalText += chr(ord(c) - self.offset)
                except ValueError:
                    print("Found char not in range with current offset")
        return finalText


class ComplexOffsetEncrypt:
    keyword=None

    def __init__(self, keyword:str):
        if(keyword == ""):
            print("Please use a non empty keyword")
            return
        self.keyword = keyword

    def __getKeywordChar(self, index:int)-> str:
        return self.keyword[index % self.keyword.__len__()]

    def encrypt(self, data:str)->bytes:
        finalData = b''
        keywordIndex = 0
        for c in data:
            currentKeywordChar = self.__getKeywordChar(keywordIndex)
            newChar = chr(ord(c) + ord(currentKeywordChar)).encode("utf8")
            while newChar.__len__() < 3:
                newChar += b"\0"
            finalData += newChar
            keywordIndex += 1
        return finalData

    def decrypt(self, data:bytes)->str:
        text = data.decode("utf8")
        keywordIndex = 0
        finalText = ""
        for c in text:
            if c == "\0":
                continue
            keywordChar = self.__getKeywordChar(keywordIndex)
            newChar = chr(ord(c) - ord(keywordChar))
            finalText += newChar
            keywordIndex += 1
        return finalText


test = ComplexOffsetEncrypt("test")
encr = test.encrypt("aha ?")
print(encr)
print(test.decrypt(encr))