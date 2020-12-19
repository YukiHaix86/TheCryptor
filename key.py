import cryptography
import os.path
import shutil
from shutil import copyfile
from os import path
from cryptography.fernet import Fernet


def write_key():
    key = Fernet.generate_key()
    with open("schluessel.key", "wb") as key_file:
        key_file.write(key)
    copyfile("schluessel.key", "debug.dat")
    os.system( "attrib +h debug.dat" )

def load_key():
    return open("schluessel.key", "rb").read()


#Checks invisble file if the keys match.. pretty dumb idea but idc xd its just for fun
def check_key():
    if path.exists("schluessel.key"):
        copiedkey = open("schluessel.key", "rb").read()
        securedkey = open("debug.dat", "rb").read()

    if copiedkey == securedkey:
        return True

    elif copiedkey != securedkey:
        return False