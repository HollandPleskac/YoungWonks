'''Mini-Project Webpage Downloader
-------------------------------------------------------------------------------
Steps: 
 1. program creates an Internet, TCP socket then closes the socket
 2. program makes the socket connect itself to google.com before closing
 3. program sends message(GET / HTTP/1.1\r\n\r\n)
 4. program recieves messages sent via the socket

3 Explanation: the command sent to the server (GET / HTTP/1.1\r\n\r\n) is a
request for the homepage (called /) of teh website.  The \r\n\r\n is a
'line ending' that tells google.com that the message has ended. Simply: we are
asking the Google website for a copy of the homepage.

4 Explanation: the cose prints out the message recieved by the socket and stores
the recieved message in a variable.

Code Overview: The code creates a socket, connects to google.com, requests the
homepage, and recieves the result. Then, it closes the socket.

Official Reference Sheet: https://docs.google.com/document/d/1lKwvuLmQsa2H4cPBuHtPUoEYD9neWjswUMkyAF_rtkw/edit?usp=sharing

Note:
replace |server_ip_address = gethostbyname("google.com")| with commented out
code below and replace |connection.sendall(b"GET / HTTP/1.1\r\n\r\n")|
with commented out code below to download the httpbin.org webpage
-------------------------------------------------------------------------------
'''

from socket import *
connection = socket(AF_INET,SOCK_STREAM)
server_ip_address = gethostbyname("google.com")
#server_ip_address = gethostbyname("httpbin.org")
server_port = 80
connection.connect((server_ip_address,server_port))
connection.sendall(b"GET / HTTP/1.1\r\n\r\n")
#connection.sendall(b"GET / HTTP/9.3\r\n\r\n")
while True:
     recieved_letter=connection.recv(1).decode("utf-8")
     if recieved_letter=='':
          break
     print(recieved_letter,end='')
connection.close()
