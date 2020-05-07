# EN
## Information
This mini-program/script helps you to creating self-hosted minecraft servers. Just open 25565 port on your router or use Hamachi and run this script. Then follow the instructions in terminal correctly and don't forget to edit server.properties.
This python3 script for linux works correctly and windows.
- Script automatically downloads, sets with written ram amount and runs to written version of minecraft server.
- If server alredy downloaded, script sets with written ram amount and runs to written version of minecraft server.
- If server alredy downloaded and setted, script runs to written version of minecraft server.
## Installation
#### For Linux:
- Install the dependencies and change permissions to be executable in terminal.
```sh
sudo apt-get install python3
  ```
  ```sh
  sudo apt-get install python3-pip
  ```
  ```sh
  pip install --upgrade pip
  ```
  ```sh
  pip install -r requirements.txt
  ```
   ```sh
  chmod +x minecraftserver.py
  ```
#### For Windows:
- Download and install python3: https://www.python.org/downloads/release/python-382/
- run cmd, go to folder  'minecraftservermanagement' and paste these:
  ```sh
  python -m pip install --upgrade pip
  ```
  ```sh
   python -m pip install -r requirements.txt
  ```

## Usage/Run
  #### For Linux:
  - Go to folder  'minecraftservermanagement' and run this:
   ```sh
  ./minecraftserver.py
  ```
  #### For Windows:
  - Go to folder  'minecraftservermanagement' and run this:
   ```sh
  python minecraftserver.py
  ```
  ---
  # TR
  ## Bilgilendirme
Bu mini-program/script self-hosted minecraft serverlarını otomatik olarak oluşturmaya ve yönetmeye yarar. İster modeminizde 25565 portunu açarak, ister Hamachi kullanarak çok hızlı ve basit bir şekilde server oluşturabilirsiniz. Sadece terminalde verilen yönlendirmeleri dikkatlice takip edin ve 'server.properties' dosyasını düzgünce ayarlayın.
Bu pythno3 scripti belirtilen işletim sistemlerinde doğru bir şekilde çalışır: LINUX/WİNDOWS
- Script seçtiğiniz versiyondaki server dosyalarını otomatik olarak indirir, sizin belirlediğniz ram miktarıyla birlikte kurar ve çalıştırır.
- Eğer dosyalar daha önce indirilmişse, sizin belirlediğniz ram miktarıyla birlikte kurar ve çalıştırır.
- Eğer dosyalar daha önce indirilmiş ve kurulmuşsa, seçtiğiniz sürümdeki serverı çalıştırır.
## Kurulum
#### Linux için:
- Gereklilikleri yükleyin ve dosyayı çalıştırılabilir moda getirin:
```sh
sudo apt-get install python3
  ```
  ```sh
  sudo apt-get install python3-pip
  ```
  ```sh
  pip install --upgrade pip
  ```
  ```sh
  pip install -r requirements.txt
  ```
   ```sh
  chmod +x minecraftserver.py
  ```
#### Windows için:
- python3 indirin ve kurun: https://www.python.org/downloads/release/python-382/
  
- Komut istemcisini çalıştırın ve 'minecraftserver.py' dosyasının bulunduğu konuma gidin. Ardından yapıştırın:
  ```sh
  python -m pip install --upgrade pip
  ```
  ```sh
   python -m pip install -r requirements.txt
  ```

## Kullanım/Çalıştırma
  #### Linux için:
  - 'minecraftserver.py' dosyasının bulunduğu konuma gidin, ardından çalıştırın:
   ```sh
  ./minecraftserver.py
  ```
  #### Windows için:
  - 'minecraftserver.py' dosyasının bulunduğu konuma gidin, ardından çalıştırın:
   ```sh
  python minecraftserver.py
  ```
