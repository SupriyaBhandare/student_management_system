from tkinter import *
from tkinter import Toplevel, messagebox
from tkinter.ttk import Treeview
from tkinter import ttk
from tkcalendar import DateEntry
import pymysql
from PIL import Image, ImageTk

def faculty():
    import faculty

def course():
    import course

root = Toplevel()
root.title("Student Management System")
root.geometry('1530x790+0+0')
root.resizable(False, False)

global con, mycursor
con = pymysql.connect(host='localhost', user='root', password='1234')
mycursor = con.cursor()

deptval = StringVar()
yearval = StringVar()
semval = StringVar()
courseval = StringVar()
idval = StringVar()
nameval = StringVar()
divval = StringVar()
rollval = StringVar()
genderval = StringVar()
dobval = StringVar()
phoneval = StringVar()
emailval = StringVar()
addressval = StringVar()
cityval = StringVar()

# ========================== ADD STUDENT =====================================

def addData():
    dept = deptval.get();
    course = courseval.get()
    year = yearval.get()
    sem = semval.get()
    id = idval.get()
    name = nameval.get()
    division = divval.get()
    roll = rollval.get()
    gender = genderval.get()
    dob = dobval.get()
    email = emailval.get()
    phone = phoneval.get()
    address = addressval.get()
    city = cityval.get()

    if (deptval.get() == '' or courseval.get() == '' or yearval.get() == '' or semval.get() == '' or idval.get() == ''
        or nameval.get() == '' or divval.get() == '' or rollval.get() == '' or genderval.get() == '' or dobval.get() == ''
        or emailval.get() == '' or phoneval.get() == '' or addressval.get() == '' or cityval.get() == ''):
        messagebox.showerror('Error', 'All Fields are required',parent=root)
    else:
        try:
            con = pymysql.connect(host='localhost', user='root', password='1234')
            mycursor = con.cursor()
            mycursor.execute('create database sms')
            mycursor.execute('use sms')
            mycursor.execute(
                'create table student (id int(10) primary key, name varchar(40),gender varchar(15),dob varchar(50),email varchar(30),'
                'phone varchar(12),address varchar(50),dept varchar(30),course varchar(10),year varchar(30),'
                'sem varchar (30),division varchar(30),roll varchar(30),city varchar(30))')
            messagebox.showinfo('Notification', 'Now you are connected to the database successfully',parent=root)
            #messagebox.showinfo('Notification', 'Now you are connected to the database successfully', parent=dbroot)
        except:
            mycursor.execute('use sms')
        try:
            # con = pymysql.connect(host='localhost',username='root',password='1234',database='sms')
            mycursor = con.cursor()
            mycursor.execute('use sms')
            mycursor.execute('insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
                             (id, name, gender, dob, email, phone, address, dept, course, year, sem, division, roll,
                              city))
            con.commit()  # modify- update
            res = messagebox.askyesnocancel('Notification', 'Data Added Successfully.. You want to clean the form',parent=root)
            if (res == True):
                deptval.set('')
                courseval.set('')
                yearval.set('')
                semval.set('')
                idval.set('')
                nameval.set('')
                divval.set('')
                rollval.set('')
                genderval.set('')
                dobval.set('')
                emailval.set('')
                phoneval.set('')
                addressval.set('')
                cityval.set('')

        except Exception as es:
            messagebox.showerror('Error', f'Due to:{str(es)}',parent=root)
        mycursor.execute('select * from student')
        data = mycursor.fetchall()
        studenttable.delete(*studenttable.get_children())
        for i in data:
            vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11], i[12], i[13]]
            studenttable.insert('', END, values=vv)
            con.commit()

# ==================== SEARCH STUDENT ====================================

def searchData():
    if searchComboval.get() == '' or searchval.get() == '':
        messagebox.showinfo('Error', 'Please Select Option',parent=root)
    else:
        try:
            mycursor.execute('use sms')
            mycursor.execute("select * from student where " +str(searchComboval.get())+" LIKE '%"+str(searchval.get())+"%'")

            data = mycursor.fetchall()
            if len(data)!=0:
                studenttable.delete(*studenttable.get_children())
                for i in data:
                    vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11], i[12], i[13]]
                    studenttable.insert('', END, values=vv)
                con.commit()

        except Exception as es:
            messagebox.showerror('Error',f'Due to:{str(es)}',parent=root)


# ============================= DELETE STUDENT DATA ============================

def deleteData():
    try:
        update = messagebox.askyesnocancel('Update', 'You want to delete the data ',parent=root)
        if (update > 0):
            cc = studenttable.focus()  # shows which record/column you selected
            content = studenttable.item(cc)
            pp = content['values'][0]
            mycursor.execute('delete from student where id=%s', (pp))
        else:
            if not update:
                return
        con.commit()
        mycursor.execute('select * from student')
        data = mycursor.fetchall()
        studenttable.delete(*studenttable.get_children())
        for i in data:
            vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11], i[12], i[13]]
            studenttable.insert('', END, values=vv)
        res = messagebox.askyesnocancel('Notification',
                                        'Id {} deleted successfully..You want to clean the form'.format(pp),parent=root)
        if (res == True):
            deptval.set('')
            courseval.set('')
            yearval.set('')
            semval.set('')
            idval.set('')
            nameval.set('')
            divval.set('')
            rollval.set('')
            genderval.set('')
            dobval.set('')
            emailval.set('')
            phoneval.set('')
            addressval.set('')
            cityval.set('')
    except Exception as es:
        messagebox.showerror('Error', f'Due to:{str(es)}',parent=root)


# ============================== GET CURSOR DATA ============================


def getCursor(root, event=''):
    row = studenttable.focus()  # shows which record/column you selected
    content = studenttable.item(row)
    data = content['values']

    idval.set(data[0])
    nameval.set(data[1])
    genderval.set(data[2])
    dobval.set(data[3])
    emailval.set(data[4])
    phoneval.set(data[5])
    addressval.set(data[6])
    deptval.set(data[7])
    courseval.set(data[8])
    yearval.set(data[9])
    semval.set(data[10])
    divval.set(data[11])
    rollval.set(data[12])
    cityval.set(data[13])

    studenttable.bind('<ButtonRelease>', getCursor)


# ============================== UPDATE DATA ================================================

def updateData():
    mycursor.execute('use sms')
    try:
        update = messagebox.askyesnocancel('Update', 'You want to update the data ',parent=root)
        if (update > 0):
            mycursor.execute(
                'update student set name=%s,gender=%s,dob=%s,email=%s,phone=%s,address=%s,dept=%s,course=%s,'
                'year=%s,sem=%s,division=%s,roll=%s,city=%s where id=%s',
                (nameval.get(), genderval.get(), dobval.get(), emailval.get(), phoneval.get(), addressval.get(),
                 deptval.get(), courseval.get(),
                 yearval.get(), semval.get(), divval.get(), rollval.get(), cityval.get(), idval.get()))
        else:
            if not update:
                return
        con.commit()
        mycursor.execute('select * from student')
        data = mycursor.fetchall()
        studenttable.delete(*studenttable.get_children())
        for i in data:
            vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11], i[12], i[13]]
            studenttable.insert('', END, values=vv)
        res = messagebox.askyesnocancel('Notification', 'Data Updated Successfully..You want to clean the form',parent=root)
        if (res == True):
            deptval.set('')
            courseval.set('')
            yearval.set('')
            semval.set('')
            idval.set('')
            nameval.set('')
            divval.set('')
            rollval.set('')
            genderval.set('')
            dobval.set('')
            emailval.set('')
            phoneval.set('')
            addressval.set('')
            cityval.set('')
    except Exception as es:
        messagebox.showerror('Error', f'Due to:{str(es)}',parent=root)


# =============================== RESET DATA======================================
def resetData():
    deptval.set('Select Department')
    courseval.set('Select Course')
    yearval.set('Select Year')
    semval.set('Select Semester')
    idval.set('')
    nameval.set('')
    divval.set('Select Division')
    rollval.set('')
    genderval.set('Select Gender')
    dobval.set('')
    emailval.set('')
    phoneval.set('')
    addressval.set('')
    cityval.set('')


# ============================== SHOW ALL  ======================================

def showallData():
    mycursor=con.cursor()
    mycursor.execute('use sms')
    mycursor.execute('select * from student')
    data = mycursor.fetchall()

    if len(data)!=0 :
        studenttable.delete(*studenttable.get_children())
        for i in data:
            #vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11], i[12], i[13]]
            studenttable.insert('', END, values=i)
        con.commit()


# ===============================Starting===========================================

bgimage = ImageTk.PhotoImage(file='bg1.jpg')  # jpg=ImageTk
bglabel = Label(root, image=bgimage)
bglabel.place(x=0, y=0)

ManageFrame = Frame(bglabel, bd=2, relief=RIDGE, bg="white")
ManageFrame.place(x=15, y=75, width=1490, height=700)


admImage = PhotoImage(file='user.png')
admLabel = Label(root, image=admImage, text=' Administrator', compound=LEFT,
                      font=('times new roman', 20, 'bold'))
admLabel.grid(row=1, column=0, pady=20, padx=20)

courseButton =Button(root,text='Courses',font=('cambria', 18, ' bold'), fg='blue',command=course)
courseButton.place(x=1050,y=20)

stuButton=Button(root, text='Students', font=('cambria', 18, ' bold'), fg='blue')
stuButton.place(x=1200,y=20)

facButton=Button(root, text='Faculty', font=('cambria', 18, ' bold'), fg='blue',command=faculty)
facButton.place(x=1350,y=20)

DataLeftFrame = LabelFrame(ManageFrame, bd=4, relief=RIDGE, text='Student Information', padx=2,
                           font=('times new roman', 12, ' bold'), fg='red', bg='white')
DataLeftFrame.place(x=10, y=10, width=660, height=670)

Label1 = Label(DataLeftFrame, text='Student', width=23, font=('times', 15, ' bold'))
Label1.place(x=180, y=35, height=50)

#For image
image = ImageTk.PhotoImage(file='fgirl.jpeg')  # jpg=ImageTk
label = Label(DataLeftFrame, image=image)
label.place(x=5 , y=0)

image1 = PhotoImage(file='boy.png')  # jpg=ImageTk
label1 = Label(DataLeftFrame, image=image1)
label1.place(x=510, y=0)

# current course information frame
CourseFrame = LabelFrame(DataLeftFrame, bd=4, relief=RIDGE, text='Current Course Information', padx=2,
                         font=('times new roman', 12, ' bold'), fg='red', bg='white')
CourseFrame.place(x=0, y=120, width=650, height=115)

# Labels
deptLabel = Label(CourseFrame, text='Department', font=('arial', 12, ' bold'), bg='white')
deptLabel.grid(row=0, column=0, padx=2, sticky=W)

deptCombo = ttk.Combobox(CourseFrame, textvariable=deptval, font=('arial', 12), width=17, state='readonly')
deptCombo['value'] = ('Select Department', 'IT', 'CSE', 'CIVIL', 'MECH')
deptCombo.current(0)
deptCombo.grid(row=0, column=1, padx=2, pady=10, sticky=W)
# course
courseLabel = Label(CourseFrame, font=('arial', 12, ' bold'), bg='white', text='Courses:')
courseLabel.grid(row=0, column=2, sticky=W, padx=2, pady=10)

courseCombo = ttk.Combobox(CourseFrame, textvariable=courseval, font=('arial', 12), width=17, state='readonly')
courseCombo['value'] = ('Select Course', 'FY', 'SY', 'TY', 'BTECH')
courseCombo.current(0)
courseCombo.grid(row=0, column=3, padx=2, pady=10, sticky=W)

# year
yearLabel = Label(CourseFrame, font=('arial', 12, ' bold'), bg='white', text='Year')
yearLabel.grid(row=1, column=0, sticky=W, padx=2, pady=10)

yearCombo = ttk.Combobox(CourseFrame, textvariable=yearval, font=('arial', 12), width=17, state='readonly')
yearCombo['value'] = ('Select Year', '2020-21', '2021-22', '2022-23', '2023-24')
yearCombo.current(0)
yearCombo.grid(row=1, column=1, padx=2, sticky=W)

# semester
semLabel = Label(CourseFrame, font=('arial', 12, ' bold'), bg='white', text='Semester')
semLabel.grid(row=1, column=2, sticky=W, padx=2, pady=10)

semCombo = ttk.Combobox(CourseFrame, textvariable=semval, font=('arial', 12), width=17, state='readonly')
semCombo['value'] = ('Select Semester', 'Sem-I', 'Sem-II')
semCombo.current(0)
semCombo.grid(row=1, column=3, padx=2, pady=10, sticky=W)

# student class information frame
ClassFrame = LabelFrame(DataLeftFrame, bd=4, relief=RIDGE, text='Student Class Information', padx=2,
                        font=('times new roman', 12, ' bold'), fg='red', bg='white')
ClassFrame.place(x=0, y=240, width=650, height=280)

# ID
def validate_entry(text):
    return text.isdecimal()
idLabel = Label(ClassFrame, font=('arial', 12, ' bold'), bg='white', text='Id ')
idLabel.grid(row=0, column=0, sticky=W, padx=2, pady=10)

idEntry = ttk.Entry(ClassFrame, textvariable=idval, font=('arial', 12), width=20,validate="all",
    validatecommand=(root.register(validate_entry), "%S"))
idEntry.grid(row=0, column=1, sticky=W, padx=2, pady=10)

# Name
def validate_entry(text):
    return text.isalpha()
nameLabel = Label(ClassFrame, font=('arial', 12, ' bold'), bg='white', text='Name ')
nameLabel.grid(row=0, column=2, sticky=W, padx=2, pady=10)

nameEntry = ttk.Entry(ClassFrame, textvariable=nameval, font=('arial', 12), width=20,validate="all",
    validatecommand=(root.register(validate_entry), "%S"))
nameEntry.grid(row=0, column=3, sticky=W, padx=2, pady=10)

# Division
divLabel = Label(ClassFrame, font=('arial', 12, ' bold'), bg='white', text='Division ')
divLabel.grid(row=1, column=0, sticky=W, padx=2, pady=10)

divCombo = ttk.Combobox(ClassFrame, textvariable=divval, font=('arial', 12), width=18, state='readonly')
divCombo['value'] = ('Select Division', 'A', 'B', 'C')
divCombo.current(0)
divCombo.grid(row=1, column=1, padx=2, pady=7)

# Roll
def validate_entry(text):
    return text.isdecimal()

rollLabel = Label(ClassFrame, font=('arial', 12, ' bold'), bg='white', text='Roll No ')
rollLabel.grid(row=1, column=2, sticky=W, padx=2, pady=10)

rollEntry = ttk.Entry(ClassFrame, textvariable=rollval, font=('arial', 12), width=20,validate="all",
    validatecommand=(root.register(validate_entry), "%S"))
rollEntry.grid(row=1, column=3, sticky=W, padx=2, pady=10)

# gender
genderLabel = Label(ClassFrame, font=('arial', 12, ' bold'), bg='white', text='Gender ')
genderLabel.grid(row=2, column=0, sticky=W, padx=2, pady=10)

genderCombo = ttk.Combobox(ClassFrame, textvariable=genderval, font=('arial', 12), width=18, state='readonly')
genderCombo['value'] = ('Select Gender', 'Male', 'Female', 'Other')
genderCombo.current(0)
genderCombo.grid(row=2, column=1, padx=2, pady=10)

# dob
dobLabel = Label(ClassFrame, font=('arial', 12, ' bold'), bg='white', text='DOB ')
dobLabel.grid(row=2, column=2, sticky=W, padx=2, pady=10)

dobEntry = DateEntry(ClassFrame, textvariable=dobval, font=('arial', 12), width=18,selectmode='month',
                     date_pattern='dd/MM/yyyy')
dobEntry.grid(row=2, column=3, sticky=W, padx=2, pady=10)

# email]
emailLabel = Label(ClassFrame, font=('arial', 12, ' bold'), bg='white', text='Student Email ')
emailLabel.grid(row=3, column=0, sticky=W, padx=2, pady=10)

emailEntry = ttk.Entry(ClassFrame, textvariable=emailval, font=('arial', 12), width=20)
emailEntry.grid(row=3, column=1, sticky=W, padx=2, pady=10)

emailEntry.insert(0, "abc@gmail.com")
emailEntry.configure(state=DISABLED)

def on_click(event):
    emailEntry.configure(state=NORMAL)
    emailEntry.delete(0, END)
    emailEntry.bind('<Button-1>', on_click_id)
on_click_id = emailEntry.bind('<Button-1>', on_click)



# phoneno
phoneLabel = Label(ClassFrame, font=('arial', 12, ' bold'), bg='white', text='Phone No')
phoneLabel.grid(row=3, column=2, sticky=W, padx=2, pady=10)

def validate_entry(new_text):
    # No more than ten characters.
    if len(new_text) > 10:
        return False
    checks = []
    for i, char in enumerate(new_text):
        checks.append(char.isdecimal()) #all input are in decimal format
    # `all()` returns True if all checks are True.
    return all(checks)

phoneEntry = ttk.Entry(ClassFrame, textvariable=phoneval, font=('arial', 12), width=20,validate="key",
    validatecommand=(root.register(validate_entry), "%P"))

phoneEntry.grid(row=3, column=3, sticky=W, padx=2, pady=10)

# Address
def validate_entry(text):
    return text.isalpha()
addLabel = Label(ClassFrame, font=('arial', 12, ' bold'), bg='white', text='Address')
addLabel.grid(row=4, column=0, sticky=W, padx=2, pady=10)

addEntry = ttk.Entry(ClassFrame, textvariable=addressval, font=('arial', 12), width=20,validate="all",
    validatecommand=(root.register(validate_entry), "%S"))
addEntry.grid(row=4, column=1, sticky=W, padx=2, pady=10)

# city
def validate_entry(text):
    return text.isalpha()
cityLabel = Label(ClassFrame, font=('arial', 12, ' bold'), bg='white', text='City')
cityLabel.grid(row=4, column=2, sticky=W, padx=2, pady=10)

cityEntry = ttk.Entry(ClassFrame, textvariable=cityval, font=('arial', 12), width=20,validate="all",
    validatecommand=(root.register(validate_entry), "%S"))
cityEntry.grid(row=4, column=3, sticky=W, padx=2, pady=10)

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

# ============ Search frame or student details  frame ======================================

DataRightFrame = LabelFrame(ManageFrame, bd=4, relief=RIDGE, text='Students Details', padx=2,
                            font=('times new roman', 12, ' bold'), fg='red', bg='white')
DataRightFrame.place(x=680, y=10, width=790, height=670)

searchFrame = LabelFrame(DataRightFrame, bd=4, relief=RIDGE, text='Search Student Info', padx=2,
                         font=('times new roman', 12, ' bold'), fg='red', bg='white')
searchFrame.place(x=0, y=20, width=778, height=80)

searchByLabel = Label(searchFrame, font=('arial', 12, ' bold'), bg='black', text='Search By', fg='red')
searchByLabel.grid(row=0, column=0, sticky=W, padx=2, pady=10)

searchComboval = StringVar()
searchCombo = ttk.Combobox(searchFrame, textvariable=searchComboval, font=('arial', 12), width=18, state='readonly')
searchCombo['value'] = ('Select option', 'Id', 'Name', 'Dept', 'Course')
searchCombo.current(0)
searchCombo.grid(row=0, column=1, padx=5, sticky=W)

searchval = StringVar()
searchByEntry = ttk.Entry(searchFrame, textvariable=searchval, font=('arial', 12), width=22)
searchByEntry.grid(row=0, column=2, padx=5)

searchButton = Button(searchFrame, text='Search', width=12, font=('arial', 12, ' bold'), bg='blue', fg='white',
                      command=searchData)
searchButton.grid(row=0, column=3, padx=5)

showAllButton = Button(searchFrame, text='Show All', width=11, font=('arial', 12, ' bold'), bg='blue', fg='white',
                       command=showallData)
showAllButton.grid(row=0, column=4, padx=5)

# ==============================    Student Table and Scroll Bar    ======================================

tableFrame = Frame(DataRightFrame, bd=4, relief=RIDGE)
tableFrame.place(x=0, y=110, width=778, height=520)

scroll_x = Scrollbar(tableFrame, orient=HORIZONTAL)
scroll_y = Scrollbar(tableFrame, orient=VERTICAL)

studenttable = ttk.Treeview(tableFrame, columns=('id', 'name', 'gender', 'dob', 'email', 'phone', 'address',
                                                 'dep', 'course', 'year', 'sem', 'div', 'roll', 'city'),
                            yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
scroll_x.pack(side=BOTTOM, fill=X)
scroll_y.pack(side=RIGHT, fill=Y)
scroll_x.config(command=studenttable.xview)
scroll_y.config(command=studenttable.yview)

studenttable.heading('id', text='Id')
studenttable.heading('name', text='Name')
studenttable.heading('gender', text='Gender')
studenttable.heading('dob', text='D.O.B')
studenttable.heading('email', text='Email')
studenttable.heading('phone', text='Phone No')
studenttable.heading('address', text='Address')
studenttable.heading('dep', text='Department')
studenttable.heading('course', text='Course')
studenttable.heading('year', text='Year')
studenttable.heading('sem', text='Sem')
studenttable.heading('div', text='Division')
studenttable.heading('roll', text='Roll No')
studenttable.heading('city', text='City')
studenttable['show'] = 'headings'

studenttable.pack(fill=BOTH, expand=1)
studenttable.bind('<ButtonRelease>', getCursor)

root.mainloop()