'''client.py
----------------------------------------------------------------------
Notes: Write the Program on the Client Side with the Python Script
Started With:
         import socket
         host='192.168.1.x'  # server side ip address
         port = 12345
 - To find ip address of the server, we type ifconfig on linux, or type
     ipconfig on Windows command prompt.
         s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 - Connect socket to server:
         s.connect((host,port))
 - In a while loop, the socket recieves data as 1024 bytes
         while 1:
             data = s.recv(1024)
             print('Revieved from server', repr(data))
             message=input("Say something to server: ")
             s.send(message.encode())
 - The socket can send a message using s.send(). At the end of the loop, close
     the socket.
         s.close()
'''

import socket
host='192.168.1.x'  # server side ip address
port = 12345
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port))
while 1:
    data = s.recv(1024)
    print('Revieved from server', repr(data))
    message=input("Say something to server: ")
    s.send(message.encode())
    s.close()
