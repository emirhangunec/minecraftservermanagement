#!/usr/bin/env python3
import os
import wget
from time import sleep
from bs4 import BeautifulSoup
import requests
if os.name =="posix":
    os.system("clear")
    defLoc = os.getcwd()
    print("OS detected: Linux")
    print("Welcome to Minecraft Server Manager .")
    def download(version,location):
        try:
            r = requests.get(f"https://mcversions.net/download/{version}")
            soup = BeautifulSoup(r.content,"html.parser")
            if soup.title.string =="MCVersions.net - 404 File not found":
                print(f"{version} can't found, make sure to don't mistake.")
            elif soup.title.string ==f"MCVersions.net - Create your own {version} Minecraft server!":  
                mydivs = soup.find_all('a', "button")
                link = mydivs[0].get("href")
                print("server.jar başarıyla bulundu, indirme işlemi başlayacak.")
                wget.download(link)
                print("\nIndirme işlemi başarıyla tamamlandı.")
                print("Kuruluma geçiliyor.")
                print("Server için ayıracağınız ram miktarını giriniz(Varsayılan olarak 1024 ayarlıdır): ")
                secilenram = input('MB: ') or '1024'
                kur(secilenram)
            else:
                print("tanımlanamayan hata")
        except:
            print("tanımlanamayan hata")
        
    def kur(ram):
        if ram.strip().lower().isnumeric():
            os.system('echo #!/bin/bash > start.sh')
            os.system(f'echo java -Xmx{ram}M -Xms{ram}M -jar server.jar nogui > start.sh ')
            os.system('chmod +x start.sh')
            print(f"{ram}MB ram ile server başlatma dosyası başarıyla oluşturuldu.")
            os.system('./start.sh')
            sleep(2)
            os.system('echo eula=true > eula.txt')
            print('eula başarıyla düzenlendi.')
            baslat()
            


        else:
            print("Hatalı veri girişi, tekrar deneyiniz.")

    def baslat():
        print("Serveri başlatmadan önce, server.properties dosyanızı ayarladığınızdan emin olun.")
        print("Server çalışırken durdurmak için stop yazın.")
        print("server.properties dosyasını düzenlemek ister misiniz?")
        onay4 = input("(E/H): ")
        if onay4.strip().lower() == "e":
            os.system("clear")
            os.system("nano server.properties")
        elif onay4.strip().lower() == "h":
            os.system('clear')
            print("server.properties düzenlenmedi devam ediliyor.")
        else:
            os.system("clear")
            print("Tanımlanmayan cevap, Sürüm seçimine dönülüyor.")
        print("Server başlatılacak, onaylıyor musunuz?")
        onay3 = input("(E/H): ")
        if onay3.strip().lower() == "e":
            os.system("clear")
            os.system("./start.sh")
        elif onay3.strip().lower() == "h":
            os.system('clear')
            print("Server başlatılmadı, geri dönülüyor.")
        else:
            os.system("clear")
            print("Tanımlanmayan cevap, Sürüm seçimine dönülüyor.")
        
    while True:
        os.chdir(defLoc)
        version = ""
        SurumInput = input("Çıkmak için:'quit'".center(30) +"\nLütfen sürüm seçiniz örn(1.15.2): ")
        if SurumInput == "quit":
            os.system("clear")
            break
        elif SurumInput.isalpha():
            os.system("clear")
            print("Hatalı sürüm seçimi, lütfen tekrar deneyiniz. Çıkmak için 'quit'. ")
        else:
            surumparcali = SurumInput.strip().lower().split(".")
            for parca in surumparcali:
                if parca.isnumeric() and len(surumparcali)<=3 and len(surumparcali) > 2:
                    if surumparcali.index(parca) == len(surumparcali) -1:
                        version += parca
                    else:
                        version += parca + "."
                else:
                    os.system("clear")
                    print("Hatalı sürüm seçimi, lütfen tekrar deneyiniz. Çıkmak için 'quit'. ")
                    break
            print(f"{version} sürümü için işlem başlatılacak, onaylıyor musunuz?")
            onay = input("(E/H): ")
            if onay.strip().lower() == "h":
                os.system("clear")
                print("Sürüm seçimine dönülüyor.") 
            elif onay.strip().lower() == "e":
                secilenKonum = os.getcwd()+"/minecraftServers/"+version
                print(f"Konum: {secilenKonum}")
                if not os.path.exists(secilenKonum):
                    os.makedirs(secilenKonum)
                    print(f"{secilenKonum} konumu başarıyla yaratıldı.")
                os.chdir(secilenKonum)
                print(f"konuma gidildi: {secilenKonum}")
                print("server.jar klasörde aranıyor.")
                if not os.path.exists("server.jar"):
                    print("server.jar klasörde bulunamadı, internette aranıyor.")
                    download(version,secilenKonum)
                elif os.path.exists("server.jar"):
                    print("server.jar zaten yüklü, kuruluma geçiliyor.")
                    if os.path.exists("start.sh"):
                        print("Başlatma dosyası bulundu, server başlatılıyor.")
                        baslat()
                    elif not os.path.exists("start.sh"):
                        print("Başlatma dosyası bulunamadı,server kuruluyor.")
                        print("Server için ayıracağınız ram miktarını giriniz(MB): ")
                        secilenram = input('MB: ') or '1024'
                        kur(secilenram)   
            else:
                os.system("clear")
                print("Tanımlanmayan cevap, Sürüm seçimine dönülüyor.")
elif os.name =="nt":
    print("Işletim sistemi tespit edildi: Windows")