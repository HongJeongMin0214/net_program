# device1_server.py
from socket import *
from random import randint
import time

HOST = ''
PORT = 9001

s = socket(AF_INET, SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
print('Device1 waiting...')

conn, addr = s.accept()
print('Connected by', addr)

while True:
    data = conn.recv(1024).decode().strip()
    if data.lower() == 'quit':
        break
    elif data.lower() == 'request':
        temp = randint(0, 40)
        humid = randint(0, 100)
        illum = randint(70, 150)
        now = time.asctime()
        msg = f"{now}: Device1: Temp={temp}, Humid={humid}, Iilum={illum}"
        conn.send(msg.encode())

conn.close()
s.close()
