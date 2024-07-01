from tkinter import*

root=Tk()
root.title("select choise")
root.geometry("1000x600+300+120")
root.resizable(False,False)
f=("calibari" , 30, "bold")

lab_name=Label(root,text="enter name",font=f)
ent_name=Entry(root,font=f)
lab_name.place(x=50,y=50)
ent_name.place(x=400,y=50)

b=IntVar()
b.set(2)

lab_breakfast=Label(root,text="Fav. Breakfast", font=f)
rb_dosa=Radiobutton(root,text="Dosa",font=f,variable=b,value=1)
rb_poha=Radiobutton(root,text="Poha",font=f,variable=b,value=2)
rb_upma=Radiobutton(root,text="Upma",font=f,variable=b,value=3)

lab_breakfast.place(x=50,y=170)
rb_dosa.place(x=450,y=120)
rb_poha.place(x=450,y=190)
rb_upma.place(x=450,y=260)

def show():
	name=ent_name.get()
	choice=""
	if b.get()==1:
		choice="Dosa"
	elif b.get()==2:	
		choice="Poha"
	else:
		choice="upma"

	msg=str(name)+"'s"+"  "+"choice is "+str(choice)
	lab_msg.configure(text=msg)

btn_submit=Button(root,text="Submit",font=f,command=show)
btn_submit.place(x=400,y=350)
lab_msg=Label(root,font=f)
lab_msg.place(x=300,y=450)

root.mainloop()


















