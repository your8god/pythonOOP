import socket
import time


address = ('localhost', 5555)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(address)
client.send(bytes('hi! I am connecting', 'utf-8'))
data = client.recv(1024).decode("utf-8")
print(f'result: {data}')

try:
    while True:
        client.send(bytes('get', 'utf-8'))
        data = client.recv(1024).decode('utf-8')
        print(data)
        time.sleep(2.5)
except ConnectionError:
    client.close()