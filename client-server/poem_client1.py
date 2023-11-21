import re
import zmq


socket = 'tcp://127.0.0.1:6666'
context = zmq.Context()
client = context.socket(zmq.SUB)
client.connect(socket)

client.setsockopt(zmq.SUBSCRIBE, 'vowels'.encode('utf-8'))
while True:
    topic, word = client.recv_multipart()
    print(topic.decode('utf-8'), word.decode('utf-8'))