import socket
import time


class Server:
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    connections = []

    def __init__(self, host):
        self.server.bind(host)

    def handler(self):
        while True:
            time_now = time.strftime('[%Y-%m-%d-%H.%M.%S]', time.localtime())
            try:
                data, address = self.server.recvfrom(1024)
                if not data:
                    continue
                if address not in self.connections:
                    self.connections.append(address)
                    conn_msg = str('[CONNECTION]' + time_now + '[' + str(address) + ']')
                    print(conn_msg)
                    for connect in self.connections:
                        if connect != address:
                            self.server.sendto(str.encode(conn_msg), connect)
                msg = str('[MESSAGE]' + time_now + '[' + str(address) + ']' + bytes.decode(data))
                print(msg)
                
                for connect in self.connections:
                    if connect != address:
                        self.server.sendto(str.encode(msg), connect)
            except Exception as err:
                print(err)


server = Server(('127.0.0.1', 4000))
server.handler()
