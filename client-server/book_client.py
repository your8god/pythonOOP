import socket
from datetime import datetime

address = ('localhost', 5555)
print('Client starts')

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(address)
client.sendto('time'.encode(), address)

data = client.recv(1024)
print(data.decode())
client.close()