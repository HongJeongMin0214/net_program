import socket
import threading
import time

clients = []

def client_handler(conn, addr):
    print(f"new client {addr}")
    clients.append(conn)
    try:
        while True:
            msg = conn.recv(1024)
            if not msg:
                break
            if b'quit' in msg:
                break
            now = time.strftime('%a %b %d %H:%M:%S %Y')
            print(f"{now} {addr}:{msg.decode()}")
            broadcast(msg, conn)
    except:
        pass
    finally:
        print(f"Client exited: {addr}")
        clients.remove(conn)
        conn.close()

def broadcast(msg, sender_conn):
    for client in clients:
        if client != sender_conn:
            try:
                client.send(msg)
            except:
                pass

def main():
    host = 'localhost'
    port = 2500
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen()
    print("Server Started")

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=client_handler, args=(conn, addr))
        thread.start()

if __name__ == "__main__":
    main()
