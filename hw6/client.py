# client.py
from socket import *
import time

BUFSIZE = 1024

# 디바이스 1, 2에 각각 연결
device1 = socket(AF_INET, SOCK_STREAM)
device1.connect(('localhost', 9001))

device2 = socket(AF_INET, SOCK_STREAM)
device2.connect(('localhost', 9002))

print("디바이스와 연결되었습니다. '1', '2', 또는 'quit' 입력 가능")

while True:
    msg = input("1 또는 2 입력 (quit 입력 시 종료): ").strip().lower()
    
    if msg == '1':
        device1.send(b'request')
        data = device1.recv(BUFSIZE).decode()
    elif msg == '2':
        device2.send(b'request')
        data = device2.recv(BUFSIZE).decode()
    elif msg == 'quit':
        device1.send(b'quit')
        device2.send(b'quit')
        break
    else:
        print("잘못된 입력입니다.")
        continue

    with open("data.txt", "a", encoding="utf-8") as f:
        f.write(data + "\n")
    print("받은 데이터:", data)

device1.close()
device2.close()
