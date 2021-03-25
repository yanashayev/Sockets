import socket


"""
open a socket 
#socket.AF_INET is IPV4
#socket.SOCK_STREAM is tcp 
"""
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

  """
 this socket wants to connect 
 """
 s.connect((socket.gethostname(),1234))
  """
 accapt the massage the server is sending
 1024- is the buffer- we are using tcp and we need to decide how big a chuncks of data we want to recive at a time
 """

msg=s.recv(1024)
print(msg.decode("utf-8"))