# -*- coding: utf-8 -*-
from Tkinter import *
#import win32api
#import win32con
#import time

st_glob=False
tk=Tk()

text=StringVar()
text.set('')
tk.title('BD v0.1')
tk.geometry('500x500')

#test
button1 = Button(tk,text='start',width=10,height=2)
button2 = Button(tk,text='end',width=10,height=2)

#для работы с БД
butAdd = Button(tk,text='Добавить',width=10,height=2)
butDel = Button(tk,text='Удалить',width=10,height=2)
butChange = Button(tk,text='Изменить',width=10,height=2)#пока не знаю

log = Text(tk)
#msg = Entry(tk, textvariable=text)

#msg.pack(side='bottom', fill='x', expand='true')

#button1.pack(side='left')
#button2.pack(side='left')

#попробовать left-top
butAdd.pack(side='top')
butDel.pack(side='top')
butChange.pack(side='top')

log.pack(side='bottom', fill='both',expand='true')

def start(event):
	global st_glob
	st_glob=True

def end(event):
	global st_glob
	st_glob =False


#bind to function
button1.bind('<Button-1>', start)
button2.bind('<Button-1>', end)
#butAdd.bind ()#почитать

def loopproc():
	if st_glob == True:
		try:
			i = 0
			while i < 3:
				work()
				log.insert(END,i+'\n')
				i +=1
				print (i)
			#sendproc(None)
			#print (message)
			#log.insert(END,message+'\n')
			tk.update()
		except:
			tk.after(1,loopproc)
			return
	tk.after(1,loopproc)


def work():

	return 1


def sendproc(event):
	temp=GetMyPos()
	sock.sendto (temp,('255.255.255.255',12123))
	log.insert (END,temp+'\n')

tk.after(1,loopproc)
tk.mainloop()