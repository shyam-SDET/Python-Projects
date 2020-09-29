from tkinter import *
import parser
from math import factorial
root = Tk()
root.title('Calculator')
root.geometry("400x300")
root.configure(background="black")
root.resizable(0,0)
# input field
display = Entry(root)
display.grid(row=1, columnspan=6, sticky=N+E+W+S)

# buttons
i = 0
def get_variables(num):
    global i
    display.insert(i, num)
    i = i + 1


Button(root, text="1",height=3,width=8, fg="black",bg="pink" ,command=lambda: get_variables(1)).grid(row=4, column=0, sticky=N+S+E+W)
Button(root, text="2",height=3,width=8,fg="black",bg="pink" , command=lambda: get_variables(2)).grid(row=4, column=1, sticky=N+S+E+W)
Button(root, text="3",height=3,width=8,fg="black",bg="pink" , command=lambda: get_variables(3)).grid(row=4, column=2, sticky=N+S+E+W)
Button(root, text="4", height=3, fg="black",bg="pink" ,command=lambda: get_variables(4)).grid(row=3, column=0, sticky=N+S+E+W)
Button(root, text="5", fg="black",bg="pink" ,command=lambda: get_variables(5)).grid(row=3, column=1, sticky=N+S+E+W)
Button(root, text="6",fg="black",bg="pink" , command=lambda: get_variables(6)).grid(row=3, column=2, sticky=N+S+E+W)
Button(root, text="7",height=3, fg="black",bg="pink" ,command=lambda: get_variables(7)).grid(row=2, column=0, sticky=N+S+E+W)
Button(root, text="8", fg="black",bg="pink" ,command=lambda: get_variables(8)).grid(row=2, column=1, sticky=N+S+E+W)
Button(root, text="9",fg="black",bg="pink" , command=lambda: get_variables(9)).grid(row=2, column=2, sticky=N+S+E+W)


def clear_all():
    display.delete(0,END)


Button(root, text="AC",height =3, foreground="black" ,bg="purple",command=lambda: clear_all()).grid(row=5, column=0, sticky=N+S+E+W)
Button(root, text=" 0", fg="black",bg="pink" , command=lambda: get_variables(0)).grid(row=5, column=1, sticky=N+S+E+W)
Button(root, text=".", fg="black", bg="purple" , command=lambda: get_variables(".")).grid(row=5, column=2, sticky=N+S+E+W)


def get_operation(operator):
    global i
    length = len(operator)
    display.insert(i,operator)
    i+=length

Button(root, text="+",height=3,width=8,fg="black", bg="purple" , command=lambda: get_operation("+")).grid(row=2, column=3, sticky=N+S+E+W)
Button(root, text="-", fg="black", bg="purple" ,command=lambda: get_operation("-")).grid(row=3, column=3, sticky=N+S+E+W)
Button(root, text="*", fg="black", bg="purple" ,command=lambda: get_operation("*")).grid(row=4, column=3, sticky=N+S+E+W)
Button(root, text="/", fg="black", bg="purple" ,command=lambda: get_operation("/")).grid(row=5, column=3, sticky=N+S+E+W)
Button(root, text="pi", fg="black", bg="purple" ,height=3,width=8,command=lambda: get_operation("3.14")).grid(row=2, column=4, sticky=N+S+E+W)
Button(root, text="%", fg="black", bg="purple" ,command=lambda: get_operation("%")).grid(row=3, column=4, sticky=N+S+E+W)
Button(root, text="(", fg="black", bg="purple" ,command=lambda: get_operation("(")).grid(row=4, column=4, sticky=N+S+E+W)
Button(root, text="exp",fg="black", bg="purple" , command=lambda: get_operation("**")).grid(row=5, column=4, sticky=N+S+E+W)


def undo():
    entire_string=display.get()
    if len(entire_string):
        new_string=entire_string[:-1]
        clear_all()
        display.insert(0,new_string)
    else:
        clear_all()
        display.insert(0,"error")


Button(root, text="delete",height=3,width=8,fg="black", bg="purple" , command=lambda: undo()).grid(row=2, column=5, sticky=N+S+E+W)
def calculate():
    entire_string=display.get()
    try:
        a=parser.expr(entire_string).compile()
        result=eval(a)
        clear_all()
        display.insert(0,result)
    except Exception:
        clear_all()
        display.insert(0,"error")

def fact():
    entire_string=display.get()
    try:
        result=factorial(int(entire_string))
        clear_all()
        display.insert(0,result)
    except Exception:
        clear_all()
        display.insert(0,"eror")


Button(root, text="x!", fg="black", bg="purple" ,command=lambda: fact()).grid(row=3, column=5, sticky=N+S+E+W)
Button(root, text=")", fg="black", bg="purple" ,command=lambda: get_operation(")")).grid(row=4, column=5, sticky=N+S+E+W)
Button(root, text="^2", fg="black", bg="purple" ,command=lambda: get_variables("**2")).grid(row=5, column=5, sticky=N+S+E+W)
Button(root, text="^2", fg="black", bg="purple" ,command=lambda: get_operation("**2")).grid(row=5, column=5, sticky=N+S+E+W)
Button(root, text="=" ,height=3,bg="red",fg="black", command=lambda: calculate()).grid(columnspan=6, sticky=N+S+E+W)
root.mainloop()