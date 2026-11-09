
from pathlib import Path
import os

def createfile():
    try:
        name = input("enter file name:- ")
        file_path = Path(name)  #checking if file exists or not 
        if not file_path.exists():
            with open(file_path,"w") as fs:
                data = input("enter what you want to write:- ")
                fs.write(data)
            print("file created successfully")
        else:
            print("file name already exists")
    except Exception as err:
        print(f"an error occured as {err}")

def readfile():
    try:
        name = input("enter file name :-")
        file_path = Path(name)
        if file_path.exists():
            with open(file_path,"r") as fs:
                content = fs.read()
                print(f"\nyour file content is {content}")
        else:
            print("error no file found: ")
    except Exception as err:
        print(f'an error occured as {err}')

def updatefile():
    try:
        name = input("enter file name :-")
        file_path = Path(name)
        if file_path.exists():
            print("operations")
            print("1. renaming the file")
            print("2. appending the file")
            print("3. overwriting the file ")

            choice = int(input("enter your option"))
            if choice == 1:
                newname = input("enter new file name: ")
                new_path = Path(newname)
                if not new_path.exists():
                    file_path.rename(new_path)
                    print("renamed successfully")
                else:
                    print("file already exists ")

            elif choice == 2:
                with open(file_path,"a") as fs:
                    data = input("what do you want to append  ")
                    fs.write("\n"+data)
                print("appended successfully ")

            elif choice == 3:
                with open(file_path,"w") as fs:
                    data = input("what do you want to append  ")
                    fs.write("\n"+data)
                print("overwritten successfully ")
    except Exception as err:
        print(f"error occured as {err}")



def deletefile():
    try:
        name = input("enter your file name :")
        file_path = Path(name)
        if file_path.exists():
            file_path.unlink()
            print("file deleted successfully")
        else:
            print("no such file found")
    except Exception as err:
        print(f"error occured as {err}")



print("press 1 for creating the file: ")
print("press 2 for reading the file: ")
print("press 3 for updating the file: ")
print("press 4 for deleting the file: ")

a = int(input('\nenter your response'))

if a == 1:
    createfile()

if a == 2:
    readfile()

if a == 3:
    updatefile()

if a == 4:
    deletefile()