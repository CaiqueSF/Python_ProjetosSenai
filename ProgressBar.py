from tkinter import *
from tkinter import ttk

janelaYT = Tk()                #INICAR A JANELA 'TK INTER'
janelaYT.geometry('680x100')   #Largura x Altura
janelaYT.title('Baixar vídeos do YT')
janelaYT['bg'] = 'cyan'

def pb():
    progressBar.step()
    progressBar.start()
    
#ProgressBar
barra = DoubleVar()
barra.set(0)
progressBar = ttk.Progressbar(janelaYT, variable = barra, maximum = 100)
progressBar.grid(row = 1, column = 1, padx = 10, pady = 10, ipadx = 120, ipady= 4)

#BOTÃO PARA INICAR O DOWNLOAD
bt1 = Button(janelaYT, bg = 'blue', text = ' Iniciar Download ', font = 'arial 12 bold', command = lambda: pb())
bt1.grid(row = 1, column = 0, padx = 5, pady = 10)

janelaYT.mainloop()    #EXIBIR A JANELA ATÉ FECHAR
        