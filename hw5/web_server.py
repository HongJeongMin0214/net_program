from socket import *

s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 80))
s.listen(10)
print("Server listening on port 80...")

while True:
    c, (addr, port) = s.accept()
    print(f"Connection from {addr}:{port}")

    try:
        request = c.recv(1024).decode()
        if not request or ' ' not in request:
            print(f"url 응답 공백 또는 비었음: {request}")
            raise ValueError("Invalid HTTP request")
        print(f"Request: {request}")
        
        resource = request.split(' ')[1]
        filename = resource[1:] if len(resource) > 1 else "index.html"
        print(f"Requested file: {filename}")

        if filename.endswith(".html"):
            with open(filename, 'r', encoding='utf-8') as f_html:
                data_html = f_html.read()
            response = "HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n" + data_html
            c.send(response.encode('utf-8'))
        elif filename.endswith(".png"):
            with open(filename, 'rb') as f_png:
                data_png = f_png.read()
            c.send(b"HTTP/1.1 200 OK\r\nContent-Type: image/png\r\n\r\n" + data_png)
        elif filename.endswith(".ico"):
            try:
                with open(filename, 'rb') as f_ico:
                    data_ico = f_ico.read()
                c.send(b"HTTP/1.1 200 OK\r\nContent-Type: image/x-icon\r\n\r\n" + data_ico)
            except FileNotFoundError:
                print("ico 파일 없음")
        else:
            raise FileNotFoundError  # 알 수 없는 확장자면 404로 처리

    except FileNotFoundError:
        c.send(b"HTTP/1.1 404 Not Found\r\n\r\n<html><body><h1>404 Not Found</h1></body></html>")
    except Exception as e:
        print(f"Error: {e}")
        c.send(b"HTTP/1.1 400 Bad Request\r\n\r\n<html><body><h1>400 Bad Request</h1></body></html>")
    finally:
        c.close()

# from socket import *

# # 서버 소켓 생성
# s = socket(AF_INET, SOCK_STREAM)
# s.bind(('', 80))  # 포트 80에서 연결 대기
# s.listen(10)
# print("Server listening on port 80...")

# while True:
#     # 클라이언트 연결 수락
#     c, (addr, port) = s.accept()
#     print(f"Connection from {addr}:{port}")

#     try:
#         request = c.recv(1024).decode()  # GET 요청 받기
#         print(f"Request: {request}")
#         resource = request.split(' ')[1]
#         filename = resource[1:]  # 파일 경로
#         print(f"Requested file: {filename}")

#     except Exception as e:
#         print(f"Error: {e}")
#         c.send(b"HTTP/1.1 400 Bad Request\r\n")
#         c.send(b"\r\n")
#         c.send(b"<html><body><h1>400 Bad Request</h1></body></html>")
#     else:
#         if filename != "index.html":  # index.html이 아니면 404 응답
#             c.send(b"HTTP/1.1 404 Not Found\r\n")
#             c.send(b"\r\n")
#             c.send(b"<HTML><HEAD><TITLE>Not Found</TITLE></HEAD>")
#             c.send(b"<BODY>Not Found index.html</BODY></HTML>")
#             continue  # 404 오류 후 다음 요청 기다리기
#         else:
#             # index.html 파일이 요청되면 해당 파일을 처리
#             with open(filename, 'r', encoding='utf-8') as f_html:
#                 data_html = f_html.read()
#             mimeType_html = 'text/html'
#             mimeType_png = 'image/png'
#             mimeType_ico = 'image/x-icon'
#             # HTML 응답 보내기
#             c.send(b"HTTP/1.1 200 OK\r\n")
#             c.send(f"Content-Type: {mimeType_html}\r\n".encode())
#             c.send(b"\r\n")  # 헤더와 본문 구분
#             c.send(data_html.encode('euc-kr'))
#             # PNG 파일 응답 보내기 (파일 존재 확인 후)
#             try:
#                 with open("iot.png", 'rb') as f_png:
#                     data_png = f_png.read()
#                 c.send(b"HTTP/1.1 200 OK\r\n")
#                 c.send(f"Content-Type: {mimeType_png}\r\n".encode())
#                 c.send(b"\r\n")
#                 c.send(data_png)
#             except FileNotFoundError:
#                 c.send(b"HTTP/1.1 404 Not Found\r\n")
#                 c.send(b"\r\n")
#                 c.send(b"<html><body><h1>PNG Not Found</h1></body></html>")
#             # ICO 파일 응답 보내기 (파일 존재 확인 후)
#             try:
#                 with open("favicon.ico", 'rb') as f_ico:
#                     data_ico = f_ico.read()
#                 c.send(b"HTTP/1.1 200 OK\r\n")
#                 c.send(f"Content-Type: {mimeType_ico}\r\n".encode())
#                 c.send(b"\r\n")
#                 c.send(data_ico)
#             except FileNotFoundError:
#                 c.send(b"HTTP/1.1 404 Not Found\r\n")
#                 c.send(b"\r\n")
#                 c.send(b"<html><body><h1>ICO Not Found</h1></body></html>")

#     finally:
#         # 클라이언트 소켓 종료
#         c.close()



# from socket import *

# s = socket(AF_INET, SOCK_STREAM)
# s.bind(('', 80))
# s.listen(5)
# print("Server listening on port 80...")

# while True:
#     c, (addr, port) = s.accept()
#     print(f'Ip: {addr}, Port: {port}')
    
#     try:
#         request = c.recv(1024).decode() # GET /index.html HTTP/1.1 OR GET /aaaa HTTP/1.1 받음
#         print(f"Request: {request}")
#         resource = request.split(' ')[1]
#         filename = resource[1:]
#         print(filename)  #index.html OR aaaa
        
#         if filename != "index.html": # 해당 파일이 존재하지 않으면 (aaaa)
#             c.send(b"HTTP/1.1 404 Not Found\r\n")
#             c.send(b"\r\n")
#             c.send(b"<HTML><HEAD><TITLE>Not Found</TITLE></HEAD>")
#             c.send(b"<BODY>Not Found</BODY></HTML>")
#     except:
#         print('url recieve error, server connection closed') 
#         break
#     else: # index.html이면
#         f_html = open(filename, 'r', encoding='utf-8')
#         f_png = open(filename, 'rb')
#         f_ico = open(filename, 'rb')
        
#         mimeType_html = 'text/html'
#         mimeType_png = 'image/png'
#         mimeType_ico = 'image/x-icon'
        
#         data_html = f_html.read()
#         data_png = f_png.read()
#         data_ico = f_ico.read()
                    
#         c.send(b"'HTTP/1.1 200 OK\r\n")
#         c.send(f"Content-Type: {mimeType_html}\r\n".encode())
#         c.send(b"\r\n")
#         c.send(data_html.encode('euc-kr'))
        
#         c.send(b"'HTTP/1.1 200 OK\r\n")
#         c.send(f"Content-Type: {mimeType_png}\r\n".encode())
#         c.send(b"\r\n")
#         c.send(data_png)
            
#         c.send(b"'HTTP/1.1 200 OK\r\n")
#         c.send(f"Content-Type: {mimeType_ico}\r\n".encode())
#         c.send(b"\r\n")
#         c.send(data_ico)

# c.close()
    
    # try:
    #     True == bool(file_name)
    # except:
    #     client_socket.send(b"HTTP/1.1 404 Not Found\r\n\r\n")
    #     client_socket.send(b"<html><body><h1>404 Not Found</h1></body></html>")
    # else:
    #     client_socket.send(b"HTTP/1.1 200 OK\r\n")
        
    #     f1 = open(file_name, 'r', encoding='utf-8')
    #     mimeType = 'text/html'
    #     client_socket.send(f"Content-Type: {mimeType}\r\n\r\n".encode())
    #     data1 = f1.read()
    #     client_socket.send(data1.encode('euc-kr'))
        
    #     f2 = open(file_name, 'rb')
    #     mimeType = 'image/png'
    #     client_socket.send(f"Content-Type: {mimeType}\r\n\r\n".encode())
    #     data2 = f2.read()
    #     client_socket.send(data2)
        
    #     f3 = open(file_name, 'rb')
    #     mimeType = 'image/x-icon'
    #     client_socket.send(f"Content-Type: {mimeType}\r\n\r\n".encode())
    #     data3 = f3.read()
    #     client_socket.send(data3)
        
    
        
        
# from socket import *
# import webbrowser

# server_socket = socket(AF_INET, SOCK_STREAM)
# server_socket.bind(('', 80))  # 포트 80에서 대기
# server_socket.listen(5)
# print("Server listening on port 80...")

# while True:
#     client_socket, (addr, port) = server_socket.accept()
#     request = client_socket.recv(1024).decode()
#     resource = request.split(' ')[1]
#     file_name = resource.split('/')[len]
#     print(file_name)
    
#     try:
#         True == bool(file_name)
#     except:
#         client_socket.send(b"HTTP/1.1 404 Not Found\r\n\r\n")
#         client_socket.send(b"<html><body><h1>404 Not Found</h1></body></html>")
#     else:
#         if file_name == 'index.html':
#             webbrowser.open(f'http://{addr}:{port}/{file_name}')
#             f = open(file_name, 'r', encoding='utf-8')
#             mimeType = 'text/html'
            
#         elif file_name == 'iot.png':
#             webbrowser.open(f'http://{addr}:{port}/index.html/{file_name}')
#             f = open(file_name, 'rb')
#             mimeType = 'image/png'
#         elif file_name == 'favicon.ico':
#             webbrowser.open(f'http://{addr}:{port}/index.html/{file_name}')
#             f = open(file_name, 'rb')
#             mimeType = 'image/x-icon'
        
#         #헤더 전송
#         client_socket.send(b"HTTP/1.1 200 OK\r\n") 
#         client_socket.send(f"Content-Type: {mimeType}\r\n\r\n".encode())
#         # 바디 전송
#         data = f.read()
#         if file_name == 'index.html':
#             client_socket.send(data.encode('euc-kr'))
#         else:
#             client_socket.send(data)
            
#     client_socket.close()
        
        