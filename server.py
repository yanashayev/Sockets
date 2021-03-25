import socket


"""
open a socket 
#socket.AF_INET is IPV4
#socket.SOCK_STREAM is tcp 
"""
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
 """
 bind the socket by IP and a port
  s.bind((*ip*,*port*))
 THIS IS THE SERVER- WE WILL HOST THE SERVER ON THE SAME MACHINE WE HAVE THE CODE (I USE RASPBERRY PI ZERO)
#socket.gethostbyname()- localhost
#1234- is the port (you can go with any 4 digits port or lower digits, but i recommend 4 digits because 3 digits will probebly be occupied)
 """

 s.bind((socket.gethostbyname(),1234))

 """
 listen forever for a connaction
 anybody how connect we will let him
 #client_socker- like our socket- we can communivate with this socket
 #address- their ip 

 """
 s.listen(5)
while True:
    clientsocket,address= s.accept()
    print(f"connection from {address} has been establushed!")
    clientsocket.send(bytes("wellcome to the server","utf-8")) #utf-8 type of bytes







 
  """
 
 """
  """
 
 """
