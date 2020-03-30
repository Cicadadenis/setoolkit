#!/usr/bin/env python
"""
УСТАНОВИТЬ реализацию ядра PyFakeMiniDNS.

Слегка измененная реализация PyfakeminiDNS Франциско Сантоса
Скрипт предназначен для запуска в виде потока и обработки различных дополнительных
задачи конфигурации системы, при необходимости в рабочей среде,
наряду с несколькими соображениями по реализации специально для SET.
"""

import os
import socket
import subprocess
import sys
import threading

# We need this module variable so the helper functions can be called
# from outside of this module, e.g., during SET startup and cleanup.
dns_server_thread = None

def start_dns_server(reply_ip):
    """
    Вспомогательная функция, предназначенная для вызова из других модулей.

    Args:
        reply_ip (строка): IPv4-адрес в четырехточечной нотации для использования во всех ответах.
"""
    global dns_server_thread
    dns_server_thread = MiniFakeDNS(kwargs={'port': 53, 'ip': reply_ip})
    dns_server_thread.start()

def stop_dns_server():
    """
    Вспомогательная функция, предназначенная для вызова из других модулей.
    """
    dns_server_thread.stop()
    dns_server_thread.join()
    dns_server_thread.cleanup()

class DNSQuery:
    """
    DNS-запрос (который может быть проанализирован как двоичные данные).

    См. Оригинал для справки, но обратите внимание, что произошли изменения:
        https://code.activestate.com/recipes/491264-mini-fake-dns-server/
    Среди изменений есть имена переменных, которые были переведены
    на английский с их оригинального испанского.
    """

    def __init__(self, data):
        """
    Args:
            data (bytes): двоичные данные пакета DNS с провода.
        """
        self.data = data

        # The domain name the client is querying the DNS for.
        self.domain = ''

        # Parse DNS packet headers.
        txn_id = data[:2]  # DNS transaction ID, two bytes.
        flags  = data[2:4] # DNS flags, also two bytes.

        # To determine whether or not this DNS packet is a query that
        # we should respond to, we need to examine the "QR" field and
        # the "opcode" field. Together, these make up five bits, but
        # they are the left-most bits (most-significant bits) in the
        # first byte of the two-byte Flags field. An ASCII diagram:
        #
        #     X  XXXX ...
        #     ^  ^
        #     |  \- The opcode bits are here.
        #     |
        #     The QR bit.
        #
        # To read them meaningfully, we first discard the three bits
        # in the rightmost (least significant) position by performing
        # a 3-place bitwise right shift, which in python is the `>>`
        # operator. At that point, we have a byte value like this:
        #
        #     000 X XXXX
        #         ^  ^
        #         |  \- The opcode bits are here.
        #         |
        #         The QR bit.
        #
        # Now that the most significant bits are all zero'ed out, we
        # can test the values of the unknown bits to see if they are
        # representing a standard query.
        #
        # In DNS, a standard query has the opcode field set to zero,
        # so all the bits in the opcode field should be 0. Meanwhile,
        # the QR field should also be a 0, representing a DNS query
        # rather than a DNS reply. So what we are hoping to see is:
        #
        #    000 0 0000
        #
        # To test for this reliably, we do a bitwise AND with a value
        # of decimal 31, which is 11111 in binary, exactly five bits:
        #
        #      00000000  (Remember, 0 AND 1 equals 0.)
        #  AND 00011111
        #  ------------
        #      00000000 = decimal 0
        #
        # In one line of Python code, we get the following:
        kind = (flags[0] >> 3) & 31 # Opcode is in bits 4, 5, 6, and 7 of first byte.
                                    # QR bit is 8th bit, but it should be 0.
                                    # And now, we test to see if the result
        if 0 == kind:               # was a standard query.

            # The header of a DNS packet is exactly twelve bytes long,
            # meaning that the very start of the first DNS question
            # will always begin at the same offset.
            offset = 12 # The first question begins at the 13th byte.

            # The DNS protocol encodes domain names as a series of
            # labels. Each label is prefixed by a single byte denoting
            # that label's length.
            length = data[offset]
            while 0 != length:
                self.domain += data[offset + 1 : offset + length + 1].decode() + '.'
                offset += length + 1
                length = data[offset]

    def response(self, ip):
        """
        Создайте ответный пакет DNS с заданным IP-адресом.

        TODO: это неправильно отвечает на запросы EDNS, которые используют
              типа OPT псевдо-записи. В частности, указатель
              неправильно, потому что мы не проверяем длину оригинала
              запрос мы получили. Вместо этого мы должны отметить длину
              исходный пакет до конца первого вопроса,
              и усекать (то есть отбрасывать, игнорировать) остаток.

              На данный момент, что это на самом деле означает, что тестирование этого
              сервер, использующий последнюю версию `dig (1)`, потерпит неудачу
              если вы не используете опцию запроса `+ noedns`. Например:

                  dig @ 127.0.0.1 example.com + noedns

              Более простые или старые утилиты DNS, такие как host (1)
              наверное собираюсь на работу.

        Args:
            ip (строка): IP-адрес для ответа.
        """
        packet = b''
        if self.domain:
            packet += self.data[:2] + b'\x81\x80'
            packet += self.data[4:6] + self.data[4:6] + b'\x00\x00\x00\x00' # Questions and Answers Counts
            packet += self.data[12:]                                        # Original Domain Name Question
            packet += b'\xc0\x0c'                                           # Pointer to domain name
            packet += b'\x00\x01\x00\x01\x00\x00\x00\x3c\x00\x04' # Response type, ttl and resource data length -> 4 bytes
            packet += bytes([int(x) for x in ip.split('.')])      # 4 bytes of IP.
        return packet

class MiniFakeDNS(threading.Thread):
    """
Сервер MiniFakeDNS, созданный для работы в качестве потока Python.
    """
    def __init__(self, group=None, target=None, name=None,
                       args=(), kwargs=None):
        super(MiniFakeDNS, self).__init__(
                group=group, target=target, name=name)
        self.args = args
        self.kwargs = kwargs

        # The IPs address we will respond with.
        self.ip = kwargs['ip']

        # The port number we will attempt to bind to. Default is 53.
        self.port = kwargs['port']

        # Remember which configuration we usurped, if any. Used to cleanup.
        self.cede_configuration = None

        # A flag to indicate that the thread should exit.
        self.stop_flag = False

    def run(self):
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as udps:
            udps.setblocking(False)
            try:
                udps.bind(('', self.port))
            except OSError as e:
                if 'Address already in use' == e.strerror and os.path.exists('/etc/resolv.conf'):
                    # We can't listen on port 53 because something else got
                    # there before we did. It's probably systemd-resolved's
                    # DNS stub resolver, but since we are probably running as
                    # the `root` user, we can fix this ourselves.
                    if 'stub-resolv.conf' in os.path.realpath('/etc/resolv.conf'):
                        self.usurp_systemd_resolved()
                        self.cede_configuration = self.cede_to_systemd_resolved
                    # Try binding again, now that the port might be available.
                    udps.bind(('', self.port))
            while not self.stop_flag:
                try:
                    data, addr = udps.recvfrom(1024)
                    p = DNSQuery(data)
                    udps.sendto(p.response(self.ip), addr)
                except BlockingIOError:
                    pass
            print("Выход из DNS-сервера..")
        sys.exit()

    def cleanup(self):
        if self.cede_configuration is not None:
            self.cede_configuration()

    def stop(self):
        """
        Сигналы к потоку DNS-сервера для остановки.
        """
        self.stop_flag = True

    def usurp_systemd_resolved(self):
        """
        Вспомогательная функция, чтобы получить systemd-разрешение из пути, когда это
        слушает 127.0.0.1:53 и мы пытаемся запустить SET
        собственный DNS-сервер.
        """
        try:
            os.mkdir('/etc/systemd/resolved.conf.d')
        except (OSError, FileExistsError):
            pass
        with open('/etc/systemd/resolved.conf.d/99-setoolkit-dns.conf', 'w') as f:
            f.write("[Resolve]\nDNS=9.9.9.9\nDNSStubListener=no")
        os.rename('/etc/resolv.conf', '/etc/resolv.conf.original')
        os.symlink('/run/systemd/resolve/resolv.conf', '/etc/resolv.conf')
        subprocess.call(['systemctl', 'restart', 'systemd-resolved.service'])

    def cede_to_systemd_resolved(self):
        """
        Вспомогательная функция для передачи конфигурации системы обратно в systemd-разрешения
        после того, как мы узурпировали контроль над конфигурацией DNS.
        """
        os.remove('/etc/systemd/resolved.conf.d/99-setoolkit-dns.conf')
        os.remove('/etc/resolv.conf')
        os.rename('/etc/resolv.conf.original', '/etc/resolv.conf')
        subprocess.call(['systemctl', 'restart', 'systemd-resolved.service'])
