from socket import *
from Tkinter import *
import tkSimpleDialog, thread
def talk(event):
	s.send(ent.get())
	ent.delete(o,END)
def hear():
	while 1:
		str = s.recv(1024) + '\n'
		str + unicode(str,'iso8859_1')
		txt.config(state=NORMAL)
		txt.insert(END,str)
		txt.config(state=DISABLED)
		ent.focus()

root = Tk()
root.title('cs\'s chat room')
ent = Entry(root)
ent.pack(fill=X)
ent.insert(o,"")
ent.bind('<Return>',talk)
txt = Text(root)
txt.pack()


#log in to server
name = tkSimpleDialog.askstring('cs\'s chat room',unicode('please put in keyname','iso8859_1'))
if name:
	HOST = '127.0.0.1'
	PORT = 50000
	s = socket(AF_INET,SOCK_STREAM)
	s.connect((HOST,PORT))
	s.send(name)
	thread.start_new_thread(hear,())
	mainloop()


