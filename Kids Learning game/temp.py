from tkinter import *
from tkinter import messagebox
import string
import random
import sys

root = Tk()
root.title("Verifing Captcha")

chars = string.ascii_letters + string.digits
name = StringVar()
capt=StringVar


def validation():
    c = name.get()
    if c==capt:
        messagebox.showwarning("Title", "matched")
    else:

        messagebox.showwarning("Title", "not matched")


def cancel():
    exit(0)


head = Frame(root, width=1366, height=45, bg='#3b5998')
head.place(x=0, y=0)

heading = Label(head, text="Password Remider", bg='#3b5998', fg='white', font=('Segoe UI', 20, 'bold'))
heading.place(x=5, y=5)

second = Frame(root, width=400, height=45, bg='white')
second.place(x=40, y=60)

reg = Label(second, text="Reg No.", bg='white', fg='black', font=('Segoe UI', 18, 'bold'))
reg.place(x=3, y=5)

reg_entry = Entry(second, font=('Seogoe UI', 17, 'bold'), bd=5, relief='groove', bg='white')
reg_entry.place(x=110, y=3)



captcha = Frame(root, width=395, height=200, bg='white', relief='ridge', bd=8)
captcha.place(x=40, y=187)
capt=random.choice(chars)
LABEL = Label(captcha, text=capt, font=('jokerman', 80)).pack()

cant = Label(root, text="type the code you see above:", font=('Segoe UI', 18), bg='white')
cant.place(x=40, y=388)



fourth = Frame(root, width=400, height=45, bg='white')
fourth.place(x=40, y=490)

verify = Entry(fourth, font=('Segoe UI', 17, 'bold'), bd=5, relief='groove', bg='white',textvariable=name)
verify.place(x=5, y=5)

star = Label(root, text="*", fg='red', font=('Segoe UI', 20, 'bold'), bg='white')
star.place(x=380, y=490)

bott = Frame(root, width=1366, height=45, bg='light grey')
bott.place(x=0, y=550)


poli_bot = Label(bott, text="Back to login page ", bg='light grey', fg='#3b5998', font=('Segoe UI', 20, 'bold'))
poli_bot.place(x=150, y=2)

contin = Button(bott, text="Submit", font=('arial'), fg='black', bg='#3b5998', command=validation)
contin.place(x=40, y=2)


root.configure(bg='white')
root.geometry("1366x700+0+0")
root.mainloop()