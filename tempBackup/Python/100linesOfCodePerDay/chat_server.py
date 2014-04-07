#chat_server.py
from socket import *

print '##########'
print 'cs\s dialog'
print '##########'

HOST = ""
PORT = 50000
ss = socket(AF_INET, SOCK_STREAM)
ss.bind((HOST, PORT))
ss.listen(1)

con, add = ss.accept()

name = con.recv(100)
data = '***' + name + ' is logged in'

while data:
	print data
	con.send(data)
	data = name + ']' + con.recv(1024)
