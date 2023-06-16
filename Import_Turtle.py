import turtle

'''
def desenhaQuadrado(t, tamanho):
    for x in range(4):
        t.color('white')
        t.forward(tamanho)
        t.left(90)

janela = turtle.Screen()        #Inicializa a janela e seus atributos
janela.bgcolor('black')
quadrado = turtle.Turtle()      #Cria o quadrado

desenhaQuadrado(quadrado, 50)   #Chama a função para desenhar o quadrado com tamanho 50

quadrado.penup()
quadrado.goto(100, 50) #quadrado.goto(Dist. Horizontal, Dist. Vertical)
quadrado.pendown()

desenhaQuadrado(quadrado, 75) #Chama a função para desenhar o quadrado com tamanho 75

janela.exitonclick()
'''

'''
def desenhaQuadradoColorido(t, tamanho):
    for x in ['red', 'purple', 'hotpink', 'blue']:
        t.color(x)
        t.forward(tamanho)
        t.left(50)
        t.right(90)

janela = turtle.Screen()        #Inicializa a janela e seus atributos
janela.bgcolor('black')         #Cor da janela 
tess = turtle.Turtle()          #Cria tess e seus atributos
tess.pensize(6)
tam = 20                        #Tamanho do menor quadrado

for x in range(15):
    desenhaQuadradoColorido(tess,tam)
    tam = tam + 10          #Aumenta o tamanho para a próxima vez
    tess.forward(10)        #Desloca tess um pouco a frente
    tess.right(18)             #Desloca tess um pouco para a direita

janela.exitonclick()
'''

def desenhaBarra(t, altura):
    t.begin_fill()                          #Comecar a preencher o perfil
    t.left(90)
    t.forward(altura)
    t.write(' ' + str(altura))
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(altura)
    t.left(90)
    t.end_fill()                            #Parar de preencher o perfil

dados = [48, 117, 200, 240, 160, 260, 220]         #Dados
alturaMax = max(dados)
numBarras = len(dados)
moldura = 10

tess = turtle.Turtle()                      #Cria tess e inicializa alguns de seus atributos
tess.color('blue')
tess.fillcolor('red')
tess.pensize(3)

janela = turtle.Screen()                    #Inicializa a janela e seus atributos
janela.bgcolor('lightblue')
janela.setworldcoordinates(0-moldura, 0-moldura, 40*numBarras+moldura, alturaMax+moldura)

for x in dados:
    desenhaBarra(tess, x)

janela.exitonclick()