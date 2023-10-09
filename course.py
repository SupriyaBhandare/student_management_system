from tkinter import *
from tkinter import Toplevel, messagebox
from tkinter.ttk import Treeview
from tkinter import ttk
import pymysql
from PIL import Image, ImageTk


def student():
    import student


def faculty():
    import faculty


root = Toplevel()
root.title("Student Management System")
root.geometry('1530x790+0+0')
root.resizable(False, False)

global con, mycursor
con = pymysql.connect(host='localhost', user='root', password='1234')
mycursor = con.cursor()

cidval = StringVar()
cnameval = StringVar()
deptval = StringVar()
feesval = StringVar()
searchComboval = StringVar()
searchval = StringVar()

# ========================== ADD course =====================================

def addData():
    cid = cidval.get()
    cname = cnameval.get()
    dept = deptval.get()
    fees = feesval.get()
    global con, mycursor
    if (
            cnameval.get() == '' or deptval.get() == '' or feesval.get() == ''):
        messagebox.showerror('Error', 'All Fields are required', parent=root)
    else:
        try:
            con = pymysql.connect(host='localhost', user='root', password='1234')
            mycursor = con.cursor()
            mycursor.execute('create database sms')
            mycursor.execute('use sms')
            mycursor.execute(
                'create table course (cid int primary key, auto_increment, cname varchar(40),dept varchar(15),fees varchar(50))')
            messagebox.showinfo('Notification', 'Now you are connected to the database successfully', parent=root)
            # mycursor.execute('use sms')
        except:
            mycursor.execute('use sms')
        try:
            # con = pymysql.connect(host='localhost',username='root',password='1234',database='sms1')
            mycursor = con.cursor()
            mycursor.execute('insert into course values(null,%s,%s,%s)',(cname, dept, fees))
            con.commit()  # modify- update
            res = messagebox.askyesnocancel('Notification', 'Data Added Successfully.. You want to clean the form',
                                            parent=root)
            if (res == True):

                cnameval.set('')
                deptval.set('')
                feesval.set('')

        except Exception as es:
            messagebox.showerror('Error', f'Due to:{str(es)}', parent=root)
        mycursor.execute('select * from course')
        data = mycursor.fetchall()
        coursetable.delete(*coursetable.get_children())
        for i in data:
            vv = [i[0], i[1], i[2], i[3]]
            coursetable.insert('', END, values=vv)
            con.commit()


# ==================== SEARCH course ====================================

def searchData():
    if searchComboval.get() == '' or searchval.get() == '':
        messagebox.showinfo('Error', 'Please Select Option', parent=root)
    else:
        try:
            mycursor.execute('use sms')
            mycursor.execute("select * from course where " +str(searchComboval.get())+" LIKE '%"+str(searchval.get())+"%'")

            data = mycursor.fetchall()
            if len(data)!=0:
                coursetable.delete(*coursetable.get_children())
                for i in data:
                    vv = [i[0], i[1], i[2], i[3]]
                    coursetable.insert('', END, values=vv)
                con.commit()

        except Exception as es:
            messagebox.showerror('Error',f'Due to:{str(es)}',parent=root)


# ============================= DELETE course DATA ============================

def deleteData():
    try:
        update = messagebox.askyesnocancel('Update', 'You want to delete the data ', parent=root)
        if (update > 0):
            cc = coursetable.focus()  # shows which record/column you selected
            content = coursetable.item(cc)
            pp = content['values'][0]
            mycursor.execute('delete from course where cid=%s', (pp))
        else:
            if not update:
                return
        con.commit()
        mycursor.execute('select * from course')
        data = mycursor.fetchall()
        coursetable.delete(*coursetable.get_children())
        for i in data:
            vv = [i[0], i[1], i[2], i[3]]
            coursetable.insert('', END, values=vv)
        res = messagebox.askyesnocancel('Notification',
                                        'Id {} deleted successfully..You want to clean the form'.format(pp),
                                        parent=root)
        if (res == True):
            cidval.set('')
            cnameval.set('')
            deptval.set('')
            feesval.set('')
    except Exception as es:
        messagebox.showerror('Error', f'Due to:{str(es)}', parent=root)


# ============================== GET CURSOR DATA ============================


def getCursor(root, event=''):
    row = coursetable.focus()  # shows which record/column you selected
    content = coursetable.item(row)
    data = content['values']

    cidval.set(data[0])
    cnameval.set(data[1])
    deptval.set(data[2])
    feesval.set(data[3])

    coursetable.bind('<ButtonRelease>', getCursor)


# ============================== UPDATE DATA ================================================

def updateData():
    try:
        update = messagebox.askyesnocancel('Update', 'You want to update the data ', parent=root)
        if (update > 0):
            mycursor.execute(
                'update course set cname=%s,dept=%s,fees=%s where cid=%s',
                (cnameval.get(), deptval.get(), feesval.get(), cidval.get()))
        else:
            if not update:
                return
        con.commit()
        mycursor.execute('select * from course')
        data = mycursor.fetchall()
        coursetable.delete(*coursetable.get_children())
        for i in data:
            vv = [i[0], i[1], i[2], i[3]]
            coursetable.insert('', END, values=vv)
        res = messagebox.askyesnocancel('Notification', 'Data Updated Successfully..You want to clean the form',
                                        parent=root)
        if (res == True):
            cidval.set('')
            cnameval.set('')
            deptval.set('')
            feesval.set('')
    except Exception as es:
        messagebox.showerror('Error', f'Due to:{str(es)}', parent=root)


# =============================== RESET DATA======================================
def resetData():
    cidval.set('')
    cnameval.set('Select Course')
    deptval.set('Select Department')
    feesval.set('')


# ============================== SHOW ALL  ======================================

def showallData():
    mycursor = con.cursor()
    mycursor.execute('use sms')
    mycursor.execute('select * from course')
    data = mycursor.fetchall()

    if len(data) != 0:
        coursetable.delete(*coursetable.get_children())
        for i in data:
            # vv = [i[0], i[1], i[2], i[3]]
            coursetable.insert('', END, values=i)
        con.commit()


# ===============================Starting===========================================

bgimage = ImageTk.PhotoImage(file='coursebg.jpeg')  # jpg=ImageTk
bglabel = Label(root, image=bgimage)
bglabel.place(x=0, y=0)

ManageFrame = Frame(bglabel, bd=2, relief=RIDGE, bg="white")
ManageFrame.place(x=15, y=75, width=1490, height=700)

admImage = PhotoImage(file='user.png')
admLabel = Label(root, image=admImage, text=' Administrator', compound=LEFT,
                 font=('times new roman', 20, 'bold'))
admLabel.grid(row=1, column=0, pady=20, padx=20)

courseButton = Button(root, text='Courses', font=('cambria', 18, ' bold'), fg='blue')
courseButton.place(x=1050, y=20)

stuButton = Button(root, text='Students', font=('cambria', 18, ' bold'), fg='blue', command=student)
stuButton.place(x=1200, y=20)

facButton = Button(root, text='Faculty', font=('cambria', 18, ' bold'), fg='blue', command=faculty)
facButton.place(x=1350, y=20)

DataLeftFrame = LabelFrame(ManageFrame, bd=4, relief=RIDGE, text='Course Information', padx=2,
                           font=('times new roman', 12, ' bold'), fg='darkgreen', bg='white')
DataLeftFrame.place(x=10, y=10, width=660, height=670)

# For image
image = ImageTk.PhotoImage(file='fgirl.jpeg')  # jpg=ImageTk
label = Label(DataLeftFrame, image=image)
label.place(x=5, y=0)

image1 = PhotoImage(file='boy.png')  # jpg=ImageTk
label1 = Label(DataLeftFrame, image=image1)
label1.place(x=510, y=0)

facLabel = Label(DataLeftFrame, text='Courses', width=23, font=('times', 15, ' bold'))
facLabel.place(x=180, y=35, height=50)

# current course information frame
courseFrame = LabelFrame(DataLeftFrame, bd=4, relief=RIDGE, text='Information', padx=2,
                         font=('times new roman', 12, ' bold'), fg='darkgreen', bg='white')
courseFrame.place(x=0, y=120, width=650, height=390)


# Labels
# ID
def validate_entry(text):
    return text.isdecimal()


cidLabel = Label(courseFrame, font=('arial', 12, ' bold'), bg='white', text='Course Id ')
cidLabel.place(x=150, y=50)

cidEntry = ttk.Entry(courseFrame, textvariable=cidval, font=('arial', 12), width=20, validate="key",
                     validatecommand=(root.register(validate_entry), "%S"))
cidEntry.place(x=280, y=50)
cidEntry.config(state='disable')

# Name
nameLabel = Label(courseFrame, font=('arial', 12, ' bold'), bg='white', text='Course Name ')
nameLabel.place(x=150, y=100)

nameCombo = ttk.Combobox(courseFrame, textvariable=cnameval, font=('arial', 12), width=18, state='readonly')
nameCombo['value'] = ('Select Course', 'FY', 'SY', 'TY', 'BTECH')
nameCombo.current(0)
nameCombo.place(x=280, y=100)

# dept
deptLabel = Label(courseFrame, font=('arial', 12, ' bold'), bg='white', text='Department ')
deptLabel.place(x=150, y=150)

deptCombo = ttk.Combobox(courseFrame, textvariable=deptval, font=('arial', 12), width=18, state='readonly')
deptCombo['value'] = ('Select Department', 'IT', 'ENTC', 'CIVIL', 'MECH')
deptCombo.current(0)
deptCombo.place(x=280, y=150)


# fees
def validate_entry(text):
    return text.isdecimal()


feesLabel = Label(courseFrame, font=('arial', 12, ' bold'), bg='white', text='Fees ')
feesLabel.place(x=150, y=200)

feesEntry = ttk.Entry(courseFrame, textvariable=feesval, font=('arial', 12), width=20, validate="key",
                      validatecommand=(root.register(validate_entry), "%S"))
feesEntry.place(x=280, y=200)

# Button Frame
ButtonFrame = Frame(DataLeftFrame, bd=4, relief=RIDGE, bg='white')
ButtonFrame.place(x=0, y=530, width=650, height=100)

addButton = Button(ButtonFrame, text='Add', width=14, font=('arial', 12, ' bold'), bg='blue', fg='white',
                   command=addData)
addButton.grid(row=0, column=0, sticky=W, pady=25, padx=5)

updateButton = Button(ButtonFrame, text='Update', width=14, font=('arial', 12, ' bold'), bg='blue', fg='white',
                      command=updateData)
updateButton.grid(row=0, column=1, sticky=W, pady=25, padx=5)

deleteButton = Button(ButtonFrame, text='Delete', width=14, font=('arial', 12, ' bold'), bg='blue', fg='white',
                      command=deleteData)
deleteButton.grid(row=0, column=2, sticky=W, pady=25, padx=5)

resetButton = Button(ButtonFrame, text='Reset', width=14, font=('arial', 12, ' bold'), bg='blue', fg='white',
                     command=resetData)
resetButton.grid(row=0, column=3, sticky=W, pady=25, padx=5)

# ============ Search frame or course details  frame ======================================

DataRightFrame = LabelFrame(ManageFrame, bd=4, relief=RIDGE, text='Course Details', padx=2,
                            font=('times new roman', 12, ' bold'), fg='darkgreen', bg='white')
DataRightFrame.place(x=680, y=10, width=790, height=670)

searchFrame = LabelFrame(DataRightFrame, bd=4, relief=RIDGE, text='Search course Info', padx=2,
                         font=('times new roman', 12, ' bold'), fg='darkgreen', bg='white')
searchFrame.place(x=0, y=20, width=778, height=80)

searchByLabel = Label(searchFrame, font=('arial', 12, ' bold'), bg='black', text='Search By', fg='red')
searchByLabel.grid(row=0, column=0, sticky=W, padx=2, pady=10)

searchCombo = ttk.Combobox(searchFrame, textvariable=searchComboval, font=('arial', 12), width=18, state='readonly')
searchCombo['value'] = ('Select option', 'CId', 'CName', 'Dept', 'Fees')
searchCombo.current(0)
searchCombo.grid(row=0, column=1, padx=5, sticky=W)

searchByEntry = ttk.Entry(searchFrame, textvariable=searchval, font=('arial', 12), width=22)
searchByEntry.grid(row=0, column=2, padx=5)

searchButton = Button(searchFrame, text='Search', width=12, font=('arial', 12, ' bold'), bg='blue', fg='white',
                      command=searchData)
searchButton.grid(row=0, column=3, padx=5)

showAllButton = Button(searchFrame, text='Show All', width=11, font=('arial', 12, ' bold'), bg='blue', fg='white',
                       command=showallData)
showAllButton.grid(row=0, column=4, padx=5)

# ==============================    course Table and Scroll Bar    ======================================

tableFrame = Frame(DataRightFrame, bd=4, relief=RIDGE)
tableFrame.place(x=0, y=110, width=778, height=520)

scroll_x = Scrollbar(tableFrame, orient=HORIZONTAL)
scroll_y = Scrollbar(tableFrame, orient=VERTICAL)

coursetable = ttk.Treeview(tableFrame, columns=('cid', 'cname', 'Dept', 'Fees'),
                           yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
scroll_x.pack(side=BOTTOM, fill=X)
scroll_y.pack(side=RIGHT, fill=Y)
scroll_x.config(command=coursetable.xview)
scroll_y.config(command=coursetable.yview)

coursetable.heading('cid', text='Id')
coursetable.heading('cname', text='Name')
coursetable.heading('Dept', text='Department')
coursetable.heading('Fees', text='Fees')

coursetable['show'] = 'headings'

coursetable.pack(fill=BOTH, expand=1)
coursetable.bind('<ButtonRelease>', getCursor)

root.mainloop()
