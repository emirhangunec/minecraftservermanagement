## Information
This mini-program/script helps you to creating self-hosted minecraft servers. Just open 25565 port on your router or use Hamachi and run this script. Then follow the instructions in terminal correctly and don't forget to edit server.properties.
This python3 script for linux works correctly and windows.
- Script automatically downloads, sets with written ram amount and runs to written version of minecraft server.
- If server alredy downloaded, script sets with written ram amount and runs to written version of minecraft server.
- If server alredy downloaded and setted, script runs to written version of minecraft server.
## Installation
Install the dependencies and change permissions to be executable in terminal.
#### For Linux:
```sh
sudo apt-get install python3
  ```
  ```sh
  sudo apt-get install python3-pip
  ```
  ```sh
  pip install wget
  ```
  ```sh
  pip install beautifulsoup4
  ```
  ```sh
  pip install requests
  ```
   ```sh
  chmod +x minecraftserver.py
  ```
#### For Windows:
- install python3
- run cmd and paste these:
  ```sh
  python -m pip install wget
  ```
  ```sh
  python -m pip install beautifulsoup4
  ```
  ```sh
  python -m pip install requests
  ```

## Usage/Run
  #### For Linux:
   ```sh
  ./minecraftserver.py
  ```
  #### For Windows:
   ```sh
  python minecraftserver.py
  ```
## Todos
 - gui

