from tkinter import *
window=Tk()


window.title("gui")

#textbox
textbox=Entry(window,width=50,bg="red").grid(row=0,column=0)

#lable
Label(window,text='this is gui',width=50,bg='blue').grid(row=0,column=1)

Button(window,text='click me',width=50,bg='green',fg='black').grid(row=1,column=0)

window.mainloop()

