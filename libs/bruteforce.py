from encryption import OffsetEncrypt

def offsetBruteForce(data:bytes)->str:
    solutions=[]
    text = data.decode("utf8")
    text = text.replace("\0", "")
    offset = 0
    while offset < 4058:
        newString = ""
        for c in text:
            if(c == "\0"):
                continue
            newCode = ord(c) - offset
            if newCode == ord(" ") or (newCode >= ord("a") and newCode <= ord("z")) or (newCode >= ord("A") and newCode <= ord("Z")) or (newCode >= ord("0") and newCode <= ord("9")):
                newString += chr(newCode)
                if(newString.__len__() == text.__len__()):
                   solutions.append(newString)
                continue
            else:
                break
        offset += 1
    return solutions

test = OffsetEncrypt(267)
encr = test.encrypt("Ceci est un test de phrase un peu plus longue")
print(encr)
res = offsetBruteForce(encr)
print(res)