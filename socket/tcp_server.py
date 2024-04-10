import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
s.listen(5)
numbers = [111, 2, 14382, 9, -2]
while True:
    try:
        clientsocket, address = s.accept()
        print(f'Connection from {address} has been established!')
        for number in numbers:
            clientsocket.send(bytes(str(number)+'\n', 'utf-8'))
    except KeyboardInterrupt:
        break

clientsocket.close()