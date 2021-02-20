import socket
from datetime import datetime
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

IP_address= input("Enter the IP address of the echo server :")
port_number= int(input("Enter the port number of the server :"))


msg= "Hello"
L=[]
for i in range(0,5):
    t1 = datetime.now()
    client_socket.sendto(msg.encode("utf-8"),(IP_address,port_number))
    data, server_address= client_socket.recvfrom(4096)
    t2=datetime.now()
    print(str(data))
    time=t2-t1
    L.append(time)
    print("Round trip time ",i, ":", time.microseconds, "microseconds")

sum=0
for i in range (0,5):
    sum+= L[i].microseconds

average=sum/5
print("The average RTT is", average, "microseconds")

client_socket.close()