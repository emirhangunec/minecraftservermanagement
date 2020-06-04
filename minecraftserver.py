#!/usr/bin/env python3
import os
import wget
from time import sleep
from bs4 import BeautifulSoup
import requests
defLoc = os.getcwd()
clear = "clear"
startText = "start.sh"
if os.name =="nt":
    clear = "cls"
    startText = "start.bat"
os.system(clear)
def download(version):
    try:
        soup = BeautifulSoup(requests.get(f"https://mcversions.net/download/{version}").content,"html.parser")
        if soup.title.string =="MCVersions.net - 404 File not found":
            raise ValueError()
        elif soup.title.string ==f"MCVersions.net - Create your own {version} Minecraft server!":
            mydivs = soup.find_all('a', "button")
            link = mydivs[0].get("href")
            wget.download(link)
            print("\nDownload completed successfully.")
    except ValueError:
        print(f"{version} version can't found, make sure to don't mistake.")
    except:
        print("Something went wrong")
def setup(ram):
    if ram.strip().lower().isnumeric():
        try:
            os.system(f'echo java -Xmx{ram}M -Xms{ram}M -jar server.jar nogui > {startText}')
            if not os.name =="nt":
                os.system('chmod +x start.sh')
            print(f"Starting file created successfully with {ram}MB ram.")
            if not os.path.exists('eula.txt'):
                print("Editing eula file.")
                if not os.name == "nt":
                    os.system(f'./{startText}')
                else:
                    os.system(f'{startText}')
                sleep(1)
                os.system('echo eula=true> eula.txt')
                print('Eula edited successfully.')
        except:
            print("Something went wrong")
    else:
        print("Wrong data input, try again.")
def start():
    os.system(clear)
    print("Before run the server, be sure server.properties configured correctly.")
    print("Type 'stop' to stop the server while running.")
    print("Do you want configure the server.properties?")
    while True:
        print("y:yes / n:no")
        editq = input("(y/n): ")
        if editq.strip().lower() == "y":
            if not os.name =="nt":
                os.system("nano server.properties")
            else:
                os.system("notepad server.properties")
            break
        elif editq.strip().lower() == "n":
            print("server.properties file is not edited, continuing.")
            break
        else:
            os.system(clear)
            print("Unidintified answer, try again.")
    print("Server starting in 2 sec.")
    sleep(1)
    print("Server starting in 1 sec.")
    sleep(1)
    os.system(clear)
    if not os.name == "nt":
        os.system(f'./{startText}')
    else:
        os.system(f'{startText}')
def check(version,location):
    while True:
        selectedLoc = location+"/minecraftServers/"+version
        print(f"Searching path: {selectedLoc}")
        if not os.path.exists(selectedLoc):
            print(f"Path not found, creating: {selectedLoc}")
            os.makedirs(selectedLoc)
            print(f"Path created successfully: {selectedLoc}")
        elif os.path.exists(selectedLoc):
            os.chdir(selectedLoc)
            print(f"Path found, locating: {selectedLoc}")
            print(f"Path located successfully: {selectedLoc}")
            print("Searching file in path: server.jar")
            if os.path.exists("server.jar"):
                print("File found: server.jar")
                print(f"Searching file in path: {startText}")
                if os.path.exists(startText):
                    print(f"File found: {startText}")
                    break
                else:
                    print(f"File not found: {startText}")
                    print("Setup is starting.")
                    print("Type ram amount to give server(Default:1024): ")
                    print("Hit enter to use default.")
                    ramInput = input('MB: ')
                    if ramInput.strip().lower().isnumeric():
                        ram = ramInput.strip().lower()
                    else:
                        ram ='1024'
                    os.chdir(selectedLoc)
                    setup(ram)
                    break
            else:
                print("File not found: server.jar")
                print("Searching file in Internet: server.jar")
                download(version)
                print("Setup is starting.")
                print("Type ram amount to give server(Default:1024): ")
                print("Hit enter to use default.")
                ramInput = input('MB: ')
                if ramInput.strip().lower().isnumeric():
                    ram = ramInput.strip().lower()
                else:
                    ram ='1024'
                os.chdir(selectedLoc)
                setup(ram)
    os.chdir(selectedLoc)
    start()
print("Welcome to Minecraft Server Manager.")
print("If you want use defaults, hit enter when asked anything.")
version = ""
while True:
    os.chdir(defLoc)
    print("Type 'q' for quit")
    edita = input("Type the version(Default:1.15.2): ")
    print("Hit enter to use default.")
    if edita.strip().lower() == "q":
        break
    else:
        version = edita.strip().lower() or "1.15.2"
        check(version,defLoc)
