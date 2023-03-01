from enum import Enum
from abc import ABC, abstractmethod



class Encrypt():
    def formatString(self, data:str)->bytes:
        final = ""
        for c in data:
            final += '   ' + c
        return final.encode("utf8")