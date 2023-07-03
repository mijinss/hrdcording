import socket, time

host = '172.30.1.25'
port = 3333

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((host,port))

server_socket.listen()

print('echo server start')

client_soc, addr = server_socket.accept()

print('connected client addr:', addr)

while True:
    data = client_soc.recv(100)
    msg = data.decode()
    print('recv msg:',msg)
    client_soc.sendall(msg.encode(encoding='utf-8'))
    if msg == '/end':
        break
time.sleep(5)
print('서버 종료')
server_socket.close()
                                  
            
              




