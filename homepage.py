from tkinter import *

from PIL import Image, ImageTk  # pip install pillow


def student():
    import student

def faculty():
    import faculty

def course():
    import course



root = Tk()
root.title("Student Management System")  # root.config(bg='')
root.geometry('1530x790+0+0')
root.resizable(False, False)

bgimage = ImageTk.PhotoImage(file='homei.jpeg')  # jpg=ImageTk
bglabel = Label(root, image=bgimage)
bglabel.image=bgimage
bglabel.place(x=0, y=0)

titleLabel = Label(root, font=('Elephant', 40, 'bold'), text='Student Management System',  width=25,
                        fg='white',bg='dimgray')
titleLabel.place(x=260, y=80)

stulogo = ImageTk.PhotoImage(file='student.jpeg')  # jpg=ImageTk
stulabel = Label(root, image=stulogo)
stulabel.place(x=190, y=330)

stuButton = Button(root, text='Student', font=('times new roman', 18, 'bold'), width=15, fg='white', bg='black',
                     cursor='hand2', command=student)
stuButton.place(x=170,y=500)

tealogo = ImageTk.PhotoImage(file='teacher.jpeg')  # jpg=ImageTk
tealabel = Label(root, image=tealogo)
tealabel.place(x=490, y=330)

facButton = Button(root, text='Faculty', font=('times new roman', 18, 'bold'), width=15, fg='white', bg='black',
                     cursor='hand2', command=faculty)
facButton.place(x=470,y=500)


coulogo = ImageTk.PhotoImage(file='course.jpeg')  # jpg=ImageTk
coulabel = Label(root, image=coulogo)
coulabel.place(x=800, y=330)

couButton = Button(root, text='Course', font=('times new roman', 18, 'bold'), width=15, fg='white', bg='black',
                     cursor='hand2', command=course)
couButton.place(x=770,y=500)

root.mainloop();
