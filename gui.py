from tkinter import *

root = Tk()
root.title("Music Player App")
root.geometry("1920x1080")

e =Entry(root,width=50,borderwidth=1.5,fg="blue",bg="yellow")
e.grid(row=0,column=0)
e.get()

def myCLick():
    myLabel = Label(root,text=e.get())
    myLabel.grid(row=3,column=0)        

clickButton = Button(root,text="Click Me!",borderwidth=0,padx=50,command=myCLick,fg="blue",bg="green")

#creating a label widget
my_label = Label(root,text="Music Player")
myLabel = Label(root,text="Welcome to the Music Player App")
#packing it into the screen
my_label.grid(row=1,column=0)
myLabel.grid(row=1,column=0)
clickButton.grid(row=2,column=1)
#clickButton.pack()

root.mainloop()
