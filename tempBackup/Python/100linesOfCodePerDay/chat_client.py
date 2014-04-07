#chat_client.py

from socket import *

print ############
print 'cs\'s dialog'
print ############

name = raw_input('plz.type your keyname ')

if name:
	#generate client socket
	HOST = '127.0.0.1'
	PORT = 50000
	cs = socket(AF_INET,SOCK_STREAM)
	cs.connect((HOST,PORT))
	cs.send(name)
	data = cs.recv(100)
	while 1:
		print data
		cs.send(raw_input() or '')
		data = cs.recv(1024)

		