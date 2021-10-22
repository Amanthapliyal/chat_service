import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 6789))
s.listen(5)

while True:
    clientsocket, address = s.accept()
    print(f"{address} has established a Connection to server! ")
    clientsocket.send(bytes("Welcome to the server!","utf-8"))
    clientsocket.close()