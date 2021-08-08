import socket
import os

serv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto=0)
serv_sock.bind(('127.0.0.1', 5006))
serv_sock.listen(10)

while True:
    # Бесконечно обрабатываем входящие подключения
    client_sock, client_addr = serv_sock.accept()
    pid = os.fork()
    if pid:
      # client_sock.close()
      print('parent process')
    else:
      print('Connected by', client_addr)

      while True:
          # Пока клиент не отключился, читаем передаваемые
          data = client_sock.recv(1024)
          print(data, pid)
          if not data:
              # Клиент отключился
              break
          client_sock.sendall(data)

      client_sock.close()
