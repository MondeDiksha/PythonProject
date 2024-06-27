#create a GUI 
#clicking ON button will show date and time and date time

from tkinter import*
from datetime import*

root=Tk()
root.title("4th project by dikshA")
root.geometry("700x500+400+200")
f=("calibri",30,"bold")

def f1():
	dt=datetime.now().date()
	day=dt.day
	month=dt.month
	year=dt.year
	msg="date=" +str(day)+"/"+str(month)+"/"+str(year)
	lab_msg.configure(text=msg)
def f2():
	dt=datetime.now().time()
	hour=dt.hour
	minute=dt.minute
	second=dt.second
	msg="Time="+str(hour)+":"+str(minute)+":"+str(second)
	lab_msg.configure(text=msg)
def f3():
	dt=datetime.now()
	day=dt.day
	month=dt.month
	year=dt.year
	hour=dt.hour
	minute=dt.minute
	second=dt.second
	msg= "date="+str(day)+"/"+str(month)+"/"+str(year)+"  ||  Time="+str(hour)+":"+str(minute)+":"+str(second)
	lab_msg.configure(text=msg)


btn_date=Button(root,text="Date",font=f,width=15,command=f1)
btn_date.pack(pady=10)
btn_time=Button(root,text="Time",font=f,width=15,command=f2)
btn_time.pack(pady=10)
btn_date_time=Button(root,text="Date and Time",font=f,width=15,command=f3)
btn_date_time.pack(pady=10)

lab_msg=Label(root,font=f)
lab_msg.pack(pady=20)
  


root.mainloop()

