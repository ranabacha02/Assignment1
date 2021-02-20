
import socket
from datetime import datetime

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = '127.0.0.1'
server_port = 12345

server = (server_address, server_port)
sock.bind(server)

while True:
    data, client_address = sock.recvfrom(4096)
    time= datetime.now()
    print(time)
    sock.sendto(data, client_address)
