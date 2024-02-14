# import tkinter as tk

# # from tkinter import *

# # window=tk.Tk()
# # window.mainloop() 

# pack place grid

#1) grid

# window=tk.Tk()
# window.geometry('500x300')   #widthxheight
# # window.minsize(100,500)
# # window.maxsize(100,500)     #width,height

# a=tk.Label(text='Enter your name:')
# a.grid(row=4,column=3)

# ai=tk.Label(text='my name')
# ai.grid(row=19,column=3)

# name=tk.Entry(fg='black',bg='lightblue')
# name.grid(row=4,column=4)

# def hi():
#     # print('welcome')
#     na=name.get()
#     print(na)
#     # print(type(na))
#     # name.delete(1)        # index start cheyunnath 0 muthal ahnn  #1 indexil ulla letter or number delete akum
#     # name.insert(3,8)      # 3nd indexil 8 addon cheyth varum
#     # name.insert(tk.END,9)   # endil 9 addon cheyth varum
#     ai.config(text=na)
    
# # hello=tk.Label(text='hello',fg='blue',bg='yellow',width=10,height=1)
# # hello.grid(row=14,column=7)
  
# # wel=tk.Label(text='welcome')
# # wel.grid(row=18,column=3)

# btn=tk.Button(text='Click here',fg='white',bg='lightblue',width=10,height=1,command=hi)
# btn.grid(row=10,column=5)
# window.configure(bg='lightgreen')
# window.mainloop() 

#....................................


#2)themed widget

# import tkinter as tk

# import tkinter.ttk as ttk

# window=tk.Tk()
# window.geometry('200x500')

# txt1=tk.Text()
# txt1.grid(row=0,column=0)

# def display():
#     # s=txt1.get('1.4',tk.END)
#     # print(s)
#     # txt1.insert('2.1','1111')   #2nd row 1st index position 1111 addon akum
#     txt1.delete('2.1')    #2nd row 1st index position delete akum
    
# btn=tk.Button(text='Click',command=display)
# btn.grid(row=1,column=1)    


# # btn=tk.Label(text='Click here',fg='white',bg='black')
# # btn.grid(row=10,column=5)

# # btn1=ttk.Label(text='Click here',foreground='white',background='green')
# # btn1.grid(row=11,column=5)

# window.mainloop()

        #...................................Theme widget.............................................



# 1) combobox

# import tkinter as tk

# import tkinter.ttk as ttk

# window=tk.Tk()
# window.geometry('200x500')

# n=tk.StringVar()
# # n=tk.IntVar()

# place=ttk.Combobox(window,width=20,textvariable=n)
# place.grid(row=0,column=1)

# # place['values']=('elkm','tvm','kollam')
# place['values']=(1,2,3,4,5,6)
# place.current(0)

# def display():
#     p=place.get()
#     print(p)

# btn=ttk.Button(text='Click',command=display)
# btn.grid(row=1,column=1)
    
# window.mainloop()

#........................................................................ 

#2) check box

# import tkinter as tk

# import tkinter.ttk as ttk

# window=tk.Tk()
# window.geometry('200x500')

# # cbool=tk.BooleanVar()
# # cbool.set(True)

# # cbool=tk.IntVar()
# # cbool.set(7)

# chk=ttk.Checkbutton(window,text='male',var=cbool)
# chk.grid(row=1,column=1)


# def display():
#     # a=chk.state()
#     a=chk.instate(['selected'])
#     print(a)

# btn=ttk.Button(text='Click',command=display)
# btn.grid(row=2,column=1)
# window.mainloop()

#........................................................................

#3) Radiobutton


# import tkinter as tk
# import tkinter.ttk as ttk
# window=tk.Tk()

# selected=tk.IntVar()
# # selected1=tk.IntVar()
# selected1=tk.StringVar()
# rad1=tk.Radiobutton(window,text='first',variable=selected,value=1)
# rad1.grid(row=1,column=1)
# rad1=tk.Radiobutton(window,text='second',variable=selected,value=2)
# rad1.grid(row=1,column=2)
# rad1=tk.Radiobutton(window,text='third',variable=selected1,value='third')
# rad1.grid(row=2,column=1)
# rad1=tk.Radiobutton(window,text='fourth',variable=selected1,value='four')
# rad1.grid(row=2,column=2)

# def display():
#         print(selected.get())
#         print(selected1.get())
        
# btn=ttk.Button(text='Click',command=display)
# btn.grid(row=5,column=1)

# window.mainloop()

#........................................................................


#4)scrolltext

# import tkinter as tk
# import tkinter.ttk as ttk
# window=tk.Tk()

# from tkinter import scrolledtext

# st=scrolledtext.ScrolledText(window,width=5,height=6)
# st.grid(row=1,column=2)

# def display():
#     na=st.get('1.2',tk.END)
#     print(na)
# #     #print(type(na))
# #     #name.delete(1)        
# #     #name.insert(3,8)      
# #     #name.insert(tk.END,9)   
# btn=ttk.Button(text='Click',command=display)
# btn.grid(row=2,column=1)

# window.mainloop()

#........................................................................


#5)message box

import tkinter as tk
import tkinter.ttk as ttk
window=tk.Tk()

from tkinter import messagebox
def display():
        # messagebox.showinfo('title','content')
        # messagebox.showwarning('title','content')
        messagebox.showerror('title','content')
        
btn=ttk.Button(text='Click',command=display)
btn.grid(row=2,column=1)
window.mainloop()

#........................................................................


#6)progressbar

# import tkinter as tk
# import tkinter.ttk as ttk
# window=tk.Tk()
# from tkinter.ttk import Progressbar

# bar=Progressbar(window,length=200) 
# bar['value']=99
# bar.grid(row=1,column=2)
# window.mainloop()

#.......................................................................

# MENU

# import tkinter as tk
# import tkinter.ttk as ttk
# from tkinter import Menu

# window=tk.Tk()
# window.geometry('500x300')
# def n():
#         print('hai')
# menubar= Menu(window)
# filemenu=Menu(menubar)
# filemenu.add_command(label='New',command=n)
# filemenu.add_command(label='Open')
# filemenu.add_command(label='Save')
# filemenu.add_separator()
# filemenu.add_command(label='Close')
# menubar.add_cascade(label='File',menu=filemenu)

# editmenu=Menu(menubar)
# editmenu.add_command(label='Undo')
# editmenu.add_command(label='Redo')
# editmenu.add_command(label='Cut')
# menubar.add_cascade(label='Edit',menu=editmenu)

# window.config(menu=menubar)  #menu like file and edit come to the windows
# window.mainloop()

#place


# from tkinter import*
# root = Tk()

# root.geometry('250x200+550+100')    #+x axis postion+ yaxis postion
# Label(root, text='ashitha',bg='#FFFF00', fg='red').place(x=45, y=10)
# Label(root, text='ashi',bg='#FFFF00', fg='red').place(x=90, y=50)


# root.mainloop()

#pack

# from tkinter import*
# import tkinter as tk

# root = Tk()

# root.geometry('250x200+550+100')
# # test=tk.Label(root, text='red',bg='red',fg='white')
# # test.pack(side=tk.RIGHT)
# # test=tk.Label(root, text='pink',bg='pink',fg='white')
# # test.pack(side=tk.TOP)
# # test=tk.Label(root, text='blue',bg='blue',fg='white')
# # test.pack(side=tk.BOTTOM)

# # Label(root, text='black',bg='lightblue',fg='black').pack(padx=20, pady=50, side=LEFT)
# Label(root, text='ashi',bg='#FFFF00', fg='red').pack(padx=20, pady=50, side=LEFT)
# root.mainloop()