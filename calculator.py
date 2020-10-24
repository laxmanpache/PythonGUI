from tkinter import *
root=Tk()
root.title("Simple Calculator")

e= Entry(root,width=50,borderwidth=5)
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)

def Button_Click(number):

    #e.delete(0,END)
    current=e.get()
    e.delete(0,END)
    e.insert(0, str(current)+str(number))

def Button_clear():
    e.delete(0,END)

def Button_add():
    first_number=e.get()
    global f_num
    global math
    math='add'
    f_num=int(first_number)
    e.delete(0,END)
def Button_sub():
    first_number=e.get()
    global f_num
    global math
    math='sub'
    f_num=int(first_number)
    e.delete(0,END)



def Button_mul():

    first_number=e.get()
    global f_num, math
    math='mul'
    f_num=int(first_number)
    e.delete(0,END)



def Button_div():
    first_num=e.get()
    global f_num,math
    math='div'
    f_num=int(first_num)
    e.delete(0,END)

def Button_equal():
    secon_number = e.get()
    e.delete(0, END)
    if math=='add':
        e.insert(0,f_num+int(secon_number))
    if math=='sub':
         e.insert(0,f_num - int(secon_number))
    if math == 'mul':
        e.insert(0, f_num * int(secon_number))

    if math=='div':
        e.insert(0,f_num / int(secon_number))




button1= Button(root,text="1",padx=40,pady=20, command=lambda:Button_Click(1))
button2= Button(root,text="2",padx=40,pady=20, command=lambda:Button_Click(2))
button3= Button(root,text="3",padx=40,pady=20, command=lambda:Button_Click(3))
button4= Button(root,text="4",padx=40,pady=20, command=lambda:Button_Click(4))
button5= Button(root,text="5",padx=40,pady=20, command=lambda:Button_Click(5))
button6= Button(root,text="6",padx=40,pady=20, command=lambda:Button_Click(6))
button7= Button(root,text="7",padx=40,pady=20, command=lambda:Button_Click(7))
button8= Button(root,text="8",padx=40,pady=20, command=lambda:Button_Click(8))
button9= Button(root,text="9",padx=40,pady=20, command=lambda:Button_Click(9))
button0= Button(root,text="0",padx=40,pady=20, command=lambda:Button_Click(0))
button_add=Button(root,text="+",padx=39,pady=20 ,command=Button_add)
button_equal=Button(root,text="=",padx=91,pady=20,command=Button_equal)
button_clear=Button(root,text="clear",padx=85,pady=20 ,command=Button_clear)
button_sub=Button(root,text="-",padx=39,pady=20 ,command=Button_sub)
button_mul=Button(root,text="*",padx=39,pady=20 ,command=Button_mul)
button_div=Button(root,text="/",padx=39,pady=20 ,command=Button_div)




button1.grid(row=3,column=0)
button2.grid(row=3,column=1)
button3.grid(row=3,column=2)

button4.grid(row=2,column=0)
button5.grid(row=2,column=1)
button6.grid(row=2,column=2)

button7.grid(row=1,column=0)
button8.grid(row=1,column=1)
button9.grid(row=1,column=2)

button0.grid(row=4,column=0)
button_clear.grid(row=6,column=1,columnspan=2)

button_add.grid(row=5,column=0)
button_equal.grid(row=5,column=1,columnspan=2)
button_sub.grid(row=6,column=0)
button_mul.grid(row=4,column=1)
button_div.grid(row=4,column=2)
root.mainloop()