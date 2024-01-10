from tkinter import *
from tkinter import ttk

#cores
co0='#ffffff' #branca
co1='#444466' #preta
co2='#4065a1' #azul


janela = Tk()
janela.title("Titulo da Janela")
janela.geometry('295x230')
janela.configure(bg=co0)

# dividindo a janela em 2 partes

frame_cima= Frame(janela, width=295, height=50, bg=co0, pady=0, padx=0, relief='flat')
frame_cima.grid(row=0, column=0, sticky=NSEW)

frame_baixo= Frame(janela, width=295, height=180, bg=co0, pady=0, padx=0, relief='flat')
frame_baixo.grid(row=1, column=0, sticky=NSEW)

# configurando frane cima

app_nome = Label(frame_cima, text='Calculadora e IMC', width=23, height=1, padx=0, relief='flat',
                  anchor='center', font=('Ivy 16 bold'), bg=co0, fg=co1)
app_nome.place(x=0, y=0)

app_linha = Label(frame_cima, text='', width=400, height=1, padx=0, relief='flat',
                  anchor='center', font=('Ivy 1'), bg=co2, fg=co1)
app_linha.place(x=0, y=35)

# configurando frane baixo

l_peso = Label(frame_baixo, text='Insira seu peso', height=1, padx=0, relief='flat',anchor='center',
                font=('Ivy 10 bold'), bg=co0, fg=co1)
l_peso.grid(row=0, column=0, sticky=NSEW, pady=10, padx=3)
e_peso = Entry(frame_baixo, width=5, relief='solid', font=('Ivy 10 bold'), justify='center')
e_peso.grid(row=0, column=1, sticky=NSEW, pady=10, padx=3)

l_altura = Label(frame_baixo, text='Insira sua altura', height=1, padx=0, relief='flat',anchor='center',
                font=('Ivy 10 bold'), bg=co0, fg=co1)
l_altura.grid(row=1, column=0, sticky=NSEW, pady=10, padx=3)
e_altura = Entry(frame_baixo, width=5, relief='solid', font=('Ivy 10 bold'), justify='center')
e_altura.grid(row=1, column=1, sticky=NSEW, pady=10, padx=3)

janela.mainloop()