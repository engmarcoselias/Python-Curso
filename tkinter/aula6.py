from tkinter import *

menu_inicial = Tk()
menu_inicial.title("Primiro App")
menu_inicial['bg'] = "#A9A9A9"
menu_inicial.geometry("400x100+100+100")

#Botão
def click():
    print('Olá Mundo')

btn = Button(menu_inicial,text="Executar", command=click)
btn.pack()


menu_inicial.mainloop()