from tkinter import *
root=Tk()
root.title('Calculator')
root.config(background='#8dccf0')
root.iconbitmap('cal icon.ico')
e=Entry(root,text='Enter your name please!',bg='#050505',fg='#ffffff',width=14,font=("Bahnschrift",25),border=7)
e.grid(row=0,column=0,columnspan=5,pady=6)
def buttonclick(number):
 if number==99:
   e.delete(0,END)
 elif number==100:
  global a
  a=None
  buttonclick(99)
 elif len(e.get())==0:
  e.insert(0,number)
 else:
  e.insert(len(e.get()), number)
 return
a=None
math=None
# Adding Function
def add():
 global a
 global math
 if a==None:
  a=float(e.get())
  e.delete(0,END)
 else:
  a=a+float(e.get())
  e.delete(0,END)
 math='add'
# SubstarctFunction
def subs():
 global a
 global math
 if a == None:
  a = float(e.get())
  e.delete(0, END)
 else:
  a = a-float(e.get())
  e.delete(0,END)
 math='sub'
 return
# Multiplication Function
def multiply():
 global a
 global math
 if a==None:
  a=float(e.get())
  e.delete(0,END)
 else:
  a=a*float(e.get())
  e.delete(0,END)
 math='multi'
 return
# Division Function
def divide():
 global a
 global math
 if a==None:
  a=float(e.get())
  e.delete(0,END)
 else:
  a=a/float(e.get())
  e.delete(0, END)
 math='divide'
 return
def display():
 global math
 global a
 if math=='add':
  if e.get()=='':
   e.insert(0,a)
  else:
   b=float(e.get())
   e.delete(0,END)
   e.insert(0,str(a+b))
  a=None
 elif math=='sub':
  if e.get() == '':
   e.insert(0, a)
  else:
   b=float(e.get())
   e.delete(0,END)
   e.insert(0,str(a-b))
  a=None
 elif math=='multi':
  if e.get() == '':
   e.insert(0, a)
  else:
   b=float(e.get())
   e.delete(0,END)
   e.insert(0, str(a * b))
  a=None
 elif math=='divide':
  if e.get() == '':
   e.insert(0, a)
  else:
   b=float(e.get())
   e.delete(0,END)
   e.insert(0, str(a / b))
  a=None
 return
def inverse():
 k = float(e.get()) * -1
 e.delete(0, END)
 e.insert(0, k)
 return
def point():
 e.insert(len(e.get()),'.')
 return
def delete():
 e.delete(len(e.get())-1,END)


button_0=Button(root,text='0',bg='#1316e8',fg='black',padx=17,pady=5,font = ("Bahnschrift", 20),command=lambda:buttonclick(0))
button_1=Button(root,text='1',bg='#1316e8',fg='black',padx=19,pady=5,font = ("Bahnschrift", 20),command=lambda:buttonclick(1))
button_2=Button(root,text='2',bg='#1316e8',fg='black',padx=16.5,pady=5,font = ("Bahnschrift", 20),command=lambda:buttonclick(2))
button_3=Button(root,text='3',bg='#1316e8',fg='black',padx=16,pady=5,font = ("Bahnschrift", 20),command=lambda:buttonclick(3))
button_4=Button(root,text='4',bg='#1316e8',fg='black',padx=15.5,pady=5,font = ("Bahnschrift", 20),command=lambda:buttonclick(4))
button_5=Button(root,text='5',bg='#1316e8',fg='black',padx=16,pady=5,font = ("Bahnschrift", 20),command=lambda:buttonclick(5))
button_6=Button(root,text='6',bg='#1316e8',fg='black',padx=16,pady=5,font = ("Bahnschrift", 20),command=lambda:buttonclick(6))
button_7=Button(root,text='7',bg='#1316e8',fg='black',padx=17,pady=5,font = ("Bahnschrift", 20),command=lambda:buttonclick(7))
button_8=Button(root,text='8',bg='#1316e8',fg='black',padx=16,pady=5,font = ("Bahnschrift", 20),command=lambda:buttonclick(8))
button_9=Button(root,text='9',bg='#1316e8',fg='black',padx=16,pady=5,font = ("Bahnschrift", 20),command=lambda:buttonclick(9))
button_10=Button(root,text='+',bg='#343e78',fg='black',padx=16,pady=5,font = ("Bahnschrift", 20),command=add)
button_11=Button(root,text='=',bg='#343e78',fg='black',padx=18,pady=5,font = ("Bahnschrift", 20),command=display)
button_12=Button(root,text='CLEAR',bg='#c41417',fg='black',padx=2,pady=15,font = ("Bahnschrift", 13),command=lambda:buttonclick(99))
button_13=Button(root,text='CE',bg='#c41417',fg='black',padx=18,pady=15,font = ("Bahnschrift", 13),command=lambda:buttonclick(100))
button_14=Button(root,text='-',bg='#343e78',fg='black',padx=17,pady=5,font = ("Bahnschrift", 20),command=subs)
button_15=Button(root,text='*',bg='#343e78',fg='black',padx=17,pady=5,font = ("Bahnschrift", 20),command=multiply)
button_16=Button(root,text='/',bg='#343e78',fg='black',padx=20,pady=5,font = ("Bahnschrift", 20),command=divide)
button_17=Button(root,text='+/-',bg='#32a891',fg='black',padx=6,pady=5,font = ("Bahnschrift", 20),command=inverse)
button_18=Button(root,text='.',bg='#32a891',fg='black',padx=20,pady=5,font = ("Bahnschrift", 20),command=point)
button_19=Button(root,text='DEL',bg='#c41417',fg='black',padx=0,pady=5,font = ("Bahnschrift", 20),command=delete)

button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)
button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)
button_1.grid(row=3,column=0)
button_3.grid(row=3,column=2)
button_2.grid(row=3,column=1)
button_10.grid(row=4,column=4)
button_0.grid(row=4,column=1)
button_11.grid(row=5,column=4)
button_12.grid(row=5,column=0)
button_13.grid(row=5,column=2)
button_14.grid(row=3,column=4)
button_15.grid(row=2,column=4)
button_16.grid(row=1,column=4)
button_17.grid(row=4,column=0)
button_18.grid(row=4,column=2)
button_19.grid(row=5,column=1)

root.mainloop()

