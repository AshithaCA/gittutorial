import tkinter as tk
import tkinter.ttk as ttk
import re
from tkinter import messagebox
window=tk.Tk()
window.geometry("500x300")
window.config(background='light blue')
a=tk.Label(text='REGISTRATION FORM',fg='black')
a.pack(side=tk.TOP)

a1=tk.Label(text='NAME',width=12)
a1.place(x=10, y=35)
nam=tk.Entry(fg='black')
nam.place(x=115, y=35)

a2=tk.Label(text='EMAIL ID',width=12)
a2.place(x=10, y=75)
email=tk.Entry(fg='black')
email.place(x=115, y=75)

a3=tk.Label(text='PHONE NO',width=12)
a3.place(x=10, y=115)
ph=tk.Entry(fg='black')
ph.place(x=115, y=115)

a4=tk.Label(text='PASSWORD',width=12)
a4.place(x=10, y=155)
pw=tk.Entry(fg='black')
pw.place(x=115, y=155)

a5=tk.Label(text='CONFORM PW',width=12)
a5.place(x=10, y=195)
cpw=tk.Entry(fg='black')
cpw.place(x=115, y=195)

# def name():
#     txt=nam.get()
#     x=re.findall('\d',txt)
#     y=re.findall('[@#$%&*^!]',txt)
#     print(txt)
#     if len(x) and len(y)!=0:
#             messagebox.showerror('invalid name','enter correct name')
def emailid():
    id=email.get() 
    a=re.findall('.com\Z',id)
    b=re.findall('.in\Z',id)
    c=re.search('@',id)
    if c!=None:
        print('......................')
        if a and b==[]:
            messagebox.showerror('invalid email','enter correct email')  
# def phone():
#     phon=ph.get()
#     d=re.findall('\D',phon)
#     if d!=[]:
#         messagebox.showerror('invalid phone no','enter correct phone no') 
# def password():
#     e=pw.get()
#     f=cpw.get()
#     if e!=f:
#         messagebox.showerror('password not matching','enter correct password')
        
         
bt=tk.Button(text='SUBMIT',command=emailid)
bt.place(x=115, y=235)

window.mainloop()