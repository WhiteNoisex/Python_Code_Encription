# MADE BY WHITE-NOISE 
# NO CHANGES OR COPYRIGHT ALOWED

import os
import sys

if(os.path.isdir(r'keys/') == False):
    prompt = input("First Time Setup Press Enter To Continue or q to exit: ")
    if(prompt == ""):
        prompt2 = input("instaling cryptography.fernet FROM PIP PRESS Enter to continue or q to stop: ")
        if(prompt == ""):
            os.system("pip install cryptography")
        else:
            sys.exit()
    else:
        sys.exit()





import random
from multiprocessing.connection import wait

from tkinter import W, Variable
from cryptography.fernet import Fernet

difsalt = ''


def write_key(keyfile):
    key = Fernet.generate_key()
    with open("keys/"+keyfile, "wb+") as key_file:
        key_file.write(key)

def load_key(keynum):
    file = open("keys/"+keynum, "rb")
    key = file.read()
    file.close()
    return key

if(os.path.isdir(r'keys/') == True):
    key2 = load_key("key2.key")
    fer2 = Fernet(key2)

    key = load_key("key1.key")
    fer = Fernet(key)

    key3 = load_key("key3.key")
    fer3 = Fernet(key3)

    key4 = load_key("key4.key")
    fer4 = Fernet(key4)
else:
    os.mkdir(os.path.dirname(__file__) + "\keys")
    random_string = ''
    for _ in range(500000):
        random_integer = random.randint(97, 97 + 26 - 1)
        flip_bit = random.randint(0, 1)
        random_integer = random_integer - 32 if flip_bit == 1 else random_integer
        random_string += (chr(random_integer))
    with open("keys/salt.salt","w+")as f:
        f.write(random_string)
        pass

    write_key("key4.key")
    write_key("key3.key")
    write_key("key2.key")
    write_key("key1.key")


if(os.path.isdir(r'encrypted_scripts/') == True):
    pass
else:
    os.mkdir(os.path.dirname(__file__) + "\encrypted_scripts")
    os.system("cls")
    os.system('color 4')
    print("/\/\/\/\ Reboot Script Now /\/\/\/\ ")
    prompt4 = input("Press Enter To Close Script:"+"\n")
    if(prompt4 != ""):
        os.system('python compiler.py')
        sys.exit()
    sys.exit()
    
with open("keys/salt.salt","r")as s: #salt
        salt = s.read() .encode().decode()



def add():
    CodeDIR = input("code NAME: ")
    codeDIR2,filename1 = CodeDIR.split(".")
    with open(CodeDIR,"r") as f:
        code = f.read()

    with open("encrypted_scripts/"+ codeDIR2+'.encr', 'a') as f:
        f.write(ency(code)+"|"+salt)

def view():
    codeDIR2 = input("code NAME: ")
    with open("encrypted_scripts/"+ codeDIR2 + ".encr" , 'r') as f:
        code = f.read()
        codeaf,salt = code.split("|")
        
        codedf = codeDIR2 + ".py"

        exec(dncy(codeaf))
      
def ency(variable):

    pwd4= fer.encrypt(variable.encode()).decode()
    pwd3 = fer2.encrypt(pwd4.encode()).decode()
    pwd2 = fer3.encrypt(pwd3.encode()).decode()
    return  fer4.encrypt(pwd2.encode()).decode()

def dncy(variable):

    pwd4= fer4.decrypt(variable.encode()).decode()
    pwd3 = fer3.decrypt(pwd4.encode()).decode()
    pwd2 = fer2.decrypt(pwd3.encode()).decode()
    return  fer.decrypt(pwd2.encode()).decode()




while True:
    mode = input(
        "Would you like to encrypt a script or view existing ones (view, add), press q to quit? ").lower()
    if mode == "q":
        break
 
    if mode == "view":
        view()
    elif mode == "add":
        add()
    elif mode == "gen_keys":
        write_key("key4.key")
        write_key("key3.key")
        write_key("key2.key")
        write_key("key1.key")
        pass
       # run()
    else:
        print("Invalid mode.")
        continue
