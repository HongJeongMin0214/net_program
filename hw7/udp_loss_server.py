from socket import *
import threading

BUFF_SIZE = 1024
PORT = 5555

# mboxID별로 메시지를 저장할 딕셔너리
mbox = {}

# 서버 소켓 설정
s_sock = socket(AF_INET, SOCK_DGRAM)
s_sock.bind(('', PORT))
print("UDP 메시지 서버 실행 중...")

while True:
    data, addr = s_sock.recvfrom(BUFF_SIZE)
    msg = data.decode().strip()

    if msg == 'quit':
        print(f"클라이언트 {addr}에서 종료 요청. 서버 종료.")
        break

    tokens = msg.split(' ', 2)
    command = tokens[0]

    # send [mboxID] message
    if command == 'send' and len(tokens) == 3:
        mbox_id = tokens[1]
        message = tokens[2]
        if mbox_id not in mbox:
            mbox[mbox_id] = []
        mbox[mbox_id].append(message)
        s_sock.sendto("OK".encode(), addr)

    # receive [mboxID]
    elif command == 'receive' and len(tokens) == 2:
        mbox_id = tokens[1]
        if mbox_id in mbox and len(mbox[mbox_id]) > 0:
            response = mbox[mbox_id].pop(0)
        else:
            response = "No messages"
        s_sock.sendto(response.encode(), addr)

    else:
        s_sock.sendto("Invalid command".encode(), addr)

s_sock.close()
