import subprocess
import random
import os.path
import string
import sys
import cryptography.fernet
import stdiomask as getpass
# Titre stylé 


def generateMasterPass():
    key = cryptography.fernet.Fernet.generate_key()
    with open("./master.key", "wb") as masterPasswordWriter:
        masterPasswordWriter.write(key)

def loadMasterPass():
    return open("./master.key", "rb").read()

def createVault():
    vault = open("./vault.txt", "wb")
    vault.close()

def encryptData (data):
    f = cryptography.fernet.Fernet(loadMasterPass())
    with open("./vault.txt", "rb") as vaultReader:
        encryptedData = vaultReader.read()
    if encryptedData.decode() == '':
        return f.encrypt(data.encode())
    else:
        decryptedData = f.decrypt(encryptedData)
        newData = decryptedData.decode() + data
        return f.encrypt(newData.encode())

def decryptedData(encryptedData):
    f = cryptography.fernet.Fernet(loadMasterPass())
    return f.decrypt(encryptedData)

def appendNewPassword(): 
   
        print()
        userName = input("Vauillez enter un nom d'utilisateur : ")
        password = getpass.getpass(prompt="Veuillez entrer un mot de passe : ", mask="*")
        website = input(" Veuillez entrer un site web : ")
        print()

        
        userNameLine = "Nom d'utilisateur : " + userName + "\n"
        passwordLine = "Mote de passe : "+ password + "\n"
        webSiteLine = "Site web : " + website + "\n"

        encryptedData = encryptData(userNameLine + passwordLine + webSiteLine )

        with open("vault.txt", "wb") as vaultWriter:
         vaultWriter.write(encryptedData)

def readPasswords():
    
    with open("vault.txt","rb") as passwordsReader:
        encryptedData = passwordsReader.read()
    print()
    print(decryptedData(encryptedData).decode())

def generateNewPassWord(passwordLeght):
    randomString = string.ascii_letters + string.digits + string.punctuation
    newPassword =""
    for i in range(passwordLeght):
        newPassword += random.choice(randomString)

        print()
        print(("Voici votre mot de passe : ") + newPassword)

 # Partie principale du programme  
#subprocess.call("clear", shell=True)
import pyfiglet 

result = pyfiglet.figlet_format("--PassWord Manager--")
print(result)
print("_" * 60)
print("**Bienvenue dans PassManager**")
print("_" * 60)

if os.path.exists("./vault.txt") and os.path.exists("./master.key"):

  print(" Vous pouvez selectionner l'une des options suivantes")
  print(" 1 - Sauvegarder un nouveau mot de passe.")
  print("2 - Générer un nouveau mot de pass aléatoire.")
  print("3 - Obtenir la liste des mots de passe.")  

  userChoice = input("Que souhaitez-vous faire ? (1/2/3) ")
  if userChoice == "1":
    appendNewPassword()
  elif userChoice =="2":
    passwordLeght = input("Quelle est la longueur souhaitée pour le mot de passe ? ")
    if not (string.ascii_letters in passwordLeght) :
        generateNewPassWord(int(passwordLeght)) 
    else:
        print(" Merci de rentrer un nombre la prochaine fois...")
        sys.exit()  
  elif userChoice == "3":
    readPasswords()      
  else:
    print("L'option secltionnée n'exite pas")
    sys.exit
else:
    print("Génération d'un nouveau mot de passe maître et d'un coffre de mots de passe...")
    generateMasterPass()
    createVault()
    print("Génération terminée.Veuillez relancer le programme.")
