from socket import *
import thread
print 'cs\'s chat server'

#generate server socket

HOST = ""
PORT = 50000

s = socket(AF_INET, SOCK_STREAM)
s.bind((HOST,PORT))
s.listen(1)

user = []

def service():
	con, add = s.accept()
	global users
	users.append(con)
	thread.start_new_thread(service,())
	name = con.recv(10)
	str = '***' + name + ' is logged in. ***'
	try:
		while con:
			print str
			for each in users: each.send(str)
			str = name + ']' + con.recv(1024)
		except:
			users.remove(con)
			str = '***' + name + ' is log out. ***'
			print str
			if users:
				for each in users: each.send(str)
	#generate thread
	thread.start_new_thread(service,())
	#infinite loop
	while 1: pass

	
