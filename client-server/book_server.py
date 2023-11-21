import socket
from datetime import datetime

address = ('localhost', 5555)
print('Server starts')

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(address)
server.listen(5)

client, _ = server.accept()
data = client.recv(1024).decode()
print(data)
if data != 'time':
    print('Error command!')
    client.sendto(b'Error command!', address)
else:
    client.send(datetime.now().isoformat().encode())

client.close()
server.close()