#!usr/bin/python
import socket
ip="127.0.0.1"
port=9000
#calling udp
sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# ....................................this section for sender side.......................................
while True:
	s=raw_input("enter a string:     ")
	sock.sendto(s, (ip,port))
	#....................................receiver side code.................................................
#!usr/bin/python
import socket  
ip="127.0.0.1"
port=9000
#calling udp protocol
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#binding ip and port
s.bind((ip,port))
print s.recvfrom(100)
