import socket
from datetime import datetime
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


msg= "Hello"
L=[]
for i in range(0,5):
    t1 = datetime.now()
    client_socket.sendto(msg.encode("utf-8"),("127.0.0.1",12345))
    data, server_address= client_socket.recvfrom(4096)
    t2=datetime.now()
    print(str(data))
    time=t2-t1
    L.append(time)
    print("The round trip time for each request/reply pair is", time.microseconds)

sum=0
for i in range (0,5):
    sum+= L[i].microseconds

average=sum/5
print("The average RTT is", average)

client_socket.close()