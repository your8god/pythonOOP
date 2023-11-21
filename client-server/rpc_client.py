import xmlrpc.client

proxy = xmlrpc.client.ServerProxy('http://localhost:5555/')
print(proxy.time())