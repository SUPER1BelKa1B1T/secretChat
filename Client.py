import socket
import threading


class Client:
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    toData = ''
    fromData = ''

    def __init__(self, host, ip, port, name):
        self.server.bind(host)
        self.name = name
        self.ip = ip
        self.port = port 

    @staticmethod
    def __new_thread__(func):
        thread = threading.Thread(target=func)
        thread.start()

    def __sender__(self):
        while self.toData != 'quit':
            self.toData = input()
            self.server.sendto(str.encode('[' + self.name + ']' + self.toData), (self.ip, self.port))

    def __handler__(self):
        while self.toData != 'quit':
            try:
                self.fromData = self.server.recvfrom(1024)
                if not self.fromData:
                    continue 
                print(bytes.decode(self.fromData))
            except Exception as err:
                print(err)
    
    def run(self):
        self.__new_thread__(self.__handler__)
        self.__new_thread__(self.__sender__)


client = Client(('127.0.0.1', 5000), '127.0.0.1', 4000, 'Max')
client.run()
