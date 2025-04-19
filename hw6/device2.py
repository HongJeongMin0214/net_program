# device2_server.py
from socket import *
from random import randint
import time

HOST = ''
PORT = 9002

s = socket(AF_INET, SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
print('Device2 waiting...')

conn, addr = s.accept()
print('Connected by', addr)

while True:
    data = conn.recv(1024).decode().strip()
    if data.lower() == 'quit':
        break
    elif data.lower() == 'request':
        heartbeat = randint(40, 140)
        steps = randint(2000, 6000)
        cal = randint(1000, 4000)
        now = time.asctime()
        msg = f"{now}: Device2: Heartbeat={heartbeat}, Steps={steps}, Cal={cal}"
        conn.send(msg.encode())

conn.close()
s.close()
