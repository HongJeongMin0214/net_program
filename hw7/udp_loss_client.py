from socket import *

BUFF_SIZE = 1024
PORT = 5555

# 클라이언트 소켓 설정
c_sock = socket(AF_INET, SOCK_DGRAM)
c_sock.connect(('localhost', PORT))

while True:
    msg = input('Enter the message("send mboxId message" or "receive mboxId"):')
    c_sock.send(msg.encode())

    if msg.strip() == 'quit':
        break

    data = c_sock.recv(BUFF_SIZE)
    print(data.decode())

c_sock.close()
