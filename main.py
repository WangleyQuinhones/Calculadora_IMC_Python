from tkinter import *
from tkinter import ttk

#cores
co0='#ffffff'


janela = Tk()
janela.title("Titulo da Janela")
janela.geometry('295x230')
janela.configure(bg=co0)

# dividindo a janela em 2 partes

frame_cima= Frame(janela, width=295, height=50, bg=co0, pady=0, padx=0, relief='flat')
frame_cima.grid(row=1, column=0, sticky=NSEW)

frame_baixo= Frame(janela, width=295, height=180, bg=co0, pady=0, padx=0, relief='flat')
frame_baixo.grid(row=1, column=0, sticky=NSEW)

janela.mainloop()