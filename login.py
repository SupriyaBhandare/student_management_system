from tkinter import *

from tkinter import Toplevel, messagebox

from PIL import Image, ImageTk  # pip install pillow


def login():
    if userEntry.get() == '' or passEntry.get() == '':
        messagebox.showerror('Error', 'Fields cannot be empty')
    elif userEntry.get()=='admin' and passEntry.get()=='1234':
        messagebox.showinfo('Successful','Welcome to Student Management System')
        root.destroy()
        import homepage

root = Tk()
root.title("Student Management System")  # root.config(bg='')
root.geometry('1530x790+0+0')
root.resizable(False, False)
bgimage = ImageTk.PhotoImage(file='bg1.jpg')  # jpg=ImageTk
bglabel = Label(root, image=bgimage)
bglabel.place(x=0, y=0)
loginFrame = Frame(root)
loginFrame.place(x=700, y=150)
logoImage = PhotoImage(file='logo1.png')
logolabel = Label(loginFrame, image=logoImage)
logolabel.grid(row=0, column=0, columnspan=2, pady=10)

usernameImage = PhotoImage(file='user.png')
usernameLabel = Label(loginFrame, image=usernameImage, text='  Username', compound=LEFT,
                      font=('times new roman', 20, 'bold'))
usernameLabel.grid(row=1, column=0, pady=10, padx=20)

userEntry = Entry(loginFrame, font=('times new roman', 20, 'bold'), bd=5, fg='royalblue')
userEntry.grid(row=1, column=1, pady=10, padx=20)

passwordImage = PhotoImage(file='password.png')
passLabel = Label(loginFrame, image=passwordImage, text='  Password', compound=LEFT,
                  font=('times new roman', 20, 'bold'))
passLabel.grid(row=2, column=0, pady=10, padx=20)

passEntry = Entry(loginFrame, font=('times new roman', 20, 'bold'), bd=5, fg='royalblue')
passEntry.grid(row=2, column=1, pady=10, padx=20)

loginButton = Button(loginFrame, text='Login', font=('times new roman', 18, 'bold'), width=15, fg='white', bg='black',
                     cursor='hand2', command=login)
loginButton.grid(row=3,column=1,pady=25,columnspan=2)


root.mainloop();
