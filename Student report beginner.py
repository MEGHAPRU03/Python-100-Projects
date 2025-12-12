from tkinter import *
w1= Tk()
w1.title('Student report card')
w1.geometry('600x600-100+40')
w1.resizable(width=0, height=0)
w1.configure(background='yellow')

def py():
    namer=name.get()
    sum = Hindi.get() + English.get() + math.get() + science.get() + stt.get()
    sum1= int(sum)
    sum11 = f'{sum1}/500'
    per= (sum1/500)*100
    # print(sum,per)
    a= Toplevel(w1)
    a.title('Student Details')
    # a.configure(background='#fff6ec')

    l2=Label(a,text=' Student Name : ',fg='black')
    l2.grid(row=0,column=0)
    Label(a, text=namer,fg='black').grid(row=0,column=1)
    Label(a,text='Total marks : ').grid(row=1,column=0)
    Label(a,text= sum11,fg='black').grid(row=1,column=1)
    Label(a, text='Percentage : ').grid(row=2,column=0)
    Label(a, text=per,fg='black').grid(row=2,column=1)
    a.mainloop()

l1=Label(w1,text='Student Report Card',font=('Calibiri',31,'bold'),fg='black',bg='yellow')
l1.place(x=0,y=0,height=100,width=600)
f1 =Frame(w1,bg='yellow')
f1.place(x=0,y=100,height=80,width=600)
l2=Label(f1,text='Student Name',bg='#D3D3D3',fg='black',font=('Arial',20,'bold'))
l2.grid(row=0,column=0,padx=30,pady=20)
name= StringVar()
e1=Entry(f1,bg='#fff6ec',fg='black',relief='ridge',font=('Arial',20,'bold'),width=22,textvariable=name)
e1.grid(row=0,column=1)


label2=Label(w1,text='Student Number',bg='red',fg='black',font=('Calibiri',22,'bold'))
label2.place(x=0,y=170,width=600,height=50)


f2=Frame(w1,bg='yellow')
f2.place(x=0,y=221,height=350,width=600)
Hindi=DoubleVar()
English=DoubleVar()
science=DoubleVar()
math=DoubleVar()
stt=DoubleVar()

l1f2=Label(f2,text='Hindi',bg='#D3D3D3',fg='black',font=('Calibri',20),height=1,width=12,pady=3,padx=5)
l1f2.grid(row=0,column=0,padx=30, pady=10)
e1f2= Entry(f2,bg='#fff6ec',font=('Arial',20,'bold'),width=22,textvariable=Hindi)
e1f2.grid(row=0,column=1,padx=5,pady=5)

l2f2=Label(f2,text='English',bg='#D3D3D3',fg='black',font=('Calibri',20),height=1,width=12,pady=3,padx=5)
l2f2.grid(row=1,column=0,padx=30, pady=10)
e2f2= Entry(f2,bg='#fff6ec',font=('Arial',20,'bold'),width=22,textvariable=English)
e2f2.grid(row=1,column=1,padx=5,pady=5)

l3f2=Label(f2,text='Science',bg='#D3D3D3',fg='black',font=('Calibri',20),height=1,width=12,pady=3,padx=5)
l3f2.grid(row=2,column=0,padx=30, pady=10)
e3f2= Entry(f2,bg='#fff6ec',font=('Arial',20,'bold'),width=22,textvariable=science)
e3f2.grid(row=2,column=1,padx=5,pady=5)

l4f2=Label(f2,text='Math',bg='#D3D3D3',fg='black',font=('Calibri',20),height=1,width=12,pady=3,padx=5)
l4f2.grid(row=3,column=0,padx=30, pady=10)
e4f2= Entry(f2,bg='#fff6ec',font=('Arial',20,'bold'),width=22,textvariable=math)
e4f2.grid(row=3,column=1,padx=5,pady=5)

l5f2=Label(f2,text='SST',bg='#D3D3D3',fg='black',font=('Calibri',20),height=1,width=12,pady=3,padx=5)
l5f2.grid(row=4,column=0,padx=30, pady=10)
e5f2= Entry(f2,bg='#fff6ec',font=('Arial',20,'bold'),width=22,textvariable=stt)
e5f2.grid(row=4,column=1,padx=5,pady=5)

b2=Button(w1,text='Done',fg='black',bg='#fff7ec',relief="raised",width=14,font=('Calibri',16,'bold'),command=py)
b2.place(x=200,y=540)
w1.mainloop()
