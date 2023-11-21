import socket
from datetime import datetime


address = ('localhost', 5555)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(address)
server.listen(3)

candies, index = ['Choko', 'Solo rolo', 'Barbarian', 'Zezv', '__@#___f***CK!'], 0
client, _ = server.accept()
while True:
    request = client.recv(1024).decode('utf-8')
    if request == 'get':
        if index == len(candies): 
            client.send(bytes("It's all! Now you can relax", 'utf-8'))
            client.close()
            server.close()
            break
        client.send(bytes(f'get time: {datetime.now().strftime("%d.%m.%Y %H:%M:%S")} --- {candies[index]}', 'utf-8'))
        index += 1
    elif request.startswith('hi'):
        print(f'new connect was created: {datetime.now().strftime("%d.%m.%Y %H:%M:%S")}')
        client.send(bytes('ok', 'utf-8'))
    else:
        client.send(bytes("undefined command! You have to only use 'get'"))
