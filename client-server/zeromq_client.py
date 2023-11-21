import zmq
from time import sleep

host = '127.0.0.1'
port = 5555
socket = f'tcp://{host}:{port}'
context = zmq.Context()

client = context.socket(zmq.REQ)
client.connect(socket)
for _ in range(5):
    client.send(bytes('time', 'utf-8'))
    request = client.recv().decode('utf-8')    
    print('Server:', request)
    sleep(2)


client.send(bytes('kek', 'utf-8'))
request = client.recv().decode('utf-8') 
client.send(bytes('close', 'utf-8'))
client.close()