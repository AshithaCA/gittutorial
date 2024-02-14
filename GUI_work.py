# import tkinter as tk

# window=tk.Tk()

# a=tk.Label(text='Enter any number1:')
# a.grid(row=4,column=3)

# num1=tk.Entry(fg='black',bg='lightblue')
# num1.grid(row=4,column=4)

# a2=tk.Label(text='Enter any number2:')
# a2.grid(row=6,column=3)

# num2=tk.Entry(fg='black',bg='lightblue')
# num2.grid(row=6,column=4)

# ans=tk.Label(text='Answer',fg='black',bg='lightblue',height=2)
# ans.grid(row=8,column=6)

# def ADD():
#     no=num1.get()
#     no1=num2.get()
#     print(int(no)+int(no1))
#     ans.config(text=int(no)+int(no1))
# def SUB():
#     no=num1.get()
#     no1=num2.get()
#     print(int(no)-int(no1))
#     ans.config(text=int(no)-int(no1))
# def MUL():
#     no=num1.get()
#     no1=num2.get()
#     print(int(no)*int(no1))
#     ans.config(text=int(no)*int(no1))
# def DIV():
#     no=num1.get()
#     no1=num2.get()
#     print(int(no)/int(no1))
#     ans.config(text=int(no)/int(no1))

   

# bt1=tk.Button(text='ADD',fg='black',bg='lightblue',width=10,height=1,command=ADD)
# bt1.grid(row=7,column=3)
# bt2=tk.Button(text='SUB',fg='black',bg='lightblue',width=10,height=1,command=SUB)
# bt2.grid(row=7,column=4)
# bt3=tk.Button(text='MULT',fg='black',bg='lightblue',width=10,height=1,command=MUL)
# bt3.grid(row=8,column=3)
# bt4=tk.Button(text='DIV',fg='black',bg='lightblue',width=10,height=1,command=DIV)
# bt4.grid(row=8,column=4)

# window.mainloop() 
#.........................................................


# import tkinter as tk
# window=tk.Tk()

# num1=tk.Label(fg='black',bg='lightblue',width=10,height=1)
# num1.grid(row=0,column=2)

# bt=tk.Button(text='00',fg='black',bg='lightblue',width=10,height=1)
# bt.grid(row=4,column=0)
# bt0=tk.Button(text='.',fg='black',bg='lightblue',width=10,height=1)
# bt0.grid(row=4,column=1)
# bt0=tk.Button(text=0,fg='black',bg='lightblue',width=10,height=1)
# bt0.grid(row=4,column=2)
# bt1=tk.Button(text=1,fg='black',bg='lightblue',width=10,height=1)
# bt1.grid(row=3,column=0)
# bt2=tk.Button(text=2,fg='black',bg='lightblue',width=10,height=1)
# bt2.grid(row=3,column=1)
# bt3=tk.Button(text=3,fg='black',bg='lightblue',width=10,height=1)
# bt3.grid(row=3,column=2)
# bt4=tk.Button(text=4,fg='black',bg='lightblue',width=10,height=1)
# bt4.grid(row=2,column=0)
# bt5=tk.Button(text=5,fg='black',bg='lightblue',width=10,height=1)
# bt5.grid(row=2,column=1)
# bt6=tk.Button(text=6,fg='black',bg='lightblue',width=10,height=1)
# bt6.grid(row=2,column=2)
# bt7=tk.Button(text=7,fg='black',bg='lightblue',width=10,height=1)
# bt7.grid(row=1,column=0)
# bt8=tk.Button(text=8,fg='black',bg='lightblue',width=10,height=1)
# bt8.grid(row=1,column=1)
# bt9=tk.Button(text=9,fg='black',bg='lightblue',width=10,height=1)
# bt9.grid(row=1,column=2)


# S1=tk.Button(text='x',fg='black',bg='lightblue',width=10,height=1)
# S1.grid(row=1,column=3)
# S2=tk.Button(text='-',fg='black',bg='lightblue',width=10,height=1)
# S2.grid(row=2,column=3)
# S3=tk.Button(text='+',fg='black',bg='lightblue',width=10,height=1)
# S3.grid(row=3,column=3)
# S4=tk.Button(text='/',fg='black',bg='lightblue',width=10,height=1)
# S4.grid(row=4,column=3)
# S5=tk.Button(text='%',fg='black',bg='lightblue',width=10,height=1)
# S5.grid(row=5,column=2)
# S6=tk.Button(text='=',fg='black',bg='lightblue',width=10,height=1)
# S6.grid(row=5,column=3)
# S6=tk.Button(text='B',fg='black',bg='lightblue',width=10,height=1)
# S6.grid(row=5,column=1)
# S6=tk.Button(text='( )',fg='black',bg='lightblue',width=10,height=1)
# S6.grid(row=5,column=0)


# window.mainloop()

#.............................................................................................

# import tkinter as tk

# import tkinter.ttk as ttk


# window=tk.Tk()

# window.geometry("500x300")
# window.minsize(400,400)
# window.maxsize(900,900)

# txt=ttk.Entry(width=20)
# txt.grid(row=0,column=0,columnspan=5)

# def one():
#     chk()
#     txt.insert(tk.END,'1')

# def two():
#     chk()
#     txt.insert(tk.END,'2')

# def three():
#     chk()
#     txt.insert(tk.END,'3')

# def four():
#     chk()
#     txt.insert(tk.END,'4')

# def five():
#     chk()
#     txt.insert(tk.END,'5')

# def six():
#     chk()
#     txt.insert(tk.END,'6')

# def seven():
#     chk()
#     txt.insert(tk.END,'7')

# def eight():
#     chk()
#     txt.insert(tk.END,'8')

# def nine():
#     chk()
#     txt.insert(tk.END,'9')

# def zero():
#     n=txt.get()
#     if len(n)==1 and n[0]=='0':
#         txt.delete(0,tk.END)
#     a=txt.insert(tk.END,'0')
    
    
# def chk():
#     n=txt.get()
#     if len(n)==1 and n[0]=='0':
#         txt.delete(0,tk.END)
    

# def bracket1():
#     txt.insert(tk.END,'(')

# def bracket2():
#     txt.insert(tk.END,'(')


# def point():
#     txt.insert(tk.END,'.')


# def plus():
#     op()
#     txt.insert(tk.END,'+')


# def minus():
#     op()
#     txt.insert(tk.END,'-')

# def mul():
#     op()
#     txt.insert(tk.END,'*')


# def div():
#     op()
#     txt.insert(tk.END,'/')



# def eqn():
#     a=txt.get()
#     ans=eval(a)
#     txt.delete(0,tk.END)
#     txt.insert(tk.END,ans)


# def clear():
#     txt.delete(0,tk.END)
    
# def backspace():
#     a=txt.get()
#     txt.delete(len(a)-1)


# def op():
#     a=txt.get()
#     if a[-1] in '+-/*':
#         txt.delete(len(a)-1)

# btnAC=tk.Button(text='AC',fg='black',bg='lavender',width=3,height=1,command=clear)
# btnAC.grid(row=2,column=0)

# btnP=tk.Button(text='.',fg='blue',bg='lavender',width=3,height=1,command=point)
# btnP.grid(row=2,column=1)

# btnBS=tk.Button(text='BS',fg='black',bg='lavender',width=3,height=1,command=backspace)
# btnBS.grid(row=2,column=2)


# btnE=tk.Button(text='=',fg='black',bg='lavender',width=3,height=1,command=eqn)
# btnE.grid(row=2,column=3)

# btn0=tk.Button(text='0',fg='red',bg='lavender',width=3,height=1,command=zero)
# btn0.grid(row=6,column=1)

# btnB1=tk.Button(text='(',fg='red',bg='lavender',width=3,height=1,command=bracket1)
# btnB1.grid(row=6,column=0)

# btnB2=tk.Button(text=')',fg='red',bg='lavender',width=3,height=1,command=bracket2)
# btnB2.grid(row=6,column=2)

# btn1=tk.Button(text='1',fg='red',bg='lavender',width=3,height=1,command=one)
# btn1.grid(row=3,column=0)

# btn2=tk.Button(text='2',fg='red',bg='lavender',width=3,height=1,command=two)
# btn2.grid(row=3,column=1)

# btn3=tk.Button(text='3',fg='red',bg='lavender',width=3,height=1,command=three)
# btn3.grid(row=3,column=2)


# btn4=tk.Button(text='4',fg='red',bg='lavender',width=3,height=1,command=four)
# btn4.grid(row=4,column=0)

# btn5=tk.Button(text='5',fg='red',bg='lavender',width=3,height=1,command=five)
# btn5.grid(row=4,column=1)

# btn6=tk.Button(text='6',fg='red',bg='lavender',width=3,height=1,command=six)
# btn6.grid(row=4,column=2)

# btn7=tk.Button(text='7',fg='red',bg='lavender',width=3,height=1,command=seven)
# btn7.grid(row=5,column=0)

# btn8=tk.Button(text='8',fg='red',bg='lavender',width=3,height=1,command=eight)
# btn8.grid(row=5,column=1)

# btn9=tk.Button(text='9',fg='red',bg='lavender',width=3,height=1,command=nine)
# btn9.grid(row=5,column=2)

# btnL=tk.Button(text='+',fg='blue',bg='lavender',width=3,height=1,command=plus)
# btnL.grid(row=3,column=3)

# btnM=tk.Button(text='-',fg='blue',bg='lavender',width=3,height=1,command=minus)
# btnM.grid(row=4,column=3)

# btnX=tk.Button(text='x',fg='blue',bg='lavender',width=3,height=1,command=mul)
# btnX.grid(row=5,column=3)

# btnD=tk.Button(text='/',fg='blue',bg='lavender',width=3,height=1,command=div)
# btnD.grid(row=6,column=3)

# window.mainloop()