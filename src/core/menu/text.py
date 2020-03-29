#!/usr/bin/env python
########################################################################
#
# text menu for set menu stuff
#
########################################################################
from src.core.setcore import bcolors, get_version, check_os, meta_path

# grab version of SET
define_version = get_version()

# check operating system
operating_system = check_os()

# grab metasploit path
msf_path = meta_path()

PORT_NOT_ZERO = "Port cannot be zero!"
PORT_TOO_HIGH = "Let's stick with the LOWER 65,535 ports..."

main_text = " Выберите из меню:\n"

main_menu = ['Социальная инженерия',
             'Тест на проникновение (Ускоренная проверка)',
             'Сторонние модули',
             'Обновите инструментарий Social-Engineer',
             'Обновить конфигурацию SET',
             'Помощь, Кредиты ']

main = ['Векторы Spear-Phishing Attack',
        'Векторы атаки на сайт',
        'Генератор инфекционных медиа',
        'Создать полезную нагрузку и прослушиватель',
        'Массовая почта',
        'Вектор атаки на основе Arduino',
        'Вектор атаки беспроводной точки доступа',
        'Вектор атаки генератора QRCode',
        'Векторы атаки Powershell',
        'Сторонние модули']

spearphish_menu = ['Провести массовую атаку по электронной почте',
                   'Создать FileFormat Payload',
                   'Создать шаблон социальной инженерии',
                   '0D']

spearphish_text = ("""
Модуль """+ bcolors.BOLD +""" Подводная охота """+ bcolors.ENDC +""" позволяет специально создавать сообщения электронной почты и отправлять
 их для большого (или небольшого) количества людей с прикрепленным файлом
 Полезная нагрузка. Если вы хотите подделать свой адрес электронной почты, убедитесь, что «Sendmail»
 остановился (apt-get install sendmail) и изменил config / set_config SENDMAIL = OFF
 флаг для SENDMAIL = ON.

 Есть два варианта, один - намокнуть и позволить SET сделать
 все для вас (вариант 1), второе - создать свой собственный FileFormat
 полезной нагрузки и использовать его в своей собственной атаке. В любом случае, удачи и наслаждайтесь!
""")

webattack_menu = ['Метод атаки Java-апплета',
                  'Метод эксплойта в браузере Metasploit',
                  'Метод Атаки Жатки Учетных данных',
                  'Метод атаки на вкладках',
                  'Метод веб-атаки',
                  'Multi-Attack Web Method',
                  'Метод атаки HTA',
                  '0D']

fasttrack_menu = ['Microsoft SQL Bruter',
                  'Пользовательские эксплойты',
                  'Вектор атаки SCCM',
                  'Dell DRAC / шасси по умолчанию для проверки',
                  'RID_ENUM - Атака перечисления пользователей',
                  'PSEXEC Powershell для инъекций',
                  '0D']

fasttrack_text = ("""
Добро пожаловать в набор инструментов для социальных инженеров - """+ bcolors.BOLD +""" Платформа ускоренного тестирования на проникновение """+ bcolors.ENDC +""". Эти векторы атаки
иметь ряд эксплойтов и аспектов автоматизации, чтобы помочь в искусстве тестирования на проникновение. ЗАДАВАТЬ
теперь включает в себя векторы атаки, используемые в Fast-Track. Все эти векторы атаки были
полностью переписан и настроен с нуля, чтобы улучшить функциональность и возможности.
""")
fasttrack_exploits_menu1 = ['MS08-067 (Win2000, Win2k3, WinXP)',
                            'Использование объекта Mozilla Firefox 3.6.16 mChannel после бесплатного использования (Win7)',
                            'Solarwinds Storage Manager 5.1.0 Эксплойт для удаленной системы SQL-инъекций',
                            'RDP | Использовать после бесплатного - отказ в обслуживании',
                            'Эксплойт обхода аутентификации MySQL',
                            'F5 обход обхода аутентификации root',
                            '0D']

fasttrack_exploits_text1 = ("""
Добро пожаловать в инструментарий Social-Engineer - ускоренное тестирование на проникновение """+ bcolors.BOLD +""" Раздел об уязвимостях """+ bcolors.ENDC +""". Эта
Меню имеет неясные эксплойты и те, которые в основном управляются на Python. Это будет продолжать расти со временем.""")

fasttrack_mssql_menu1 = ['Сканирование и атака MSSQL',
                         'Подключайтесь напрямую к MSSQL',
                         '0D']

fasttrack_mssql_text1 = ("""
Добро пожаловать в набор инструментов Social-Engineer - ускоренное тестирование на проникновение """+ bcolors.BOLD +""" Microsoft SQL Brute Forcer """+ bcolors.ENDC +""". Эта
Вектор атаки будет пытаться идентифицировать живые MSSQL-серверы и перебирать слабые пароли учетных записей, которые
может быть найден Если это произойдет, SET затем скомпрометирует уязвимую систему, развернув двоичный файл для
шестнадцатеричный вектор атаки, который возьмет необработанный двоичный файл, преобразует его в шестнадцатеричный и использует поэтапный подход
при развертывании шестнадцатеричной формы двоичного файла на базовую систему. На данный момент, триггер произойдет
преобразовать полезную нагрузку обратно в двоичный файл для нас.""")

webattack_text = ("""
Модуль Web Attack - это уникальный способ использования множества сетевых атак для компрометации предполагаемой жертвы.

Метод """+ bcolors.BOLD +""" Атака Java-апплета """+ bcolors.ENDC +""" подделывает сертификат Java и доставляет полезную нагрузку, основанную на метасплоте. Использует настроенный Java-апплет, созданный Томасом Вертом для доставки полезной нагрузки.

Метод """+ bcolors.BOLD +""" Использование браузера Metasploit """+ bcolors.ENDC +""" будет использовать некоторые действия браузера Metasploit через iframe и доставит полезную нагрузку Metasploit.

Метод """+ bcolors.BOLD +""" Учетные данные """+ bcolors.ENDC +""" будет использовать веб-клонирование веб-сайта с полем имени пользователя и пароля и собирать всю информацию, размещенную на интернет сайт.

Метод """+ bcolors.BOLD +""" TabNabbing """+ bcolors.ENDC +""" будет ожидать перехода пользователя на другую вкладку, а затем обновит страницу до чего-то другого.

Метод """+ bcolors.BOLD +""" Web-Jacking Attack """+ bcolors.ENDC +""" был представлен white_sheep, emgent. Этот метод использует замены iframe, чтобы выделенная URL-ссылка выглядела легитимной, однако при нажатии всплывающее окно затем заменяется вредоносной ссылкой. Вы можете редактировать параметры замены ссылки в set_config, если он слишком медленный / быстрый.

Метод """+ bcolors.BOLD +""" Multi-Attack """+ bcolors.ENDC +""" добавляет комбинацию атак через меню веб-атаки. Например, вы можете использовать Java-апплет, Metasploit Browser, Credential Harvester / Tabnabbing одновременно, чтобы увидеть, что успешно.

Метод """+ bcolors.BOLD +""" Атака HTA """+ bcolors.ENDC +""" позволит вам клонировать сайт и выполнить инъекцию PowerShell через файлы HTA, которые можно использовать для использования PowerShell на базе Windows. через браузер.
""")

webattack_vectors_menu = ['Веб-шаблоны',
                          'Сайт Клонер',
                          'Пользовательский импорт\n',
                          ]

webattack_vectors_text = ("""
Первый метод позволит SET импортировать список предопределенных веб-страниц.
 приложения, которые он может использовать в рамках атаки.

 Второй метод полностью клонирует веб-сайт по вашему выбору
 и позволяют использовать векторы атаки в рамках полностью
 то же самое веб-приложение, которое вы пытались клонировать.

 Третий метод позволяет импортировать ваш собственный сайт, обратите внимание, что вы
 должен иметь только index.html при использовании сайта импорта
 функциональность.
   """)

teensy_menu = ['Powershell HTTP GET Полезная нагрузка MSF',
               'WSCRIPT HTTP GET Полезная нагрузка MSF',
               'Основанная на Powershell обратная оболочка полезной нагрузки',
               'Internet Explorer / FireFox Beef Jack Полезная нагрузка',
               'Перейти на вредоносный сайт Java и принять апплет полезной нагрузки',
               'Gnome wget Скачать полезную нагрузку',
               'Binary 2 Teensy Attack (развертывание полезных нагрузок MSF)',
               'SDCard 2 Teensy Attack (разверните любой EXE)',
               'SDCard 2 Teensy Attack (Развертывание на OSX)',
               'X10 Arduino Sniffer PDE и библиотеки',
               'X10 Arduino Jammer PDE и библиотеки',
               'Powershell Direct ShellCode Teensy Attack',
               'DIP-переключатель Peensy Multi Attack + SDCard Attack',
	       'HID Msbuild скомпилировать в память Shellcode Attack',
               '0D']

teensy_text = ("""
Вектор """+ bcolors.BOLD +""" Arduino-Attack """+ bcolors.ENDC +""" Vector использует устройство на основе Arduin для
 запрограммируйте устройство. Вы можете использовать Teensy's, которые имеют на борту
 хранения и может позволить удаленное выполнение кода на физическом
 система. Поскольку устройства зарегистрированы как клавиатура USB, это
 будет обходить любой отключенный автозапуск или защиту конечной точки на
 система.

 Вам нужно будет купить USB-устройство Teensy, оно примерно
 22 доллара Этот вектор атаки будет автоматически генерировать код
 необходим для того, чтобы развернуть полезную нагрузку в системе для вас.

 Этот вектор атаки создаст файлы .pde, необходимые для импорта.
 в Arduino (IDE используется для программирования Teensy). Атака
 векторы варьируются от загрузчиков на основе Powershell, атак на wscript,
 и другие методы.

 Для получения дополнительной информации о спецификациях и хороших учебниках посетите:

 http://www.irongeek.com/i.php?page=security/programmable-hid-usb-keystroke-dongle

 Чтобы купить Teensy, посетите: http://www.pjrc.com/store/teensy.html
 Особая благодарность: IronGeek, WinFang и Garland

 Этот вектор атаки также атакует контроллеры на базе X10, обязательно используйте
 Устройства связи на основе X10, чтобы это работало.

 Выберите полезную нагрузку, чтобы создать файл pde для импорта в Arduino:""")

wireless_attack_menu = ['Запустить беспроводную точку доступа SET Wireless Vector',
                        'Остановите точку доступа SET Wireless Attack Vector',
                        '0D']


wireless_attack_text = """
 Модуль """+ bcolors.BOLD +""" Беспроводная атака """+ bcolors.ENDC +""" создаст точку доступа, использующую ваш
 беспроводную карту и перенаправить все DNS-запросы к вам. Концепция довольно
 просто, SET создаст беспроводную точку доступа, dhcp-сервер и обман
 DNS для перенаправления трафика на компьютер злоумышленника. Затем он выйдет
 этого меню со всем, что работает как дочерний процесс.

 Затем вы можете запустить любой вектор атаки SET, например, Java
 Атака апплетов и когда жертва присоединяется к вашей точке доступа и пытается
 веб-сайт, будет перенаправлен на ваш компьютер атакующего.

 Этот вектор атаки требует AirBase-NG, AirMon-NG, DNSSpoof и dhcpd3.

"""

infectious_menu = ['Эксплойты формата файла',
                   'Стандартный исполняемый файл Metasploit',
                   '0D']


infectious_text = """
Модуль """+ bcolors.BOLD + bcolors.GREEN +""" Инфекционный """+ bcolors.ENDC +""" USB / CD / DVD создаст файл autorun.inf и
 Полезная нагрузка Metasploit. Когда DVD / USB / CD вставлен, он будет автоматически
 запустить, если автозапуск включен. """+ bcolors.ENDC +"""

 Выберите вектор атаки, который вы хотите использовать: ошибки формата файла или прямой исполняемый файл.
"""

# used in create_payloads.py
if operating_system != "windows":
    if msf_path != False:
        payload_menu_1 = [
            'Инъекция памяти Meterpreter (DEFAULT) Это снизит полезную нагрузку Meterpreter за счет инъекции PowerShell.',
            'Meterpreter Multi-Memory Injection Это позволит сбросить несколько полезных нагрузок Metasploit с помощью PowerShell.',
            'SE Toolkit Interactive Shell Пользовательский интерактивный обратный инструментарий, разработанный для SET',
            'SE Toolkit HTTP Reverse Shell Чисто собственная HTTP-оболочка с поддержкой шифрования AES',
            'RATTE HTTP Tunneling Payload Безопасность обходной нагрузки, которая будет туннелировать все соединения через HTTP',
            'ShellCodeExec Alphanum Shellcode Это сбросит полезную нагрузку метра-интерпретатора через shellcodeexec',
            'Импортируйте свой собственный исполняемый файл. Укажите путь для своего собственного исполняемого файла.',
            'Импортируйте свои собственные команды .txt Укажите полезные данные, которые будут отправлены через командную строку.\n']

if operating_system == "windows" or msf_path == False:
    payload_menu_1 = [
        'SE Toolkit Interactive Shell    Custom interactive reverse toolkit designed for SET',
        'SE Toolkit HTTP Reverse Shell   Purely native HTTP shell with AES encryption support',
        'RATTE HTTP Tunneling Payload    Security bypass payload that will tunnel all comms over HTTP\n']

payload_menu_1_text = """
Какую полезную нагрузку вы хотите создать:

  Name:                                       Description:
"""

# used in gen_payload.py
payload_menu_2 = [
    'Windows Shell Reverse_TCP               Создайте командную оболочку на жертве и отправьте обратно злоумышленнику',
    'Windows Reverse_TCP Meterpreter         Создайте снаряд метра-препон на жертву и отправьте обратно злоумышленнику',
    'Windows Reverse_TCP VNC DLL             Создайте сервер VNC на жертве и отправьте обратно злоумышленнику',
    'Windows Shell Reverse_TCP X64           Командная оболочка Windows X64, обратный TCP, встроенный',
    'Windows Meterpreter Reverse_TCP X64     Подключитесь обратно к атакующему (Windows x64), Meterpreter',
    'Windows Meterpreter Egress Buster       Создайте оболочку meterpreter и найдите порт через несколько портов',
    'Windows Meterpreter Reverse HTTPS       Туннельная связь по HTTP с использованием SSL и использование Meterpreter',
    'Windows Meterpreter Reverse DNS         Используйте имя хоста вместо IP-адреса и используйте Reverse Meterpreter',
    'Download/Run your Own Executable        Загружает исполняемый файл и запускает его\n'
]


payload_menu_2_text = """\n"""

payload_menu_3_text = ""
payload_menu_3 = [
    'Windows Reverse TCP Shell              Создайте командную оболочку на жертве и отправьте обратно злоумышленнику',
    'Windows Meterpreter Reverse_TCP        Создайте снаряд метра-препон на жертву и отправьте обратно злоумышленнику',
    'Windows Reverse VNC DLL                Создайте сервер VNC на жертве и отправьте обратно злоумышленнику',
    'Windows Reverse TCP Shell (x64)        Командная оболочка Windows X64, обратный TCP, встроенный',
    'Windows Meterpreter Reverse_TCP (X64)  Подключитесь обратно к атакующему (Windows x64), Meterpreter',
    'Windows Shell Bind_TCP (X64)           Выполните полезную нагрузку и создайте принимающий порт в удаленной системе',
    'Windows Meterpreter Reverse HTTPS      Туннельная связь по HTTP с использованием SSL и использование Meterpreter\n']

# called from create_payload.py associated dictionary = ms_attacks
create_payloads_menu = [
    'SET Custom Written DLL Вектор перехвата атаки (RAR, ZIP)',
    'SET Custom письменный документ UNC LM SMB Capture Attack',
    'MS15-100 Microsoft Windows Media Center Уязвимость MCL',
    'MS14-017 Microsoft Word RTF объект путаницы (2014-04-01)',
    'Microsoft Windows CreateSizedDIBSECTION Переполнение буфера в стеке',
    'Microsoft Word RTF pFragments Sпереполнение буфера прихвата (MS10-087)',
    'Adobe Flash Player «Кнопка» Удаленное выполнение кода',
    'Adobe CoolType SING Table "uniqueName" Переполнение',
    'Неверное использование указателя в Adobe Flash Player "newfunction"',
    'Переполнение буфера в Adobe Collab.collectEmailInfo',
    'Переполнение буфера в Adobe Collab.getIcon',
    'Adobe JBIG2Используйте эксплойт для повреждения памяти',
    'Adobe PDF Embedded EXE Социальная инженерия',
    'Adobe util.printf () Переполнение буфера',
    'Пользовательский EXE в VBA (отправляется через RAR) (требуется RAR)',
    'Adobe U3D CLODProgressiveMeshDeclaration Массив переполнен',
    'Adobe PDF Embedded EXE Социальная инженерия (NOJS)',
    'Foxit PDF Reader v4.1.1 Переполнение буфера в стеке заголовков',
    'Переполнение буфера в Apple QuickTime PICT PnSize',
    'Переполнение буфера в стеке при запуске Nuance PDF Reader v6.0',
    'Уязвимость Adobe Reader u3D, приводящая к повреждению памяти',
    'Переполнение буфера в ActiveX MSCOMCTL (ms12-027)\n']

create_payloads_text = """
Выберите нужный вам формат файла.
 По умолчанию используется PDF EXE.\n
           ********** PAYLOADS **********\n"""

browser_exploits_menu = [
    'Adobe Flash Player ByteArray Use After Free (2015-07-06)',
    'Adobe Flash Player Nellymoser Audio Decoding Buffer Overflow (2015-06-23)',
    'Adobe Flash Player Drawing Fill Shader Memory Corruption (2015-05-12)',
    'MS14-012 Microsoft Internet Explorer TextRange Use-After-Free (2014-03-11)',
    'MS14-012 Microsoft Internet Explorer CMarkup Use-After-Free (2014-02-13)',
    'Internet Explorer CDisplayPointer Use-After-Free (10/13/2013)',
    'Micorosft Internet Explorer SetMouseCapture Use-After-Free (09/17/2013)',
    'Java Applet JMX Remote Code Execution (UPDATED 2013-01-19)',
    'Java Applet JMX Remote Code Execution (2013-01-10)',
    'MS13-009 Microsoft Internet Explorer SLayoutRun Use-AFter-Free (2013-02-13)',
    'Microsoft Internet Explorer CDwnBindInfo Object Use-After-Free (2012-12-27)',
    'Java 7 Applet Remote Code Execution (2012-08-26)',
    'Microsoft Internet Explorer execCommand Use-After-Free Vulnerability (2012-09-14)',
    'Java AtomicReferenceArray Type Violation Vulnerability (2012-02-14)',
    'Java Applet Field Bytecode Verifier Cache Remote Code Execution (2012-06-06)',
    'MS12-037 Internet Explorer Same ID Property Deleted Object Handling Memory Corruption (2012-06-12)',
    'Microsoft XML Core Services MSXML Uninitialized Memory Corruption (2012-06-12)',
    'Adobe Flash Player Object Type Confusion  (2012-05-04)',
    'Adobe Flash Player MP4 "cprt" Overflow (2012-02-15)',
    'MS12-004 midiOutPlayNextPolyEvent Heap Overflow (2012-01-10)',
    'Java Applet Rhino Script Engine Remote Code Execution (2011-10-18)',
    'MS11-050 IE mshtml!CObjectElement Use After Free  (2011-06-16)',
    'Adobe Flash Player 10.2.153.1 SWF Memory Corruption Vulnerability (2011-04-11)',
    'Cisco AnyConnect VPN Client ActiveX URL Property Download and Execute (2011-06-01)',
    'Internet Explorer CSS Import Use After Free (2010-11-29)',
    'Microsoft WMI Administration Tools ActiveX Buffer Overflow (2010-12-21)',
    'Internet Explorer CSS Tags Memory Corruption (2010-11-03)',
    'Sun Java Applet2ClassLoader Remote Code Execution (2011-02-15)',
    'Sun Java Runtime New Plugin docbase Buffer Overflow (2010-10-12)',
    'Microsoft Windows WebDAV Application DLL Hijacker (2010-08-18)',
    'Adobe Flash Player AVM Bytecode Verification Vulnerability (2011-03-15)',
    'Adobe Shockwave rcsL Memory Corruption Exploit (2010-10-21)',
    'Adobe CoolType SING Table "uniqueName" Stack Buffer Overflow (2010-09-07)',
    'Apple QuickTime 7.6.7 Marshaled_pUnk Code Execution (2010-08-30)',
    'Microsoft Help Center XSS and Command Execution (2010-06-09)',
    'Microsoft Internet Explorer iepeers.dll Use After Free (2010-03-09)',
    'Microsoft Internet Explorer "Aurora" Memory Corruption (2010-01-14)',
    'Microsoft Internet Explorer Tabular Data Control Exploit (2010-03-0)',
    'Microsoft Internet Explorer 7 Uninitialized Memory Corruption (2009-02-10)',
    'Microsoft Internet Explorer Style getElementsbyTagName Corruption (2009-11-20)',
    'Microsoft Internet Explorer isComponentInstalled Overflow (2006-02-24)',
    'Microsoft Internet Explorer Explorer Data Binding Corruption (2008-12-07)',
    'Microsoft Internet Explorer Unsafe Scripting Misconfiguration (2010-09-20)',
    'FireFox 3.5 escape Return Value Memory Corruption (2009-07-13)',
    'FireFox 3.6.16 mChannel use after free vulnerability (2011-05-10)',
    'Metasploit Browser Autopwn (USE AT OWN RISK!)\n']

browser_exploits_text = """
Введите эксплойт браузера, который вы хотели бы использовать [8]:
"""

# this is for the powershell attack vectors
powershell_menu = ['Powershell буквенно-цифровой инжектор Shellcode',
                   'Powershell Reverse Shell',
                   'Powershell Bind Shell',
                   'База данных SAM Powershell Dump',
                   '0D']

powershell_text = ("""
Модуль """+ bcolors.BOLD +""" Вектор атаки Powershell """+ bcolors.ENDC +""" позволяет создавать атаки, специфичные для PowerShell. Эти атаки позволят вам использовать PowerShell, который доступен по умолчанию во всех операционных системах Windows Vista и выше. PowerShell обеспечивает плодотворную среду для развертывания полезных нагрузок и выполнения функций, которые не запускаются профилактическими технологиями. \ N """)


encoder_menu = ['shikata_ga_nai',
                'Без кодировки',
                'Multi-кодировщик',
                'Исполняемый файл\n']

encoder_text = """
Выберите один из приведенных ниже вариантов: «Исполняемый файл с резервной копией» обычно является лучшим. Однако,
большинство все еще подобрано AV. Вам может понадобиться сделать дополнительную упаковку / шифрование
для того, чтобы обойти базовое обнаружение AV."""

dll_hijacker_text = """
 Уязвимость DLL Hijacker позволяет нормальным расширениям файлов
 вызывать локальные (или удаленные) .dll файлы, которые затем могут вызывать вашу полезную нагрузку или
 исполняемый файл. В этом сценарии она сжимает атаку в zip-файле
 и когда пользователь открывает расширение файла, будет вызывать DLL
 в конечном итоге наша полезная нагрузка. Во время этого выпуска все эти
 Расширения файлов были протестированы и, кажется, работают и не исправлены. Эта
 будет постоянно обновляться с течением времени.
"""

fakeap_dhcp_menu = ['10.0.0.100-254',
                    '192.168.10.100-254\n']

fakeap_dhcp_text = "Пожалуйста, выберите, какой DHCP Config вы хотели бы использовать: "
