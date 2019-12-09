'''server.py
----------------------------------------------------------------------
Notes: Write the Program on the Server Side with the Python Script
Started With: 
         import socket
         host=''
         port=12345
         s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
 - the parameter AF_INET means that this socket is an Internet socket.
 - the parameter SOCK_STREAM means that we want to use a TCP socket, not a UDP socket.
 - TCP sockets make sure that messages arrive in order and without transmission errors.
 - UDP messages are not guaranteed to arrive in order, and sometimes do not arrive at all!
 - bind the socket to host ip address and port using:
         s.bind((host, port))
         print('socket binded to', port)
 - backlog argument specifies the maximum number of queued connections and should be at
     least 0. The maximun value is system-dependent (usually 5)
         backlog = 5
 - listen for connections made to the socket
         s.listen(backlog)
 - s.accept() returns a pair of values: (conn, addr) where conn is a new socket object
     usable to send and recieve data on the connections, and addr is the address bound
     to the socket on the other end of the connection.
         conn,addr = s.accept()
         print('socket is listening')
         print('Got connection from ',addr)
 - In a while loop
         while 1:
             name = input('Hello, say something to the client')
             print('waiting for client's response')
 - socket.send is the data sent to the client. The socket must be byte connected to
     a remote socket. It returns the number of bytes sent.
     'conn.recv' tells the buffer size.
         conn.send(name.encode())
         data = conn.recv(1024).decode('utf-8')
         print('Recieved from client address: ',addr)
         print('Message recieved: ',data)
 - At the end of the while loop, close the connection.
         conn.close()
'''
import socket
host=''
port=12345
backlog = 5
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((host, port))
print('socket binded to', port)
s.listen(backlog)
conn,addr = s.accept()
print('socket is listening')
print('Got connection from ',addr)
while 1:
    name = input('Hello, say something to the client')
    print('waiting for clients response')
    conn.send(name.encode())
    data = conn.recv(1024).decode('utf-8')
    print('Recieved from client address: ',addr)
    print('Message recieved: ',data)
conn.close()
