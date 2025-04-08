import socket

while True:
    url = input("Enter the URL (index.html or aaaa): ")
    if url.lower() == 'exit':
        break

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('localhost', 80))

    try:
        s.send(f"GET /{url} HTTP/1.1\r\nHost: localhost\r\nConnection: close\r\n\r\n".encode())

        response = b""
        while True:
            chunk = s.recv(1024)
            if not chunk:
                break
            response += chunk

        # 응답을 헤더와 바디로 분리
        try:
            header, body = response.split(b"\r\n\r\n", 1)
            if b"Content-Type: text/html" in header:
                print("Response from server:")
                print(body.decode())  # HTML 파일이면 UTF-8로 출력
            else:
                print("Binary data received (e.g., image)")
        except ValueError:
            print("Invalid response format")

    except Exception as e:
        print(f"Error during request: {e}")

    finally:
        s.close()

# import socket
# import webbrowser

# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.connect(('localhost', 80))

# while True:
#     url = input("Enter the URL (index.html or aaaa): ")
#     webbrowser.open(f'http://127.0.0.1/{url}')  # f-string으로 URL을 동적으로 생성

#     try:
#         s.send(f"GET /{url} HTTP/1.1\r\nHost: localhost\r\n\r\n".encode())  # GET 요청 전송
#     except:
#         print('URL send error, client connection closed') 
#         break
#     else:
#         data1 = b""  # HTML 데이터
#         data2 = b""  # PNG 데이터
#         data3 = b""  # ICO 데이터

#         # HTML 데이터 받기
#         data1 += s.recv(1024)
#         if data1:
#             print(f"Response from server html: {data1.decode('euc-kr')}")
#         else:
#             print("(HTML) No response received or connection closed.")
#             break  # 응답이 없으면 종료
        
#         # PNG 데이터 받기
#         data2 += s.recv(1024)
#         if data2:
#             print("Response from server png:")
#             print(data2)
#         else:
#             print("(PNG) No response received or connection closed.")
#             break 
        
#         # ICO 데이터 받기
#         data3 += s.recv(1024)
#         if data3:
#             print("Response from server ico:")
#             try:
#                 print(data3)
#             except Exception as e:
#                 print(f"Error printing ICO data: {e}")
#         else:
#             print("(ICO) No response received or connection closed.")
#             break
# s.close()   
# import socket
# import webbrowser

# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.connect(('localhost', 80))

# while True:    
#     url = input("Enter the URL (index.html or aaaa): ")
#     webbrowser.open(f'http://127.0.0.1/{url}')
    
#     try:
#         s.send(f"GET /{url} HTTP/1.1".encode()) # GET /index.html HTTP/1.1 OR GET /aaaa HTTP/1.1 전송
#     except:
#         print('url send error, client connection closed') 
#         break
#     else:
#         data1 = b""  # HTML 데이터
#         data2 = b""  # PNG 데이터
#         data3 = b""
#         i = 0
        
#         for i in range(4):    
#             data1 += s.recv(1024)
#         if data1:
#             print(f"Response from server html: {data1.decode()}")
#         else:
#             print("(HTML)No response received or connection closed.")
#             break  # 응답이 없으면 루프 종
        
#         for i in range(4):    
#             data2 += s.recv(1024)
#         data2 = s.recv(1024)
#         if data2:
#             print("Response from server png:")
#             print(data2)
#         else:
#             print("(PNG)No response received or connection closed.")
#             break 
        
#         for i in range(4):    
#             data3 += s.recv(1024)
#         data3 = s.recv(1024)
#         if data3:
#             print("Response from server ico:")
#             try:
#                 print(data3)
#             except Exception as e:
#                 print(f"Error printing ICO data: {e}")
#         else:
#             print("(ICO)No response received or connection closed.")
#             break
# s.close()