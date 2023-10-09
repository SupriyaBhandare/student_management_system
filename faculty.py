from tkinter import *
from tkinter import Toplevel, messagebox
from tkinter.ttk import Treeview
from tkinter import ttk
from tkcalendar import DateEntry
import pymysql
from PIL import Image, ImageTk

def student():
    import student

def course():
    import course

root = Toplevel()
root.title("Student Management System")
root.geometry('1530x790+0+0')
root.resizable(False, False)

global con, mycursor
con = pymysql.connect(host='localhost', user='root', password='1234')
mycursor = con.cursor()

idval = StringVar()
nameval = StringVar()
stateval=StringVar()
cityval = StringVar()
addressval = StringVar()
deptval = StringVar()
yearval = StringVar()
semval = StringVar()
courseval = StringVar()
emailval = StringVar()
phoneval = StringVar()
qualival=StringVar()
expeval=StringVar()
dobval = StringVar()
genderval = StringVar()
subjval = StringVar()

# ========================== ADD faculty =====================================

def addData():
    id = idval.get()
    name = nameval.get()
    state = stateval.get()
    city = cityval.get()
    gender = genderval.get()
    dob = dobval.get()
    email = emailval.get()
    phone = phoneval.get()
    address = addressval.get()
    qualification = qualival.get()
    experience = expeval.get()
    subject = subjval.get()
    global con,mycursor
    if (
            idval.get() == '' or nameval.get() == '' or genderval.get() == '' or dobval.get() == '' or emailval.get() == '' or phoneval.get() == ''
            or stateval.get() == '' or cityval.get() == '' or addressval.get() == '' or qualival.get() == '' or expeval.get() == '' or subjval.get() == ''):
        messagebox.showerror('Error', 'All Fields are required',parent=root)
    else:
        try:
            con = pymysql.connect(host='localhost', user='root', password='1234')
            mycursor = con.cursor()
            mycursor.execute('create database sms')
            mycursor.execute('use sms')
            mycursor.execute(
                'create table faculty (id int primary key, name varchar(40),gender varchar(15),dob varchar(50),'
                'email varchar(30),phone varchar(12),state varchar(30),city varchar(30),address varchar(50), '
                'qualification varchar(30),experience varchar(30),subject varchar(30))')
            messagebox.showinfo('Notification', 'Now you are connected to the database successfully',parent=root)
            #mycursor.execute('use sms')
        except:
            mycursor.execute('use sms')
        try:
            # con = pymysql.connect(host='localhost',username='root',password='1234',database='sms1')
            mycursor = con.cursor()
            mycursor.execute('insert into faculty values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
                             (id, name, gender, dob, email, phone, state, city, address, qualification, experience,
                              subject))
            con.commit()  # modify- update
            res=messagebox.askyesnocancel('Notification', 'Data Added Successfully.. You want to clean the form',parent=root)
            if (res == True):
                idval.set('')
                nameval.set('')
                genderval.set('')
                dobval.set('')
                emailval.set('')
                phoneval.set('')
                stateval.set('')
                cityval.set('')
                addressval.set('')
                qualival.set('')
                expeval.set('')
                subjval.set('')
        except Exception as es:
            messagebox.showerror('Error', f'Due to:{str(es)}',parent=root)
        mycursor.execute('select * from faculty')
        data = mycursor.fetchall()
        facultytable.delete(*facultytable.get_children())
        for i in data:
            vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11]]
            facultytable.insert('', END, values=vv)
            con.commit()


# ==================== SEARCH faculty ====================================

def searchData():
    mycursor.execute('use sms')
    if searchComboval.get() == '' or searchval.get() == '':
        messagebox.showinfo('Error', 'Please Select Option',parent=root)
    else:
        try:
            mycursor.execute("select * from faculty where " +str(searchComboval.get())+" LIKE '%"+str(searchval.get())+"%'")
            data = mycursor.fetchall()
            if len(data)!=0:
                facultytable.delete(*facultytable.get_children())
                for i in data:
                    vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11]]
                    facultytable.insert('', END, values=vv)
                con.commit()

        except Exception as es:
            messagebox.showerror('Error',f'Due to:{str(es)}',parent=root)


# ============================= DELETE faculty DATA ============================

def deleteData():
    mycursor.execute('use sms')
    try:
        update = messagebox.askyesnocancel('Update', 'You want to delete the data ',parent=root)
        if (update > 0):
            cc = facultytable.focus()  # shows which record/column you selected
            content = facultytable.item(cc)
            pp = content['values'][0]
            mycursor.execute('delete from faculty where id=%s', (pp))
        else:
            if not update:
                return
        con.commit()
        mycursor.execute('select * from faculty')
        data = mycursor.fetchall()
        facultytable.delete(*facultytable.get_children())
        for i in data:
            vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11]]
            facultytable.insert('', END, values=vv)
        res = messagebox.askyesnocancel('Notification',
                                        'Id {} deleted successfully..You want to clean the form'.format(pp),parent=root)
        if (res == True):
            idval.set('')
            nameval.set('')
            genderval.set('')
            dobval.set('')
            emailval.set('')
            phoneval.set('')
            stateval.set('')
            cityval.set('')
            addressval.set('')
            qualival.set('')
            expeval.set('')
            subjval.set('')
    except Exception as es:
        messagebox.showerror('Error', f'Due to:{str(es)}',parent=root)


# ============================== GET CURSOR DATA ============================


def getCursor(root, event=''):
    mycursor.execute('use sms')
    row = facultytable.focus()  # shows which record/column you selected
    content = facultytable.item(row)
    data = content['values']

    idval.set(data[0])
    nameval.set(data[1])
    genderval.set(data[2])
    dobval.set(data[3])
    emailval.set(data[4])
    phoneval.set(data[5])
    cityval.set(data[6])
    addressval.set(data[7])
    stateval.set(data[8])
    qualival.set(data[9])
    expeval.set(data[10])
    subjval.set(data[11])

    facultytable.bind('<ButtonRelease>', getCursor)


# ============================== UPDATE DATA ================================================

def updateData():
    mycursor.execute('use sms')
    try:
        update = messagebox.askyesnocancel('Update', 'You want to update the data ',parent=root)
        if (update > 0):
            mycursor.execute(
                'update faculty set name=%s,gender=%s,dob=%s,email=%s,phone=%s,address=%s,state=%s,city=%s,'
                'qualification=%s,experience=%s,subject=%s where id=%s',
                (nameval.get(), genderval.get(), dobval.get(), emailval.get(), phoneval.get(),stateval.get(),cityval.get(), addressval.get(),
                 qualival.get(),expeval.get(),subjval.get(),idval.get()))
        else:
            if not update:
                return
        con.commit()
        mycursor.execute('select * from faculty')
        data = mycursor.fetchall()
        facultytable.delete(*facultytable.get_children())
        for i in data:
            vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11]]
            facultytable.insert('', END, values=vv)
        res = messagebox.askyesnocancel('Notification', 'Data Updated Successfully..You want to clean the form',parent=root)
        if (res == True):
            idval.set('')
            nameval.set('')
            genderval.set('')
            dobval.set('')
            emailval.set('')
            phoneval.set('')
            stateval.set('')
            cityval.set('')
            addressval.set('')
            qualival.set('')
            expeval.set('')
            subjval.set('')
    except Exception as es:
        messagebox.showerror('Error', f'Due to:{str(es)}',parent=root)



# =============================== RESET DATA======================================
def resetData():
    idval.set('')
    nameval.set('')
    genderval.set('Select Gender')
    dobval.set('')
    emailval.set('')
    phoneval.set('')
    stateval.set('Select State')
    cityval.set('')
    addressval.set('')
    qualival.set('')
    expeval.set('')
    subjval.set('Select Subject')



# ============================== SHOW ALL  ======================================

def showallData():
    con = pymysql.connect(host='localhost', user='root', password='1234', database='sms1')
    mycursor = con.cursor()
    mycursor.execute('use sms')
    mycursor.execute('select * from faculty')
    data = mycursor.fetchall()

    if len(data) != 0:
        facultytable.delete(*facultytable.get_children())
        for i in data:
            # vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11], i[12], i[13]]
            facultytable.insert('', END, values=i)
        con.commit()


# ===============================Starting===========================================

bgimage = ImageTk.PhotoImage(file='bg3.jpeg')  # jpg=ImageTk
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

stuButton=Button(root, text='Students', font=('cambria', 18, ' bold'), fg='blue',command=student)
stuButton.place(x=1200,y=20)

facButton=Button(root, text='Faculty', font=('cambria', 18, ' bold'), fg='blue')
facButton.place(x=1350,y=20)

DataLeftFrame = LabelFrame(ManageFrame, bd=4, relief=RIDGE, text='Faculty Information', padx=2,
                           font=('times new roman', 12, ' bold'), fg='sienna', bg='white')
DataLeftFrame.place(x=10, y=10, width=660, height=670)


#For image
image = ImageTk.PhotoImage(file='fgirl.jpeg')  # jpg=ImageTk
label = Label(DataLeftFrame, image=image)
label.place(x=5 , y=0)

image1 = PhotoImage(file='boy.png')  # jpg=ImageTk
label1 = Label(DataLeftFrame, image=image1)
label1.place(x=510, y=0)

facLabel = Label(DataLeftFrame, text='Faculty', width=23, font=('times', 15, ' bold'))
facLabel.place(x=180, y=35, height=50)

# current course information frame
facultyFrame = LabelFrame(DataLeftFrame, bd=4, relief=RIDGE, text='Information', padx=2,
                         font=('times new roman', 12, ' bold'), fg='sienna', bg='white')
facultyFrame.place(x=0, y=120, width=650, height=390)

# Labels
# ID
def validate_entry(text):
    return text.isdecimal()

idLabel = Label(facultyFrame, font=('arial', 12, ' bold'), bg='white', text='Id ')
idLabel.grid(row=0, column=0, sticky=W, padx=2, pady=10)

idEntry = ttk.Entry(facultyFrame, textvariable=idval, font=('arial', 12), width=20,validate="key",validatecommand=(root.register(validate_entry), "%S"))
idEntry.grid(row=0, column=1, sticky=W, padx=2, pady=10)

# Name
def validate_entry(text):
    return text.isalpha()

nameLabel = Label(facultyFrame, font=('arial', 12, ' bold'), bg='white', text='Name')
nameLabel.grid(row=0, column=2, sticky=W, padx=2, pady=10)

nameEntry = ttk.Entry(facultyFrame, textvariable=nameval, font=('arial', 12), width=20,validate="key",validatecommand=(root.register(validate_entry), "%S"))
nameEntry.grid(row=0, column=3, sticky=W, padx=2, pady=10)

# gender
genderLabel = Label(facultyFrame, font=('arial', 12, ' bold'), bg='white', text='Gender ')
genderLabel.grid(row=2, column=0, sticky=W, padx=2, pady=10)

genderCombo = ttk.Combobox(facultyFrame, textvariable=genderval, font=('arial', 12), width=18, state='readonly')
genderCombo['value'] = ('Select Gender', 'Male', 'Female', 'Other')
genderCombo.current(0)
genderCombo.grid(row=2, column=1, padx=2, pady=10)

# dob

dobLabel = Label(facultyFrame, font=('arial', 12, ' bold'), bg='white', text='DOB ')
dobLabel.grid(row=2, column=2, sticky=W, padx=2, pady=10)

dobEntry = DateEntry(facultyFrame, textvariable=dobval, font=('arial', 12), width=18,selectmode='month',
                     date_pattern='dd/MM/yyyy')
dobEntry.grid(row=2, column=3, sticky=W, padx=2, pady=10)

#Email
emailLabel = Label(facultyFrame, font=('arial', 12, ' bold'), bg='white', text='Email ')
emailLabel.grid(row=3, column=0, sticky=W, padx=2, pady=10)

emailEntry = ttk.Entry(facultyFrame, textvariable=emailval, font=('arial', 12), width=20)
emailEntry.grid(row=3, column=1, sticky=W, padx=2, pady=10)

emailEntry.insert(0, "abc@gmail.com")
emailEntry.configure(state=DISABLED)

def on_click(event):
    emailEntry.configure(state=NORMAL)
    emailEntry.delete(0, END)
    emailEntry.bind('<Button-1>', on_click_id)
on_click_id = emailEntry.bind('<Button-1>', on_click)

# phoneno
def validate_entry(new_text):
    # No more than ten characters.
    if len(new_text) > 10:
        return False
    checks = []
    for i, char in enumerate(new_text):
        checks.append(char.isdecimal()) #all input are in decimal format
    # `all()` returns True if all checks are True.
    return all(checks)

phoneLabel = Label(facultyFrame, font=('arial', 12, ' bold'), bg='white', text='Phone No')
phoneLabel.grid(row=3, column=2, sticky=W, padx=2, pady=10)

phoneEntry = ttk.Entry(facultyFrame, textvariable=phoneval, font=('arial', 12), width=20,validate="key",
    validatecommand=(root.register(validate_entry), "%P"))
phoneEntry.grid(row=3, column=3, sticky=W, padx=2, pady=10)

#state
stateLabel = Label(facultyFrame, font=('arial', 12, ' bold'), bg='white', text=' State ')
stateLabel.grid(row=4, column=0, sticky=W, padx=2, pady=10)

stateCombo = ttk.Combobox(facultyFrame, textvariable=stateval, font=('arial', 12), width=18, state='readonly')
stateCombo['value'] = ('Select State', 'Maharashtra', 'Karnataka', 'UP','Gujrat','Goa')
stateCombo.current(0)
stateCombo.grid(row=4, column=1, padx=2, pady=10)

# city
def validate_entry(text):
    return text.isalpha()
cityLabel = Label(facultyFrame, font=('arial', 12, ' bold'), bg='white', text='City')
cityLabel.grid(row=4, column=2, sticky=W, padx=2, pady=10)

cityEntry = ttk.Entry(facultyFrame, textvariable=cityval, font=('arial', 12), width=20,validate="key",validatecommand=(root.register(validate_entry), "%S"))
cityEntry.grid(row=4, column=3, sticky=W, padx=2, pady=10)

# Address
def validate_entry(text):
    return text.isalpha()
addLabel = Label(facultyFrame, font=('arial', 12, ' bold'), bg='white', text='Address')
addLabel.grid(row=5, column=0, sticky=W, padx=2, pady=10)

addEntry = ttk.Entry(facultyFrame, textvariable=addressval, font=('arial', 12), width=20,validate="all",
    validatecommand=(root.register(validate_entry), "%S"))
addEntry.grid(row=5, column=1, sticky=W, padx=2, pady=10)

#qualification
def validate_entry(text):
    return text.isalpha()
qualiLabel = Label(facultyFrame, font=('arial', 12, ' bold'), bg='white', text=' Qualification ')
qualiLabel.grid(row=5, column=2, sticky=W, padx=2, pady=10)

qualiEntry = ttk.Entry(facultyFrame, textvariable=qualival, font=('arial', 12), width=20,validate="all",
    validatecommand=(root.register(validate_entry), "%S"))
qualiEntry.grid(row=5, column=3, sticky=W, padx=2, pady=10)

#Experience
def validate_entry(new_text):
    # No more than ten characters.
    if len(new_text) > 2:
        return False
    checks = []
    for i, char in enumerate(new_text):
        checks.append(char.isdecimal()) #all input are in decimal format
    # `all()` returns True if all checks are True.
    return all(checks)

expLabel = Label(facultyFrame, font=('arial', 12, ' bold'), bg='white', text=' Experience ')
expLabel.grid(row=6, column=0, sticky=W, padx=2, pady=10)

expEntry = ttk.Entry(facultyFrame, textvariable=expeval, font=('arial', 12), width=20,validate="key",
    validatecommand=(root.register(validate_entry), "%P"))
expEntry.grid(row=6, column=1, sticky=W, padx=2, pady=10)

#subject
subLabel = Label(facultyFrame, font=('arial', 12, ' bold'), bg='white', text=' Subject ')
subLabel.grid(row=6, column=2, sticky=W, padx=2, pady=10)

subCombo = ttk.Combobox(facultyFrame, textvariable=subjval, font=('arial', 12), width=18, state='readonly')
subCombo['value'] = ('Select Subject', 'Maths', 'English', 'Science','C','C++','Java','Python','DBMS')
subCombo.current(0)
subCombo.grid(row=6, column=3, padx=2, pady=10)

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

# ============ Search frame or faculty details  frame ======================================

DataRightFrame = LabelFrame(ManageFrame, bd=4, relief=RIDGE, text='Faculty Details', padx=2,
                            font=('times new roman', 12, ' bold'), fg='sienna', bg='white')
DataRightFrame.place(x=680, y=10, width=790, height=670)

searchFrame = LabelFrame(DataRightFrame, bd=4, relief=RIDGE, text='Search Faculty Info', padx=2,
                         font=('times new roman', 12, ' bold'), fg='sienna', bg='white')
searchFrame.place(x=0, y=20, width=778, height=80)

searchByLabel = Label(searchFrame, font=('arial', 12, ' bold'), bg='black', text='Search By', fg='red')
searchByLabel.grid(row=0, column=0, sticky=W, padx=2, pady=10)

searchComboval = StringVar()
searchCombo = ttk.Combobox(searchFrame, textvariable=searchComboval, font=('arial', 12), width=18, state='readonly')
searchCombo['value'] = ('Select option', 'Id', 'Name', 'Qualification', 'Subject')
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

# ==============================    Faculty Table and Scroll Bar    ======================================

tableFrame = Frame(DataRightFrame, bd=4, relief=RIDGE)
tableFrame.place(x=0, y=110, width=778, height=520)

scroll_x = Scrollbar(tableFrame, orient=HORIZONTAL)
scroll_y = Scrollbar(tableFrame, orient=VERTICAL)

facultytable = ttk.Treeview(tableFrame, columns=('id', 'name', 'gender','dob', 'email', 'phone', 'city', 'address','state','qualification',
'experience' ,'subject'),
                            yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
scroll_x.pack(side=BOTTOM, fill=X)
scroll_y.pack(side=RIGHT, fill=Y)
scroll_x.config(command=facultytable.xview)
scroll_y.config(command=facultytable.yview)

facultytable.heading('id', text='Id')
facultytable.heading('name', text='Name')
facultytable.heading('gender', text='Gender')
facultytable.heading('dob', text='DOB')
facultytable.heading('email', text='Email')
facultytable.heading('phone', text='Phone No')
facultytable.heading('state', text='State')
facultytable.heading('city', text='City')
facultytable.heading('address', text='Address')
facultytable.heading('qualification', text='Qualification')
facultytable.heading('experience', text='Experience')
facultytable.heading('subject', text='Assigned Subject')

facultytable['show'] = 'headings'

facultytable.pack(fill=BOTH, expand=1)
facultytable.bind('<ButtonRelease>', getCursor)

root.mainloop()
