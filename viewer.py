from tkinter import *
import time
import ttkthemes
from tkinter import ttk,messagebox,filedialog
import pymysql
import pandas

#functionality Part

def iexit():
    result=messagebox.askyesno('Confirm','Do you want to exit?')
    if result:
        root.destroy()
    else:
        pass

def export_data():
    url=filedialog.asksaveasfilename(defaultextension='.csv')
    indexing=studentTable.get_children()
    newlist=[]
    for index in indexing:
        content=studentTable.item(index)
        datalist=content['values']
        newlist.append(datalist)


    table=pandas.DataFrame(newlist,columns=['GroupNo','Members','MobileNo','Email','Department','Guide','Research Publication ','Added Date','Added Time'])
    table.to_csv(url,index=False)
    messagebox.showinfo('Success','Data is saved succesfully')



def toplevel_data(title,button_text,command):
    global GroupNoEntry,MobileEntry,membersEntry,emailEntry,departmentEntry,guideEntry,researchEntry,domainentry,Projectentry,linkentry,screen
    screen = Toplevel()
    screen.title(title)
    screen.grab_set()
    screen.resizable(False, False)
    idLabel = Label(screen, text='Groupno', font=('times new roman', 20, 'bold'))
    idLabel.grid(row=0, column=0, padx=30, pady=15, sticky=W)
    GroupNoEntry = Entry(screen, font=('roman', 15, 'bold'), width=24)
    GroupNoEntry.grid(row=0, column=1, pady=15, padx=10)






    addressLabel = Label(screen, text='Department', font=('times new roman', 20, 'bold'))
    addressLabel.grid(row=4, column=0, padx=30, pady=15, sticky=W)
    departmentEntry = Entry(screen, font=('roman', 15, 'bold'), width=24)
    departmentEntry.grid(row=4, column=1, pady=15, padx=10)

    genderLabel = Label(screen, text='Guide', font=('times new roman', 20, 'bold'))
    genderLabel.grid(row=5, column=0, padx=30, pady=15, sticky=W)
    guideEntry = Entry(screen, font=('roman', 15, 'bold'), width=24)
    guideEntry.grid(row=5, column=1, pady=15, padx=10)

    projectLabel = Label(screen, text='Project Name', font=('times new roman', 20, 'bold'))
    projectLabel.grid(row=6, column=0, padx=30, pady=15, sticky=W)
    Projectentry = Entry(screen, font=('roman', 15, 'bold'), width=24)
    Projectentry.grid(row=6, column=1, pady=15, padx=10)

    domainLabel = Label(screen, text='Project Domain', font=('times new roman', 20, 'bold'))
    domainLabel.grid(row=7, column=0, padx=30, pady=15, sticky=W)
    domainentry = Entry(screen, font=('roman', 15, 'bold'), width=24)
    domainentry.grid(row=7, column=1, pady=15, padx=10)

    dobLabel = Label(screen, text='Research Publication', font=('times new roman', 20, 'bold'))
    dobLabel.grid(row=8, column=0, padx=30, pady=15, sticky=W)
    researchEntry = Entry(screen, font=('roman', 15, 'bold'), width=24)
    researchEntry.grid(row=8, column=1, pady=15, padx=10)

    linkLabel = Label(screen, text='Research Paper Link', font=('times new roman', 20, 'bold'))
    linkLabel.grid(row=9, column=0, padx=30, pady=15, sticky=W)
    linkentry = Entry(screen, font=('roman', 15, 'bold'), width=24)
    linkentry.grid(row=9, column=1, pady=15, padx=10)




    student_button = ttk.Button(screen, text=button_text, command=command)
    student_button.grid(row=10, columnspan=2, pady=15)
    if title=='Update Student':
        indexing = studentTable.focus()

        content = studentTable.item(indexing)
        listdata = content['values']
        GroupNoEntry.insert(0, listdata[0])
        membersEntry.insert(0, listdata[1])
        MobileEntry.insert(0, listdata[2])
        emailEntry.insert(0, listdata[3])
        departmentEntry.insert(0, listdata[4])
        guideEntry.insert(0, listdata[5])
        Projectentry.insert(0, listdata[6])
        domainentry.insert(0, listdata[7])
        researchEntry.insert(0, listdata[8])
        linkentry.insert(0, listdata[9])


def procedureex():
    query = 'call doneresearch(%s,%s)'
    mycursor.execute(query,(guideEntry.get(),researchEntry.get()))
    fetched_data = mycursor.fetchall()
    studentTable.delete(*studentTable.get_children())
    for data in fetched_data:
        studentTable.insert('', END, values=data)

def joinuse():
    query = 'select* from staff'
    mycursor.execute(query, guideEntry.get())
    con.commit()

    screen.destroy()
    fetched_data = mycursor.fetchall()
    studentTable.delete(*studentTable.get_children())
    for data in fetched_data:
        studentTable.insert('', END, values=data)


def update_data():
    query='update projectdetails set department=%s,Guide=%s,ProjectName=%s,ProjectDomain=%s,Research_Publication=%s,ResearchLink=%s,date=%s,time=%s where groupid=%s'
    mycursor.execute(query,(departmentEntry.get(),
                            guideEntry.get(),Projectentry.get(),domainentry.get(),researchEntry.get(),linkentry.get(),date,currenttime,GroupNoEntry.get()))
    con.commit()
    messagebox.showinfo('Success',f'Id {GroupNoEntry.get()} is modified successfully',parent=screen)
    screen.destroy()
    show_student()



def show_student():
    query = 'select * from projectdetails'
    mycursor.execute(query)
    fetched_data = mycursor.fetchall()
    studentTable.delete(*studentTable.get_children())
    for data in fetched_data:
        studentTable.insert('', END, values=data)




def viewcreate():
    query = 'select GroupNo,Department from Viewer'
    mycursor.execute(query)
    fetched_data = mycursor.fetchall()
    studentTable.delete(*studentTable.get_children())
    addstudentButton.config(state=DISABLED)
    searchstudentButton.config(state=DISABLED)
    updatestudentButton.config(state=DISABLED)
    showstudentButton.config(state=DISABLED)
    exportstudentButton.config(state=DISABLED)
    Runprocedure.config(state=DISABLED)
    viewmode.config(state=DISABLED)
    deletestudentButton.config(state=DISABLED)

    for data in fetched_data:
        studentTable.insert('', END, values=data)




def delete_student():
    indexing=studentTable.focus()
    print(indexing)
    content=studentTable.item(indexing)
    content_id=content['values'][0]

    query='delete from projectdetails where groupid=%s'
    mycursor.execute(query,content_id)
    con.commit()
    messagebox.showinfo('Deleted',f'Id {content_id} is deleted succesfully')
    query='select * from projectdetails'
    mycursor.execute(query)
    fetched_data=mycursor.fetchall()
    studentTable.delete(*studentTable.get_children())
    for data in fetched_data:
        studentTable.insert('',END,values=data)




def search_data():
    query='select * from projectdetails where Groupid=%s or department=%s'
    mycursor.execute(query,(GroupNoEntry.get(),departmentEntry.get()))
    fetched_data=mycursor.fetchall()
    for data in fetched_data:
        studentTable.insert('',END,values=data)




def add_data():
    if GroupNoEntry.get()=='' or  departmentEntry.get()=='' or guideEntry.get()=='' or researchEntry.get()=='' or domainentry.get()=='' or Projectentry.get()=='':
        messagebox.showerror('Error','All Fields are required',parent=screen)

    else:
        try:
            query='insert into projectdetails values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            mycursor.execute(query,(GroupNoEntry.get(),departmentEntry.get(),
                                    guideEntry.get(),Projectentry.get(),domainentry.get(),researchEntry.get(),linkentry.get(),date,currenttime))
            con.commit()
            result=messagebox.askyesno('Confirm','Data added successfully. Do you want to clean the form?',parent=screen)
            if result:
                GroupNoEntry.delete(0,END)
                membersEntry.delete(0,END)
                MobileEntry.delete(0,END)
                emailEntry.delete(0,END)
                departmentEntry.delete(0,END)
                guideEntry.delete(0,END)
                Projectentry.delete(0, END)
                domainentry.delete(0, END)
                researchEntry.delete(0,END)
            else:
                pass
        except:
            messagebox.showerror('Error','You have entered a wrong Grouid or repeated a previous id',parent=screen)
            return


        query='select *from projectdetails'
        mycursor.execute(query)
        fetched_data=mycursor.fetchall()
        studentTable.delete(*studentTable.get_children())
        for data in fetched_data:
            studentTable.insert('',END,values=data)


def connect_database():
    def connect():
        global mycursor,con
        try:
            con=pymysql.connect(host='localhost',user='root',password='Adi120632@')
            mycursor=con.cursor()
        except:
            messagebox.showerror('Error','Invalid Details',parent=connectWindow)
            return

        try:

            query='use projectmanagement'
            mycursor.execute(query)
            query='create table projectdetails(groupid varchar(100) not null primary key,department varchar(100),Guide varchar(20),ProjectName varchar(100),ProjectDomain varchar(100),Research_Publication varchar(20),ResearchLink varchar(20),date varchar(50), time varchar(50) )'
            mycursor.execute(query)
        except:
            query='use projectmanagement'
            mycursor.execute(query)
        messagebox.showinfo('Success', 'Database Connection is successful', parent=connectWindow)
        connectWindow.destroy()

        searchstudentButton.config(state=NORMAL)
        viewmode.config(state=NORMAL)
        Runprocedure.config(state=NORMAL)
        viewmode.config(state=NORMAL)



    connectWindow=Toplevel()
    connectWindow.grab_set()
    connectWindow.geometry('470x250+730+230')
    connectWindow.title('Database Connection')
    connectWindow.resizable(0,0)

    hostnameLabel=Label(connectWindow,text='Host Name',font=('arial',20,'bold'))
    hostnameLabel.grid(row=0,column=0,padx=20)

    hostEntry=Entry(connectWindow,font=('roman',15,'bold'),bd=2)
    hostEntry.grid(row=0,column=1,padx=40,pady=20)

    usernameLabel = Label(connectWindow, text='User Name', font=('arial', 20, 'bold'))
    usernameLabel.grid(row=1, column=0, padx=20)

    usernameEntry = Entry(connectWindow, font=('roman', 15, 'bold'), bd=2)
    usernameEntry.grid(row=1, column=1, padx=40, pady=20)

    passwordLabel = Label(connectWindow, text='Password', font=('arial', 20, 'bold'))
    passwordLabel.grid(row=2, column=0, padx=20)

    passwordEntry = Entry(connectWindow, font=('roman', 15, 'bold'), bd=2)
    passwordEntry.grid(row=2, column=1, padx=40, pady=20)

    connectButton=ttk.Button(connectWindow,text='CONNECT',command=connect)
    connectButton.grid(row=3,columnspan=2)

count=0
text=''
def slider():
    global text,count
    # if count==len(s):
    #     count=0
    #     text=''
    text=text+s[count]
    sliderLabel.config(text=text)
    count+=1
    sliderLabel.after(300,slider)




def clock():
    global date,currenttime
    date=time.strftime('%d/%m/%Y')
    currenttime=time.strftime('%H:%M:%S')
    datetimeLabel.config(text=f'   Date: {date}\nTime: {currenttime}')
    datetimeLabel.after(1000,clock)



#GUI Part
root=ttkthemes.ThemedTk()

root.get_themes()

root.set_theme('radiance')

root.geometry('1300x850+0+0')
root.resizable(0,0)
root.title('Project Management System')

datetimeLabel=Label(root,font=('times new roman',18,'bold'))
datetimeLabel.place(x=5,y=5)
clock()
s='Project Management System' #s[count]=t when count is 1
sliderLabel=Label(root,font=('arial',28,'italic bold'),width=30)
sliderLabel.place(x=200,y=0)
slider()

connectButton=ttk.Button(root,text='Connect database',command=connect_database)
connectButton.place(x=980,y=0)

leftFrame=Frame(root)
leftFrame.place(x=50,y=80,width=300,height=750)

logo_image=PhotoImage(file='user.png')
logo_Label=Label(leftFrame,image=logo_image)
logo_Label.grid(row=0,column=0)

addstudentButton=ttk.Button(leftFrame,text='Add Project Details',width=25,state=DISABLED,command=lambda :toplevel_data('Add Student','Add',add_data))
addstudentButton.grid(row=1,column=0,pady=20)

searchstudentButton=ttk.Button(leftFrame,text='Search Project Details',width=25,state=DISABLED,command=lambda :toplevel_data('Search Student','Search',search_data))
searchstudentButton.grid(row=2,column=0,pady=20)

deletestudentButton=ttk.Button(leftFrame,text='Delete Project Details',width=25,state=DISABLED,command=delete_student)
deletestudentButton.grid(row=3,column=0,pady=20)

updatestudentButton=ttk.Button(leftFrame,text='Update Project Details',width=25,state=DISABLED,command=lambda :toplevel_data('Update Student','Update',update_data))
updatestudentButton.grid(row=4,column=0,pady=20)

showstudentButton=ttk.Button(leftFrame,text='Show details Group',width=25,state=DISABLED,command=show_student)
showstudentButton.grid(row=5,column=0,pady=20)

exportstudentButton=ttk.Button(leftFrame,text='Research Done Group',width=25,state=DISABLED,command=lambda :toplevel_data('Research','Done',joinuse))
exportstudentButton.grid(row=6,column=0,pady=20)

Runprocedure=ttk.Button(leftFrame,text='Research Status',width=25,state=DISABLED,command=lambda :toplevel_data('Research','Done',procedureex))
Runprocedure.grid(row=7,column=0,pady=20)

viewmode=ttk.Button(leftFrame,text='ViewMode',width=25,state=DISABLED,command=viewcreate)
viewmode.grid(row=8,column=0,pady=20)

exitButton=ttk.Button(leftFrame,text='Exit',width=25,command=iexit)
exitButton.grid(row=9,column=0,pady=20)

rightFrame=Frame(root)
rightFrame.place(x=350,y=80,width=820,height=700)

scrollBarX=Scrollbar(rightFrame,orient=HORIZONTAL)
scrollBarY=Scrollbar(rightFrame,orient=VERTICAL)

studentTable=ttk.Treeview(rightFrame,columns=('GroupNo','Members','Mobile','Email','Department','Guide','ProjectName','ProjectDomain','ResearchPublication','ResearchLink','Added Date','Added Time'),
                          xscrollcommand=scrollBarX.set,yscrollcommand=scrollBarY.set)

scrollBarX.config(command=studentTable.xview)
scrollBarY.config(command=studentTable.yview)

scrollBarX.pack(side=BOTTOM,fill=X)
scrollBarY.pack(side=RIGHT,fill=Y)

studentTable.pack(expand=1,fill=BOTH)

studentTable.heading('GroupNo',text='')
studentTable.heading('Members',text='')
studentTable.heading('Mobile',text='')
studentTable.heading('Email',text='')
studentTable.heading('Department',text='')
studentTable.heading('Guide',text='')
studentTable.heading('ProjectName',text='')
studentTable.heading('ProjectDomain',text='')
studentTable.heading('ResearchPublication',text='')
studentTable.heading('ResearchLink',text='')
studentTable.heading('Added Date',text='')
studentTable.heading('Added Time',text='')

studentTable.column('GroupNo',width=100)



style=ttk.Style()

style.configure('Treeview', rowheight=40,font=('arial', 12, 'bold'), fieldbackground='white', background='white',)
style.configure('Treeview.Heading',font=('arial', 14, 'bold'),foreground='red')

studentTable.config(show='headings')

root.mainloop()