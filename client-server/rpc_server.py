from xmlrpc.server import SimpleXMLRPCServer
from datetime import datetime

def time():
    return datetime.now().isoformat()

server = SimpleXMLRPCServer(('localhost', 5555))
server.register_function(time, 'time')
server.serve_forever()