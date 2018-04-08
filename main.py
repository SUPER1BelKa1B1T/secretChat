# -*- coding:utf-8 -*-

from socket import *
import threading
import os
from termcolor import colored
import colorama

colorama.init()

def server(ip, port):
    UDPserver = socket(AF_INET, SOCK_DGRAM)
    UDPserver.bind((ip, port))
    UDPserver.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    UDPserver.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)

    while True:
        message, addr = UDPserver.recvfrom(1024)
        print(colored(u'\n[Client:] ', 'green'), addr)
        print(colored(u'[Message:] ', 'green'), bytes.decode(message))
        if bytes.decode(message) == 'q':
            UDPserver.close()

def client(ip, port, name):
    UDPclient = socket(AF_INET, SOCK_DGRAM)
    UDPclient.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
    while True:
        data = input(colored('[Message:' + name + ']', 'yellow'))
        if not data:
            continue 
        if data == 'q':
            UDPclient.sendto(str.encode(data), (ip, port))
            UDPclient.close()
        UDPclient.sendto(str.encode('[' + name + ']' + data), (ip, port))


while True:
    ip = input('==>Input ip:')
    port = input('==>Input port:')

    toip = input('==>Input toip: ')
    toport = input('==>Input toport: ')

    name = input(u'==>Name: ')

    if ip and port:
        break

os.system('cls')

if __name__=='__main__':
    threadCMD = threading.Thread(target=server, args = (str(ip), int(port), str(name)))
    threadBOT = threading.Thread(target=client, args = (str(toip), int(toport)))
    threadCMD.start()
    threadBOT.start()


    