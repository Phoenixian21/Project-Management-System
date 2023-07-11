from tkinter import *
from tkinter import messagebox
from PIL import ImageTk

def login():
    if userentry.get()=='' or passentry.get()=='':
        messagebox.showerror('Error','Fields cannot be Empty')
    elif userentry.get()=='aditya' and passentry.get()=='1234':
        messagebox.showinfo("Welcome ","Welcome Group Leader")
        window.destroy()
        import trial

    else :
        messagebox.showerror('Error','Invalid Credetials')

def viewget():
    window.destroy()
    import viewer

window=Tk()
window.geometry('1200x700+0+0')
window.title('ProjectManagement')

backimg=ImageTk.PhotoImage(file='front.jpg')
lo= Label(window,image=backimg)
lo.place(x=0,y=0)

logframe=Frame(window,bg='white')
logframe.place(x=500,y=200)


logoimage=PhotoImage(file='vit.png',)
logolabel=Label(logframe,image=logoimage)
logolabel.grid(row=0,column=0,columnspan=2)
userimage=PhotoImage(file='user.png')
passimage=PhotoImage(file='pass.png')
usernamelabel=Label(logframe,image=userimage,text=' UserName  ',compound=LEFT,font=('times new roman',20,'bold'),bg='white')
usernamelabel.grid(row=1,column=0)

userentry=Entry(logframe,font=('times new roman',15,),bd=3)
userentry.grid(row=1,column=1)



passnamelabel=Label(logframe,image=passimage,text='Password',compound=LEFT,font=('times new roman',20,'bold'),bg='white')
passnamelabel.grid(row=2,column=0)
passentry=Entry(logframe,font=('times new roman',15,),bd=3)
passentry.grid(row=2,column=1)


loginbutton=Button(logframe,text='Login',font=('times new roman',15,'bold'),bg='violet',width=15,fg='black',cursor='hand2',command=login)
loginbutton.grid(row=3,column=0,columnspan=2,pady=5)

viewbutton=Button(logframe,text='View Database',font=('times new roman',15,'bold'),bg='violet',width=15,fg='black',cursor='hand2',command=viewget)
viewbutton.grid(row=4,column=0,columnspan=2,pady=5)




window.mainloop()

