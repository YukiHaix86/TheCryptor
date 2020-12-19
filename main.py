import os, cryptography
from cryptography.fernet import Fernet
import encryp
import key
import sys,time,random
import yukiutils

#key.write_key()
key = key.load_key()
#check if key exists
print("Checking if Key exists...")
#if key.check_key() == True:
 #   print("Key found and checked!")
#else:
 #   print("Attention Key might be broken! You should delete your .key file or select generate new key in the Menu!")

#
str_array = ["Encrypt Message","Decrypt Message","Encrypt File","Decrypt File","Check Key","Generate new Keys","Exit"]
print("What do you want to do?")

i = 0
for x in str_array:
    i += 1
    txt = "{counter1}.| {str_array_output}".format(counter1 = i, str_array_output = x)
    print(txt)
#change to yukiutils
print("You can now choose what you wanna do! (Only numbers from 1-7 accepted!)")
print("")

selectioner = False
while selectioner == False:

   auswahl = input()

   if auswahl.isdigit() == True:
       auswahl = int(auswahl)

       if 1<= auswahl <= 6:
           txt2 = "You selected {auswahl1}.| ".format(auswahl1 = auswahl)
           print(txt2 + str_array[auswahl-1])
           selectioner = True
       elif auswahl == 7:
           print("Goodbye")
           break
       else:
           print("You can only use the numbers 1-7!")
   else:
       print("You can only use the numbers 1-7!")

#Dictionary for Selection

auswahl -= 1

if auswahl == 0:
    msg = input("Write your message to encrypt\n").encode()
    newmessage = encryp.encryptmessage(msg, key)
    print(newmessage)

elif auswahl == 1:
    msg = input("Write message to decrypt\n").encode()
    newmessage = encryp.decryptmessage(msg, key)
    print(newmessage)
else:
    print("Something went wrong")