from enum import Enum
from abc import ABC, abstractmethod



class Encrypt():
    def formatString(data:str)->bytes:
        final = ""
        for c in data:
            for x in range(4-len(c.encode("utf8"))):
                final += '\0'
            final += c
        return final.encode("utf8")