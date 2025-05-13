import socket
import threading

# 메시지를 계속 수신하는 함수 (서브 스레드)
def receive(sock):
    while True:
        try:
            data = sock.recv(1024)
            if not data:
                break
            print(data.decode())
        except:
            break

# 메인 클라이언트 함수
def main():
    host = 'localhost'
    port = 2500
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))

    my_id = input("ID를 입력하세요: ")
    sock.send(f"[{my_id}]".encode())

    # 메시지 수신을 위한 서브 스레드 실행
    recv_thread = threading.Thread(target=receive, args=(sock,))
    recv_thread.daemon = True
    recv_thread.start()

    while True:
        msg = input()
        if msg == 'quit':
            sock.send(f"[{my_id}] 님이 퇴장하셨습니다.".encode())
            break
        full_msg = f"[{my_id}] {msg}"
        sock.send(full_msg.encode())

    sock.close()

if __name__ == "__main__":
    main()
