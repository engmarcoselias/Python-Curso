from flask import Flask
from tkinter import *

app = Flask(__name__)



@app.route("/")
def index():
    return 'Bem-vindo a TreinaWeb!'

if __name__ == "__main__":
    app.run()

app_main = Tk()

botao = Button(app_main,text="Executar")
botao.pack()

app_main.mainloop()
