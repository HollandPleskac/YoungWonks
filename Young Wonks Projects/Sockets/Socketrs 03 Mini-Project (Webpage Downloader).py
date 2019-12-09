#Mini-Project Webpage Downloader
from socket import *
connection=socket(AF_INET,SOCK_STREAM)
server_ip_address=gethostbyname("httpbin.org")
server_port=80
connection.connect((server_ip_address,server_port))
connection.sendall(b"GET / HTTP/1.1\r\n\r\n")
while True:
     received_letter=connection.recv(1).decode("utf-8")
     if received_letter=='':
          break
     print(received_letter,end='')
connection.close()
