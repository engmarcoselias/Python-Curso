from tkinter import *

app  = Tk()
app.title("App Aula")

#dimensoes da janela

largura = 500
altura = 300

#resolução do nosso sistema

largura_screen = app.winfo_screenwidth()
altura_screen = app.winfo_screenheight()

print(largura_screen, altura_screen)

#posição da janela

posx = (largura_screen/2) - (largura/2)
posy = (altura_screen/2) -(altura/2)

#definir geometria

app.geometry("%dx%d+%d+%d" %(largura,altura,posx,posy))

app.mainloop()



