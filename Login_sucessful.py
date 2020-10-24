from tkinter import *
from tkinter import messagebox
import sqlite3

root=Tk()
root.title("Login System")
root.geometry("1120x700+0+0")
conn=sqlite3.connect("information1.db")
c=conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS  info(Name text,password text, mobile text,gender text)")
conn.commit()

def home():
    f1=Frame(root)
    f1.place(x=0,y=0,width=1120,height=700)
    login_btn=Button(f1,text="Login",bg="green",fg="red",command=login)
    login_btn.place(x=0,y=0,width=100,height=50)
    sign_up_btn=Button(f1,text="Sign Up",bg="green",fg="red",command=sign)
    sign_up_btn.place(x=0,y=55,width=100,height=50)

def validation():
     username_txt=un_e.get()
     password_txt=pas_e.get()
     c.execute("select name from info")

     r=c.fetchone()
     c.execute("select password from info")
     p=c.fetchone()
     conn.commit()
     if username_txt=="" and password_txt=="":
         messagebox.showerror("Error","Both field are empty")
     if username_txt==r[0]  and password_txt=="":
         messagebox.showerror("Error", "password field are empty")
     if username_txt==""  and password_txt==p[0]:
         messagebox.showerror("Error", "username field are empty")
     if username_txt!=r[0]  or password_txt!=p[0]:
         messagebox.showerror("Error", "Check username and password")
     if username_txt==r[0]  and password_txt==p[0]:
         messagebox.showinfo("information", "you signin sucessfully")

def login():
    global un_e,pas_e
    f2=Frame(root)
    f2.place(x=0,y=0,width=1120,height=700)
    un_l=Label(f2,text="Username",font=("times in new roman",20,"bold")).grid(row=1,column=1,padx=20,pady=20)
    un_e=Entry(f2,width=50)
    un_e.grid(row=1,column=2)

    pas_l=Label(f2,text="Password",font=("times in new roman",20,"bold")).grid(row=2,column=1,padx=20,pady=20)
    pas_e = Entry(f2, width=50)
    pas_e.grid(row=2, column=2)

    sub_btn=Button(f2,text="submit",bg="green",fg="red",command=validation).grid(row=3,column=2)

def action():
    name = u_name_entry.get()
    passwo =passw.get()
    Mobile=mobile_no_e.get()
    Gender=gender.get()

    c.execute("insert into info values('"+name+"','"+passwo+"','"+Mobile+"','"+Gender+"')")
    messagebox.showinfo("information","Your responce recorded")
    conn.commit()
    conn.close()

def sign():
    global u_name_entry,passw,mobile_no_e,gender
    f3=Frame(root)
    f3.place(x=0,y=0,width=1120,height=700)
    u_name=Label(f3,text="Name",font=("times in new roman",20,"bold")).grid(row=0,column=1,padx=30,pady=20)
    u_name_entry=Entry(f3,width=30)
    u_name_entry.grid(row=0,column=2)


    passw1=Label(f3,text="Password",font=("times in new roman",20,"bold")).grid(row=1,column=1,padx=30,pady=20)
    passw=Entry(f3,width=30)
    passw.grid(row=1,column=2)



    mobile_no=Label(f3,text="Mobile N",font=("times in new roman",20,"bold")).grid(row=2,column=1,padx=30,pady=20)
    mobile_no_e=Entry(f3,width=30)
    mobile_no_e.grid(row=2,column=2)

    gen = Label(f3, text="Select Gender", font=("times in new roman", 20, "bold")).grid(row=3, column=1, padx=30,
                                                                                             pady=20)
    gender=StringVar()
    g1= Radiobutton(f3,text="Male",variable=gender,value="Male",font="time 15")
    g1.deselect()
    g1.grid(row=3,column=2)
    g2= Radiobutton(f3,text="Female",variable=gender,value="Female",font="time 15")
    g2.select()
    g2.grid(row=3,column=3)


    sub_s_btn = Button(f3, text="submit", bg="green", fg="red",command=action)
    sub_s_btn.grid(row=4, column=2)
    exit_btn = Button(f3,text="Exit",bg="red",fg="white",command=f3.quit).grid(row=4,column=3)


home()


root.mainloop()