import cryptography
from cryptography.fernet import Fernet


def encryptfile(fname, key):
    f = Fernet(key)
    with open(fname, "rb") as file:
        file_data = file.read()

    encryptedfile = f.encrypt(file_data)
    with open(fname, "wb") as file:
        file.write(encryptedfile)

def decryptfile(fname, key):
    f = Fernet(key)
    with open(fname, "rb") as file:
        encrypted_data = file.read()
    decryptdata = f.decrypt(encrypted_data)
    with open(fname, "wb") as file:
        file.write(decryptdata)



def encryptmessage(msg, key):
    f = Fernet(key)
    encryptedmsg = f.encrypt(msg)
    return encryptedmsg

def decryptmessage(msg, key):
    f = Fernet(key)
    decrypted = f.decrypt(msg)
    return decrypted
