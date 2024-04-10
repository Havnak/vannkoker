import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1234))

while True:
    msg = s.recv(1024)
    number_list = msg.decode().split('\n')
    print(number_list)
    for number in number_list:
        try:
            print(int(number)*2)
        except:
            continue