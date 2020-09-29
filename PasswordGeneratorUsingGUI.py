# importing Libraries
from tkinter import *
import random, string
import pyperclip


###initialize window

master = Tk()
master.geometry("500x450")
master.resizable(1,1)
master.title("PASSWORD GENERATOR PROJECT")
# heading
heading = Label(master, text='PASSWORD GENERATOR', font='arial 15 bold').pack()
# Label(root, text='CLOSE', font='arial 15 bold').pack(side=BOTTOM)

###select password length
pass_label = Label(master, text='SELECT PASSWORD LENGTH', font='arial 10 bold').pack()
pass_len = IntVar()
length = Spinbox(master, from_=8, to_=32, textvariable=pass_len, width=21).pack()

#####define function

pass_str = StringVar()


def Generator():
    password = ''
    for x in range(0, 4):
        password = random.choice(string.ascii_uppercase) + random.choice(string.ascii_lowercase) + random.choice(
            string.digits) + random.choice(string.punctuation)
    for y in range(pass_len.get() - 4):
        password = password + random.choice(
            string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation)
    pass_str.set(password)


###button

Button(master, text="GENERATE PASSWORD", command=Generator).pack(pady=7)

Entry(master, textvariable=pass_str).pack()


########function to copy

def Copy_password():
    pyperclip.copy(pass_str.get())


Button(master, text='COPY TO CLIPBOARD', command=Copy_password).pack(pady=7)

# loop to run program
master.mainloop()
