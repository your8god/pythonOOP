import zmq
from datetime import datetime

host = '127.0.0.1'
port = 5555
socket = f'tcp://{host}:{port}'
context = zmq.Context()

server = context.socket(zmq.REP)
server.bind(socket)
while True:
    request = server.recv().decode('utf-8')
    print(f'{datetime.now().isoformat()}: message : {request}')
    if request == 'close':
        server.close()
        break
    if request != 'time':
        print('Error command')
        server.send(bytes('Error command', 'utf-8'))
        continue
    server.send(bytes(datetime.now().strftime('%d.%m.%Y %H:%M:%S'), 'utf-8'))
    