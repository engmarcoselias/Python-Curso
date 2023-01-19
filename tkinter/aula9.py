from tkinter import *

app = Tk()
app.title("App Aula")

label1 = Label(app, text= "este é o label 1.")
label2 = Label(app, text= "este é o label 2.")
botao = Button(app,text= "Executar")

#adicionando o pack

botao.pack()
label1.pack()
label2.pack()



app.mainloop()