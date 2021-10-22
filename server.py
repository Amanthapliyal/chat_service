import socket

HEADERSIZE =10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 6789))
s.listen(5)

while True:
    clientsocket, address = s.accept()
    print(f"{address} has established a Connection to server! ")
    
    msg = "welcome TO The Server!"
    msg = f'{len(msg): < {HEADERSIZE}}' + msg

    clientsocket.send(bytes(msg,"utf-8"))
    