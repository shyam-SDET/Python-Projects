#import library
from tkinter import *
import datetime
import time
# import winsound
# import simpleaudio as sa
import playsound
def alarm(set_alarm_timer):
    print("Current time is:")
    while True:
        time.sleep(1)
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H:%M:%S")
        date = current_time.strftime("%d/%m/%Y")
        print(date,now)
        if(now>set_alarm_timer):
            print("This time is already gone")
            break
        if now == set_alarm_timer:
            print("Your Alarm is ringing please stop it")
            #winsound.PlaySound("sound.wav",winsound.SND_ASYNC)
            # filename = 'cello.wav'
            # wave_obj = sa.WaveObject.from_wave_file(filename)
            # play_obj = wave_obj.play()
            # play_obj.wait_done()

            playsound.playsound('cello.wav',True)
            break

def actual_time():
    set_alarm_timer = f"{hour.get()}:{min.get()}:{sec.get()}"
    alarm(set_alarm_timer)

clock = Tk()
clock.title("Alarm Clock")
# clock.iconbitmap(r"images.jpg")
clock.geometry("400x400")
time_format=Label(clock, text= "Enter time in 24 hour format!", fg="red",bg="black",font="Arial").place(x=69,y=50)
setYourAlarm = Label(clock,text = "When you want wake up",fg="purple",relief = "solid",font=("Helevetica",15,"bold")).place(x=90, y=10)

# The Variables we require to set the alarm(initialization):
hour = StringVar()
min = StringVar()
sec = StringVar()

#Time required to set the alarm clock:
#hourTime= Entry(clock,textvariable = hour,bg = "pink",width = 15).place(x=110,y=120)
# minTime= Entry(clock,textvariable = min,bg = "pink",width = 15).place(x=155,y=120)
# secTime = Entry(clock,textvariable = sec,bg = "pink",width = 11).place(x=200,y=120)
label1 = Label(clock,text = "Hour ",font=30).place(x = 70,y=120)
label2 = Label(clock,text = "Minutes ",font=30).place(x = 70,y=150)
label3 = Label(clock,text = "Seconds ",font=30).place(x = 70,y=180)
hourTime = Spinbox(clock, from_=1, to_=24, textvariable=hour, width=11).place(x=170,y=120)
minTime = Spinbox(clock, from_=0, to_=59, textvariable=min, width=11).place(x=170,y=150)
secTime = Spinbox(clock, from_=0, to_=59, textvariable=sec, width=11).place(x=170,y=180)

#To take the time input by user:
submit1 = Button(clock,text = "Set Alarm",fg="red",width = 10,command = actual_time).place(x =150,y=230)
button_1 = Button(clock, text =" close the Window",fg="blue",width=20, command = clock.destroy).place(x=120,y=290)
clock.mainloop()
#Execution of the window.

