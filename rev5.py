from tkinter import *
window=Tk()


window.title("project")

#textbox
textbox=Entry(window,width=50,bg="red").grid(row=0,column=0)



def data():

	window=Tk()
	da={1:'black',2:"red",3:"blue"}
	window.title("project")
	Label(window,text=da,width=50,bg='blue').grid(row=0,column=1)
	
#lable
Label(window,width=50,bg='blue').grid(row=0,column=1)

Button(window,text='click me',action=data(),width=50,bg='green',fg='black').grid(row=1,column=0)

window.mainloop()