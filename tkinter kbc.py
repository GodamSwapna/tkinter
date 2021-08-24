import tkinter
from tkinter import *

questions=["which is the largest country in the world?",
           "how many days are there in aleap year?",
           "how many continents are there in the world?",
           "how many years are there in one millenium?",
           "ipad is manufactured by?"]

first_options=["india","354","7","100years","google"]

second_options=["USA","366","5","50 years","Amazon"]

third_option=["russia","420","6","75 years","microsoft"]

fourth_option=["china","8","365","150 years","apple"]

root=tkinter.Tk()
root.title("kbc")
root.geometry("1027x900")

root.config(bg="black")
leftframe=Frame(root,bg="black",pady=20)
leftframe.grid(row=0,column=0)

topframe=Frame(leftframe,pady=20)
topframe.grid()
centerframe=Frame(leftframe,pady=20)
centerframe.grid(row=1,column=0)
bottomframe=Frame(leftframe)
bottomframe.grid(row=2,column=0)
rightframe=Frame(root,pady=50,padx=20,bg="black")
rightframe.grid(row=0,column=1)
image50=PhotoImage(file='50-50.png')

lifeline50Button=Button(topframe,image=image50,bg="black",bd=0,activebackground="black",width=180,height=80)
lifeline50Button.grid(row=0,column=0)

audience=PhotoImage(file='audiencepole1.png')

audiencepoleButton=Button(topframe,image=audience,bg="black",bd=0,activebackground="black",width=180,height=80)
audiencepoleButton.grid(row=0,column=1)

phone=PhotoImage(file='phone.png')
phoneButton=Button(topframe,image=phone,bg="black",bd=0,activebackground="black",width=180,height=80)
phoneButton.grid(row=0,column=2)
centerimage=PhotoImage(file="center.png")

centerimageButton=Label(centerframe,image=centerimage,bg="black",width=300,height=200)
centerimageButton.grid(row=0,column=0)

phoneButton.grid(row=0,column=2)
amountimage=PhotoImage(file="picture_0.png",)
amountLable=Label(rightframe,image=amountimage,bg="black")
amountLable.grid(row=0,column=0)

layoutimage=PhotoImage(file="lay.png")
layoutLable=Label(bottomframe,image=layoutimage,bg="black")
layoutLable.grid(row=0,column=0)

questionArea=Text(bottomframe,font=('arial',18,'bold'),width=30,height=2,wrap='word',bg="black",fg="white",bd=0)
questionArea.place(x=70,y=10)

questionArea.insert(END,questions[0])
lableA=Label(bottomframe,text="A:",bg="black",fg="white",bd=0,font=("arial",16,"bold"))
lableA.place(x=60,y=110)

optionButton1=Button(bottomframe,text=first_options[0],font=("arial",18,"bold"),bg="black",fg="white",bd=0,activebackground="black",activeforeground="white",cursor="hand2")
optionButton1.place(y=100,x=100) 

lableB=Label(bottomframe,text="B:",bg="black",fg="white",bd=0,font=("arial",16,"bold"))
lableB.place(x=330,y=110)




optionButton2=Button(bottomframe,text=second_options[0],font=("arial",18,"bold"),bg="black",fg="white",bd=0,activebackground="black",activeforeground="white",cursor="hand2")
optionButton2.place(y=370,x=100)
lableC=Label(bottomframe,text="C:",bg="black",fg="white",bd=0,font=("arial",16,"bold"))
lableC.place(x=60,y=190)

optionButton3=Button(bottomframe,text=third_option[0],font=("arial",18,"bold"),bg="black",fg="white",bd=0,activebackground="black",activeforeground="white",cursor="hand2")
optionButton3.place(y=100,x=190)
lableD=Label(bottomframe,text="D:",bg="black",fg="white",bd=0,font=("arial",16,"bold"))
lableD.place(x=330,y=190)

optionButton4=Button(bottomframe,text=fourth_option[0],font=("arial",18,"bold"),bg="black",fg="white",bd=0,activebackground="black",activeforeground="white",cursor="hand2")
optionButton4.place(y=370,x=180)



root.mainloop()
