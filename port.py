import socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
h = ""
p = 
def tara(p):
	if s.connect_ex((h,p)):
		print("Kapalı")
	else:
		print("Açık")
tara(p)

