#!/usr/bin/python
#
# quick installer for SET
#
#
from __future__ import print_function
import subprocess
import os
print("[*] Установка require.txt...")
subprocess.Popen("pip3 install -r requirements.txt", shell=True).wait()
print("[*] Установка setoolkit в / usr / share / setoolkit..")
print(os.getcwd())
subprocess.Popen("mkdir /usr/share/setoolkit/;mkdir /etc/setoolkit/;cp -rf * /usr/share/setoolkit/;cp src/core/config.baseline /etc/setoolkit/set.config", shell=True).wait()
print("[*] Создание лаунчера для сетоолкитов...")
filewrite = open("/usr/local/bin/setoolkit", "w")
filewrite.write("#!/bin/sh\ncd /usr/share/setoolkit\n./setoolkit")
filewrite.close()
print("[*] Готово. Chmoding +x.... ")
subprocess.Popen("chmod +x /usr/local/bin/setoolkit", shell=True).wait()
print("[*] Законченный. Запустите setoolkit, чтобы запустить инструментарий Social Engineer..")
