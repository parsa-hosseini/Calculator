from tkinter import *
from tkinter import messagebox
win = Tk()
win.resizable(0 , 0)
win.geometry('400x600')
win.title('Calculator')
win.configure(bg = '#75ACEF')

def b_1():
    if eam.get() == '':
        e1.insert(END , '1')
    else: 
        e2.insert(END , '1')
def b_2():
    if eam.get() == '':
        e1.insert(END , '2')
    else: 
        e2.insert(END , '2')
def b_3():
    if eam.get() == '':
        e1.insert(END , '3')
    else: 
        e2.insert(END , '3')
def b_4():
    if eam.get() == '':
        e1.insert(END , '4')
    else: 
        e2.insert(END , '4')
def b_5():
    if eam.get() == '':
        e1.insert(END , '5')
    else: 
        e2.insert(END , '5')
def b_6():
    if eam.get() == '':
        e1.insert(END , '6')
    else: 
        e2.insert(END , '6')
def b_7():
    if eam.get() == '':
        e1.insert(END , '7')
    else: 
        e2.insert(END , '7')
def b_8():
    if eam.get() == '':
        e1.insert(END , '8')
    else: 
        e2.insert(END , '8')
def b_9():
    if eam.get() == '':
        e1.insert(END , '9')
    else: 
        e2.insert(END , '9')
def b_0():
    if eam.get() == '':
        e1.insert(END , '0')
    else: 
        e2.insert(END , '0')
def c_l_s():
    e1.delete(0 , END)
    e2.delete(0 , END)
    e3.delete(0 , END)
    eam.delete(0 , END)
def b_fl():
    if eam.get() == '':
        e1.insert(END , '.')
    else: 
        e2.insert(END , '.')
def b_p():
    eam.insert(END , '+')
def b_x():
    eam.insert(END , '*')
def b_t():
    eam.insert(END , '/')
def b_f():
    eam.insert(END , '-')
def in_get():
    e3.delete(0 , END)
    a = float(e1.get())
    b = float(e2.get())
    if eam.get() == '+':
        n1 = a + b
        e3.insert(END , f' = {n1}')
    elif eam.get() == '-':
        n2 = a - b
        e3.insert(END , f' = {n2}')
    elif eam.get() == '/':
        n3 = a / b
        e3.insert(END , f' = {n3}') 
    elif eam.get() == '*':
        n4 = a * b
        e3.insert(END , f' = {n4}')        
    else:
        messagebox.showerror('WARNING!' , 'Pleas enter a true oparator')
        eam.delete(0 , END)

e1 = Entry(win , width = 22 , borderwidth = 20)
e1.place(x = 5 , y = 5)
e2 = Entry(win , width = 22 , borderwidth = 20)
e2.place(x = 220 , y = 5)
eam = Entry(win , width = 4)
eam.place(x = 185 , y = 23)
e3 = Entry(win , width = 54 , borderwidth = 30)
e3.place(x = 6 , y = 82)
b1 = Button(win , text = '1' , width = 10 , height = 4 , command = b_1)
b1.place(x = 10 , y = 190)
b2 = Button(win , text = '2' , width = 10 , height = 4 , command = b_2)
b2.place(x = 95 , y = 190)
b3 = Button(win , text = '3' , width = 10 , height = 4 , command = b_3)
b3.place(x = 180 , y = 190)
bx = Button(win , text = 'x' , width = 10 , height = 4 , command = b_x)
bx.place(x = 290 , y = 190)
b4 = Button(win , text = '4' , width = 10 , height = 4 , command = b_4)
b4.place(x = 10 , y = 280)
b5 = Button(win , text = '5' , width = 10 , height = 4 , command = b_5)
b5.place(x = 95 , y = 280)
b6 = Button(win , text = '6' , width = 10 , height = 4 , command = b_6)
b6.place(x = 180 , y = 280)
bt = Button(win , text = '÷' , width = 10 , height = 4 , command = b_t)
bt.place(x = 290 , y = 280)
b7 = Button(win , text = '7' , width = 10 , height = 4 , command = b_7)
b7.place(x = 10 , y = 370)
b8 = Button(win , text = '8' , width = 10 , height = 4 , command = b_8)
b8.place(x = 95 , y = 370)
b9 = Button(win , text = '9' , width = 10 , height = 4 , command = b_9)
b9.place(x = 180 , y = 370)
bf = Button(win , text = '-' , width = 10 , height = 4 , command = b_f)
bf.place(x = 290 , y = 370)
b0 = Button(win , text = '0' , width = 10 , height = 4 , command = b_0)
b0.place(x = 10 , y = 460)
bfl = Button(win , text = '.' , width = 10 , height = 4 , command = b_fl)
bfl.place(x = 95 , y = 460)
bi = Button(win , text = '=' , width = 10 , height = 4 , command =in_get)
bi.place(x = 180 , y = 460)
bp = Button(win , text = '+' , width = 10 , height = 4 , command = b_p)
bp.place(x = 290 , y = 460)
bc = Button(win , text = 'c' , width = 50 , height = 2 , command = c_l_s)
bc.place(x = 10 , y = 540)

win.mainloop()