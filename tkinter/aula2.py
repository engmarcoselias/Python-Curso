from tkinter import *#importa a biblioteca tkinter toda

menu_inicial = Tk() #Objeto criado para criar uma janela
menu_inicial.title("Primeiro App")#metodo que passa o parametro titulo
menu_inicial.geometry("400x300+450+100")#altera tamanho e posição da janela
menu_inicial.resizable(True,True)#redimenciona a janela(se True ou 1 = sim, se False ou 0 = não )

#menu_inicial.minsize(width= 200,height= 150)
#menu_inicial.maxsize(900,600)

#menu_inicial.state("zoomed")#iniciar a janela maximizada(iconic = minimizada)
menu_inicial.iconbitmap("tkinter/icon/icone.ico")#alterar icone

menu_inicial.mainloop()#cria um loop 