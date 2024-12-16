# GUI-->graphical user interface

from tkinter import *
root=Tk()
root.title("Square root Finder by Soham Rane")
root.geometry("1000x400")
f=("Arial",40,"bold")

def find():
	try:    
		num=float(ent.get())
		square_root=num**0.5
		res = "square root="+str(round(square_root,2))
		msg.configure(text=res)
	except ValueError:
		res = "You should enter numbers only"
		msg.configure(text=res)
	except TypeError:
		print("You should not enter negative numbers")
		msg.configure(text=res)

lab=Label(root,text="Enter Number ",font=f)
lab.pack(pady=5)
ent=Entry(root,font=f)
ent.pack(pady=5)
btn=Button(root,text="Find Square Root",font=f,command=find)
btn.pack(pady=5)
msg=Label(root,font=f)
msg.pack(pady=5)

root.mainloop()