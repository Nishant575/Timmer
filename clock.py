import tkinter as Tkinter 
from tkinter import *
from datetime import datetime 
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

               # label.after(arg1, arg2) delays by 
               # first argument given in milliseconds 
               # and then calls the function given as second argument. 
               # Generally like here we need to call the 
               # function in which it is present repeatedly. 
               # Delays by 1000ms=1 seconds and call count again. 
               label.after(1000, count) 
               counter += 1

     # Triggering the start of the counter. 
     count()	 
     
# start function of the stopwatch 
def Start(label): 
	global running 
	running=True
	counter_label(label) 
	start['state']='disabled'
	stop['state']='normal'
	reset['state']='normal'
	
# Stop function of the stopwatch 
def Stop(): 
	global running 
	start['state']='normal'
	stop['state']='disabled'
	reset['state']='normal'
	running = False
	
# Reset function of the stopwatch 
def Reset(label): 
	global counter 
	counter=66600
	
	# If rest is pressed after pressing stop. 
	if running==False:	 
		reset['state']='disabled'
		label['text']=string
	
	# If reset is pressed while the stopwatch is running. 
	else:				 
		label['text']=string
	
root = Tkinter.Tk() 
root.title("Stopwatch") 
	
# Fixing the window size. 
root.minsize(width=700, height=700) 
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
sec_ent.pack(side="left") 
mins_ent.pack(side ="left") 
hrs_ent.pack(side="left") 
root.mainloop()
