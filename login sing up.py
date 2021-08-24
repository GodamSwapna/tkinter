import tkinter
from tkinter import*
# import sqlite3


root=tkinter.Tk()
root.title("login form")
root.geometry("600x300")
root.configure(bg="blue")
def validate():
    username1=text_username.get()
    password1=text_password.get()
    if username1=="Godamswapna" and password1=="swa@pna1":
        
        Message.showinfo(username1,"logged successfully")
    else:
        Message.showinfo(username1,"wrong credential")

username=Label(root,text="User Name",fg="white",bg="black",font="bold,15")
username.place(x=100,y=60)
password=Label(root,text="password",fg="white",bg="black",font="bold,15")
password.place(x=100,y=90)
text_username=Entry()
text_username.place(x=200,y=60)
text_password=Entry()
text_password.place(x=200,y=90)
submit=Button(root,text="submit",comman=validate)
submit.place(x=200,y=140)

root.mainloop()


# window=tkinter.Tk()
# window.geometry("300x300")
# def login():
#     print("")
# def signup():

#     def signup_database():
#         conn=sqlite3.connect("1.db")
#         cur=conn.cursor()
#         cur.execute("CREATE TABLE IF NOT EXISTS test(id INTEGER PRIMARY KEY,name text email text password text)")
#         cur.execute("INSERT INTO test Valuess(Null,?,?,?)",(e1.get(),e2.get(),e3.get()))
#         l4=Label(signup_window,text="account created",font="times 15")
#         l4.grid(row=6,column=2)
#         conn.commit()
#         conn.close()
#     window.destroy()
#     signup_window=tkinter.Tk()
#     signup_window.geometry("400x250")
#     l1=Label(signup_window,text="user name",font="times 20")
#     l1.grid(row=1,column=1)
#     l2=Label(signup_window,text="user email",font="times 20")
#     l2.grid(row=2,column=1)
#     l3=Label(signup_window,text="userpassword",font="times 20")
#     l3.grid(row=3,column=1)

#     name_text=StringVar()
#     e1=Entry(signup_window,textvariable=name_text)
#     e1.grid(row=1,column=2)
#     email_text=StringVar()
#     e2=Entry(signup_window,textvariable=email_text)
#     e2.grid(row=2,column=2)
#     password_text=StringVar()
#     e3=Entry(signup_window,textvariable=password_text)
#     e3.grid(row=3,column=2)

#     b1=Button(signup_window,text="login",width=20,command=signup_database)
#     b1.grid(row=4,column=2)







# l1=Label(window,text="what do you want to do",font="times 20")
# l1.grid(row=1,column=2,columnspan=2)

# b1=Button(window,text="login",width=20,command=login)
# b1.grid(row=2,column=2)

# b2=Button(window,text="signup",width=20,command=signup)
# b2.grid(row=2,column=3)
# window.mainloop()


