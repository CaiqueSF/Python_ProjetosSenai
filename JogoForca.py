#Importação dos Módulos a serem utilizados

from tkinter import *   #Módulo para criação da interface
import random           #Seleção de uma palavra aleatória
from playsound import playsound        #Adicionar a música de fundo

def escolha_dificuldade():
    #Pack() ---> utilizado para fixar o label na interface_dificuldade
    Label(interface_dificuldade, text = 'Escola sua dificuldade abaixo', font = ('Arial, 12'), fg = 'Black').pack()

    Button(interface_dificuldade, text = 'Facil - 10 erros permitidos', font = ('Arial, 12'), fg = 'Black',
           command = escolha_dificuldade_facil).pack()
    Button(interface_dificuldade, text = 'Médio - 8 erros permitidos', font = ('Arial, 12'), fg = 'Black',
           command = escolha_dificuldade_medio).pack()
    Button(interface_dificuldade, text = 'Dificil - 6 erros permitidos', font = ('Arial, 12'), fg = 'Black',
           command = escolha_dificuldade_dificil).pack()
    
#Definição do número de erros permitidos e fechamento da janela de dificuldades
def escolha_dificuldade_facil():
    dificuldade.append(10)
    interface_dificuldade.destroy()

def escolha_dificuldade_medio():
    dificuldade.append(8)
    interface_dificuldade.destroy()

def escolha_dificuldade_dificil():
    dificuldade.append(6)
    interface_dificuldade.destroy()

def forca(event):
    cabeca_olhos_nariz = interface_forca.create_oval            #Cria uma forma oval
    corpo = interface_forca.create_line                         #Cria uma linha
    boca = interface_forca.create_arc                           #Cria um arco
    try:
        char = caracter.get().upper()[0]                        #Pega o primeiro caracter e deixa-o maiúsculo
    except IndexError:                                          #Caso o usuário não digite nada e clique enter, faça:
        pass
    else:
        try:
            int(char)                                           #Conferência de que é uma letra
        except ValueError:
            if char not in letras_escolhidas:
                letras_escolhidas.append(char)                  #Atualiza a lista letras_escolhidas
                for indice in range (len(letras)):              #Percorre toda a lista de letras apara conferência
                    if char == letras[indice]:                  #Se o uruário acertou a letra, faça:
                        lista_traco[indice] = letras[indice]    #Atualiza lista_traco
                        caracter_vazio['text'] = lista_traco
                        lista_conferencia.append(char)
                if char not in letras:                          #Atualiza lista_erro
                    lista_erro.append(char)
                    caracteres_anteriores['text'] = lista_erro
    entrada_dados.set('')                                       #Limpa a caixa de entrada do usuário
    if len(lista_conferencia) == len(letras):                   #Caso o usuário acerte todas as letras faça:
        mensagem_final['text'] = 'Jogo ganho! Parabéns'         #Atualiza o texto da mensagem final
        mensagem_final['fg'] = 'green'                          #Atualiza a cor da mensagem final
        caracter.destroy()                                      #Destroi o caracter para impedir mais entrada de dados
        Button(interface, text = 'Finalizar', font = ('Arial, 12'), fg = 'red', command = quit).pack()      #Cria um botão para finalizar

    if len(lista_erro) == dificuldade[0]:                       #Caso o usuário acerte todas as letras faça:
        mensagem_final['text'] = 'Erros máximos atingidos, você perdeu!'    #Atualiza o texto da mensagem final
        mensagem_final['fg'] = 'red'                            #Atualiza a cor da mensagem final
        caracter.destroy()                                      #Destroi o caracter para impedir mais entrada de dados
        Button(interface, text = 'Finalizar', font = ('Arial, 12'), fg = 'red', command = quit).pack()  #Cria um botão para finalizar

    #Desenhar o bonequinho
    if len(lista_erro) == 1:    #Cabeça
        cabeca_olhos_nariz(165, 95, 215, 140, fill = 'gray', outline = 'black')
    if len(lista_erro) == 2:    #Corpo
        corpo(190, 140, 190, 235)
    if len(lista_erro) == 3:    #Braço 1
        corpo(190, 140, 130, 190)
    if len(lista_erro) == 4:    #Braço 2
        corpo(190, 140, 250, 190)
    if len(lista_erro) == 5:    #Perna 1
        corpo(190, 235, 125, 300)
    if len(lista_erro) == 6:    #Perna 2
        corpo(190, 235, 250, 300)
    if len(lista_erro) == 7:    #Olho 1
        cabeca_olhos_nariz(175, 105, 185, 115, fill = 'white', outline = 'black')
    if len(lista_erro) == 8:    #Olho 2
        cabeca_olhos_nariz(195, 105, 205, 115, fill = 'white', outline = 'black')
    if len(lista_erro) == 9:    #Nariz
        cabeca_olhos_nariz(187.5, 117.5, 192.5, 122.5, fill = 'white', outline = 'black')
    if len(lista_erro) == 10:    #Boca
        boca(165, 125, 205, 130, fill = 'white')

def quit():
    interface.destroy()
    playsound.playsound('C:/Users/Caíque/Desktop/CAÍQUE/Senai/Aulas - Programação em Python/VS Code/Teste_Python/musica_fundo.mp3', block = False)

#Leitura do arquivo linha por linha e selecionando aleatoriamente uma das strings
with open('C:/Users/Caíque/Desktop/CAÍQUE/Senai/Aulas - Programação em Python/VS Code/Teste_Python/Palavras.txt') as arq:
    #Usa o split pois cada linha tem a palavra + \n, pegamos a posição [0], pois o split crita uma lista
    leitura = arq.readlines()
    palavra = random.choice(leitura).split('\n')[0].upper()       
#print(palavra)
#print(len(palavra))

#Criação das listas para armazenar os dados
letras = []             #Letras da palavra escolhida aleatoriamente
lista_traco = []        #Traços para apresentar o tamanho da palavra na interface
lista_erro = []         #Letras erradas que o usuário já escolheu 
letras_escolhidas = []  #Todas as letras escolhidas pelo usuário
lista_conferencia = []  #Lita para conferir se o usuário ganhou
dificuldade = []        #Número máximo de erros de acordo com a dificuldade

#Armazenando dados nas listas
for indice in range(len(palavra)):
    letras.append(palavra[indice])
    lista_traco.append(' ___ ')

interface_dificuldade = Tk()        #Cria o objetivo na classe Tk()
escolha_dificuldade()               #Chama a função para interface de escolha de dificuldade
interface_dificuldade.mainloop()    #Mantém a janela aberta até ser fechada

if len(dificuldade) == 1:
    interface = Tk()                
    #Para melhor organização da interface uaremos o canvas
    interface_titulo = Canvas(interface)    #Canvas é uma classe otimizada para construção e organização de formas geométricas
    interface_titulo.pack(side = TOP)       #Definimos que o título está localizada no topo
    interface_forca = Canvas(interface, width = 400, height = 400) #width: comprimento e heigth: largura
    interface_forca.pack(side = TOP)
    interface_texto = Canvas(interface, width = 400, height = 400)
    interface_texto.pack(side = TOP)

    #Criação das haste e forca (coordenadas iniciais, finais e cor)
    interface_forca.create_rectangle(10, 400, 400, 390, fill = 'yellow') #Retangulo para receber as coordenadas
    interface_forca.create_rectangle(10, 400, 20, 30, fill = 'yellow')
    interface_forca.create_rectangle(10, 30, 200, 40, fill = 'yellow')
    interface_forca.create_rectangle(180, 40, 200, 50, fill = 'red')
    interface_forca.create_rectangle(187.5, 50, 192.5, 90, fill = 'black')
    interface_forca.create_oval(160, 90, 220, 145, fill = 'black')
    interface_forca.create_oval(165, 95, 215, 140, fill = 'white')

    #Entrada de texto inicial
    Label(interface_titulo, text = 'Bem vindo ao jogo da forca!', font = ('Atrial, 12'), fg = 'black').pack()
    Label(interface_texto, text = 'Digite sua letra abaixo:\n', font = ('Atrial, 12'), fg = 'black').pack()

    entrada_dados = StringVar() #Variável responsável por receber a string letra do usuário
    caracter = Entry(interface_texto, textvariable = entrada_dados) #usa o entry para reconhecer a entrada de dados
    #passando interface_texto como norteador de onde a caixa de entrada de dados do usuário vai ficar e também
    #passa a variável que será utilizada para armazenar o dado
    caracter.pack() #Adiciona a caixa de entrada a interface
    caracter.bind('<Return>', forca) #Bind realiza a ligação do caracter à função forca a partir de um evento (ex: Enter)

    #Cria a interface de caracteres vázios
    caracter_vazio = Label(interface_texto, text = lista_traco)
    caracter_vazio.pack()

    #Bloco para letras erradas escolhidas pelo usuário
    Label(interface_texto, text = 'Letras erradas').pack()
    caracteres_anteriores = Label(interface_texto, text = lista_erro)
    caracteres_anteriores.pack()

    #Mensagem de vitória ou derrota
    mensagem_final = Label(interface_texto, text = '')
    mensagem_final.pack()
    interface.mainloop()