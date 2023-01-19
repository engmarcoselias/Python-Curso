from tkinter import *

menu_inicial = Tk()
menu_inicial.title("Primiro App")
menu_inicial['bg'] = "#A9A9A9"#muda cor de fundo
menu_inicial.geometry("400x100+100+100")

#Botão
def click(mensagem):
    print(mensagem)

btn = Button(menu_inicial,text="Executar", command= lambda: click("Hello Word"))
btn.pack()


menu_inicial.mainloop()