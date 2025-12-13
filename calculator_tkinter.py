#calculator
import math
from tkinter import *
from math import *

w1= Tk()
w1.geometry('480x600-100+50')
w1.resizable(width=0, height=0)
#-------------------------------------------------------------------------------------------------------------------------------
# variables
equation = StringVar()
expression = ''
#-------------------------------------------------------------------------------------------------------------------------------
# functions
def pie():
    global expression
    res = str(math.pi)
    equation.set(res)
    expression = res

def e():
    global expression
    res = str(math.e)
    equation.set(res)
    expression = res

def clear():
    global expression
    expression = ''
    equation.set(expression)

def backspace():
    global expression
    expression = expression[:-1]
    equation.set(expression)

def one_by_x():
    global expression
    try:
        res= 1/float(eval(expression))
        equation.set(str(res))
        expression = str(res)
    except:
        expression = ''
        equation.set(expression)

def abss():
    global expression
    try:
        res= math.abs(eval(expression))
        equation.set(str(res))
        expression= str(res)
    except:
        expression = ''
        equation.set(expression)
def expo():
    global expression
    res= math.exp(eval(expression))
    equation.set(str(res))
    expression = str(res)
def modd():
    global expression
    try:
        expression = expression + '%'
        equation.set(str(res))
        expression = str(res)
    except:
        expression = ''
        equation.set(expression)

def press(val):
    global expression
    expression += str(val)
    equation.set(expression)
def fact():
    global expression
    try:
        res= math.factorial(eval(expression))
        equation.set(str(res))
        expression = str(res)
    except:
        expression = ''
        equation.set(expression)
def neg():
    global expression
    res = -1 * eval(expression)
    equation.set(str(res))
    expression = str(res)
def equals():
    global expression
    try:
        res= eval(expression)
        equation.set(str(res))
        expression = str(res)
    except:
        expression = ''
        equation.set(expression)

#-------------------------------------------------------------------------------------------------------------------------------
# buttons list
b_list = [ ['pi',pie,0,0,],['e',e,0,1],['c',clear,0,2],['back',backspace,0,3],
['1/x',one_by_x,1,0],['|x|',abss,1,1],['exp',expo,1,2],['mod',modd,1,3],
['(',lambda: press('('),2,0],[')',lambda: press(')'),2,1],['n!',fact,2,2],['/',lambda: press('/'),2,3],
['7',lambda: press('7'),3,0],['8',lambda: press('8'),3,1],['9',lambda: press('9'),3,2],['*',lambda: press('*'),3,3],
['4',lambda: press('4'),4,0],['5',lambda: press('5'),4,1],['6',lambda: press('6'),4,2],['-',lambda: press('-'),4,3],
['1',lambda: press('1'),5,0],['2',lambda: press('2'),5,1],['3',lambda: press('3'),5,2],['+',lambda: press('+'),5,3],
['+/-',neg,6,0],['0',lambda: press('0'),6,1],['.',lambda: press('.'),6,2],['=',equals,6,3]
]
#-------------------------------------------------------------------------------------------------------------------------------
#layout
e1= Entry(w1,textvariable=equation,width=480,font=('Arial',40,'bold'),bd=5,relief='sunken',fg='black',justify='right',state='readonly')
e1.pack(padx=10,ipady=8,ipadx=5,pady=8)

f1= Frame(w1,width=480,height=500)
f1.pack(padx=10,ipady=8,ipadx=5,pady=10)

for but,cmdd,r1,c1 in b_list:
    b1= Button(f1,text=but,command=cmdd,height=3,width=10,bg='#fff6ec', fg= 'black',font=('Arial',10,'bold'),padx=3,pady=3.2)
    b1.grid(row=r1,column=c1)
    if but== '=' :
        b1 = Button(f1, text=but, command=cmdd, height=3, width=10,bg='blue', fg='black',
                    font=('Calibri', 10, 'bold'),padx=3,pady=3.2)
        b1.grid(row=r1, column=c1)



#-------------------------------------------------------------------------------------------------------------------------------

w1.mainloop()
