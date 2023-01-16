from tkinter import *
win = Tk()

#add widgets from here

win.geometry("300x200+10+20")
win.title("My First GUI Application")

#label widgets
lbl = Label(win, text="My First GUI", fg="Red")
lbl.place(x=10, y = 10)

lbl2 = Label(win, text="First Text Field:")
lbl2.place(x=5, y = 50)

lbl3 = Label(win, text="Second Text Field:")
lbl3.place(x=5, y = 70)

#add button widgets
btn = Button(win,text="Yes", fg="Blue", font=("Verdana", 10))
btn.place(x = 120, y = 100)

btn = Button(win,text="No", fg="Blue", font=("Verdana", 10))
btn.place(x = 180, y = 100)

#add entry widgets
txtfld = Entry(win,text="This is an entry widget", bd=3)
txtfld.place(x=120, y = 50)

txtfld2 = Entry(win,text="This is an entry widget", bd=3)
txtfld2.place(x=120, y = 70)

#add radio button
def sel():
    selection = "You selected option" + str(var.get())
    lbl.config(text=selection)
var = IntVar()

r1 = Radiobutton(win, text="Male", variable=var, value=1, command= sel)
#r1.place(x=110, y = 150)
r1.pack(side="bottom", anchor=N)

r1 = Radiobutton(win, text="Female", variable=var, value=2, command= sel)
#r1.place(x=170, y = 150)
r1.pack(side="bottom", anchor=N)
label = Label(win)
label.pack()

win.mainloop()
