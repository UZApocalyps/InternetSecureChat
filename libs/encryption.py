from enum import Enum

class EncryptionTypes(Enum):
    TEST1 = 1


class Encryption:
    encryptionType: EncryptionTypes = None

    @classmethod
    def encrypt(self, method:EncryptionTypes):
        if(method.name == EncryptionTypes.TEST1):
            print("Encrypthing with test1")
        else:
            print("Couldn't find a encryption matching with the requirements")

    def __init__(self, method:EncryptionTypes):
        self.encryptionType = method

    def encrypt(self, data) -> bytes:
        # Check type needed and encrypt with it
        return data
