from tkinter import *
from tkinter import ttk

janela = Tk()
janela.title("Titulo da Janela")
janela.geometry('295x230')
janela.configure(bg='white')

# dividindo a janela em 2 partes

frame_cima= Frame(janela, width=295, height=50, bg='white', pady=0, padx=0, relief='flat')
frame_cima.grid(row=1, column=0, sticky=NSEW)

frame_baixo= Frame(janela, width=295, height=180, bg='white', pady=0, padx=0, relief='flat')
frame_baixo.grid(row=1, column=0, sticky=NSEW)

janela.mainloop()