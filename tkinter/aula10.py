from tkinter import *

app = Tk()
app.title("App Aula")
app.geometry("200x200+200+200")

label1 = Label(app,
                text= "este é o label 1.",
                bg="#7B68EE",
                fg="black",
                font="Arial 15 bold italic")
label1.pack()
label2 = Label(app,
                text= "este é o label 1.",
                bg="#7B68AA",
                fg="black",
                font="Arial 45 bold italic")
label2.pack()




app.mainloop()