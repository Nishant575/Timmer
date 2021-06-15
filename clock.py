
import tkinter as Tkinter
from tkinter import *
from datetime import datetime
import time
from tkinter import messagebox
counter = 66600
running = False
def counter_label(label):
     def count():
          if running:
               global counter

               # To manage the intial delay.

               tt = datetime.fromtimestamp(counter)
               time = tt.strftime("%H:%M:%S")
               display=time
               label['text']=display
               label.after(1000, count)
               counter += 1
     count()

def Start(label):
	global running
	running=True
	counter_label(label)
	start['state']='disabled'
	stop['state']='normal'
	reset['state']='normal'

def Stop():
	global running
	start['state']='normal'
	stop['state']='disabled'
	reset['state']='normal'
	running = False

def Reset(label):
    global counter
    global running
    counter=66600
    if running==False:
    	reset['state']='disabled'
    	label['text']=string
    else:
        running = False
        start['state'] = 'normal'
        stop['state'] = 'disabled'
        reset['state'] = 'normal'
        label['text'] = string

def Countdown():
    start_count['state']='disabled'
    times = int(hrs.get())*3600+ int(mins.get())*60 + int(sec.get())
    while times > -1:
        minute,second = (times // 60 , times % 60)
        hour = 0
        if minute > 60:
            hour , minute = (minute // 60 , minute % 60)
        sec.set(second)
        mins.set(minute)
        hrs.set(hour)
        root.update()
        time.sleep(1)
        if(times == 0):
            start_count['state']='normal'
            messagebox.showinfo("Time Countdown", "Time's up ")
            sec.set('00')
            mins.set('00')
            hrs.set('00')
        times -= 1

root = Tkinter.Tk()
root.title("Stopwatch")

root.minsize(width=700, height=400)
tt = datetime.fromtimestamp(counter)
string = tt.strftime("%H:%M:%S")

#countdown frame
f1 = LabelFrame(root,font="aria 24 bold", text = 'Countdown timmer' , padx = 10 , pady = 10 , height = 200, width = 700)
f1.pack(fill = X)
label = Tkinter.Label(f1, text=string, fg="black", font="Verdana 50 bold")
label.pack()
f = Tkinter.Frame(f1)
start = Tkinter.Button(f, text='Start', width=13, height=2,
                       font="time 15 bold", command=lambda:Start(label))
stop = Tkinter.Button(f, text='Stop',width=13, height=2,
                      font="time 15 bold",state='disabled', command=Stop)
reset = Tkinter.Button(f, text='Reset',width=13, height=2,
                       font="time 15 bold", state='disabled',
                       command=lambda:Reset(label))
f.pack(anchor = 'center',pady=5)
start.pack(side="left")
stop.pack(side ="left")
reset.pack(side="left")

#timmer frame
f2 = LabelFrame(root,font="aria 24 bold", text = 'Timmer' , padx = 10 , pady = 10 , height = 200, width = 700)
f2.pack(fill = X, pady=50)
tf = Tkinter.Frame(f2)
sec = StringVar()
sec_ent = Entry(tf, textvariable = sec, width = 10, font = 'arial 12')
sec.set('00')
mins= StringVar()
mins_ent = Entry(tf, textvariable = mins, width =10, font = 'arial 12')
mins.set('00')
hrs= StringVar()
hrs_ent = Entry(tf, textvariable = hrs, width =10, font = 'arial 12')
hrs.set('00')
tf.pack(anchor = 'center',pady=5)
hrs_ent.pack(side="left")
mins_ent.pack(side ="left")
sec_ent.pack(side="left")
bf = Tkinter.Frame(f2)
start_count = Tkinter.Button(bf, text='Start', width=13, height=2,
                       font="time 10 bold", command=lambda:Countdown())

bf.pack(anchor = 'center',pady=5)
start_count.pack(side="left")

root.mainloop()
