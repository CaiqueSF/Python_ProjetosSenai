#= = = = = = = = = = FUNÇÕES = = = = = = = = = =
'''
def prinFunc(nome):
    print(f'Definindo com funções "def" em {nome}')

prinFunc('Python')
prinFunc('C')
prinFunc('C++')
prinFunc('C#')
prinFunc('JAVA.SCRIPT')
prinFunc('HTML')
prinFunc('CSS')
'''

#= = = = = = = = = = FUNÇÃO CALCULADORA = = = = = = = = = =
'''
def calculadora():
    n1 = float(input('Digite o primeiro número: '))
    n2 = float(input('Digite o segundo número: '))
    print('')
    opcao = int(input('Escolha: 1-SOMA === 2-SUBTRAÇÃO === 3-MULTIPLICAÇÃO === 4-DIVISÃO: '))
    print('')

    if opcao == 1:
        print(f'SOMA: {n1} + {n2} = {n1+n2}')
    elif opcao == 2:
        print(f'SUBTRAÇÃO: {n1} - {n2} = {n1-n2}')
    elif opcao == 3:
        print(f'MULTIPLICAÇÃO: {n1} x {n2} = {n1*n2}')
    elif opcao == 4:
        print(f'DIVISÃO: {n1} ÷ {n2} = {n1/n2}')
    else:
        print('OPÇÃO INVÁLIDA!!!')

calculadora()
'''

#= = = = = = = = = = FUNÇÃO VARIAÇÃO = = = = = = = = = =
'''
def variacao(argumento, *argumentoS):
    print('Primeiro argumento:', argumento)
    for x in argumentoS:
        print('Demais argumentos:', x)
    #return

variacao(10)
print('')
variacao('Pão de queijo', 'Café')
print('')
variacao('Brincando', 'com os argumentos', 'seguindo mais ainda')
print('')
'''

#= = = = = = = = = = FUNÇÃO IMPRIME LINHA = = = = = = = = = =
'''
def imprimeLinha(num):
    for x in range(1, num+1):
        print((' {} ').format(x), end='')
    print()

def imprimeSequencia(num):
    for num in range(num+1):
        imprimeLinha(num)

num = input('Digite um número: ')
imprimeSequencia(int(num))
'''

#= = = = = = = = = = FUNÇÃO RELÓGIO = = = = = = = = = =
'''
def relogio(hora, minuto):
    x = hora/12

    if x <= 1:
        h1 = str(hora)
        print(f'Sua hora: {h1}:', end='')
    elif x > 1 and x < 2:
        h2 = str(hora - 12)
        print(f'Sua hora: {h2}:', end='')
    else:
        print('Formato de hora inválido')
    
    if x <= 1 and minuto <= 60:
        print(minuto, 'a.m.')
    elif x > 1 and minuto <= 60:
        print(minuto, 'p.m.')
    else:
        print('Formato de minutos inválido')

while True:
    print('Digite 500 para sair')
    hora = int(input('Informe a hora: '))

    if hora == 500:
        break
    minuto = int(input('Informe os minutos: '))
    relogio(hora, minuto)
    print('')
'''


#= = = = = = = = = = FUNÇÃO PAGAMENTO = = = = = = = = = =
def pagamento():
    diario = []

    while True:
        valor = float(input('Valor da prestação: '))
        atraso = int(input('Dias atrasados: '))
        print('')

        multa = 0.03
        multaDia = 0.001 * atraso
        total = float(valor + (valor * multaDia) + (valor * multa))
        
        print(f'O valor a ser pago é R${total}')
        diario.append(total)
        #append(x): Adiciona um item ao fim da lista... 
        #...prolonga a lista, adicionando no fim todos os elementos do argumento.

        #upper(): retorna os caracteres dentro da string convertidos para 'MAIÚSCULAS'
        #lower(): retorna os caracteres dentro da string convertidos para 'minúsculas'
        continuar = input('Deseja continuar? S/N: ').upper() 
        print('')
        if continuar == 'N' or continuar == 'n':
            break
    
    print(f'As prestações pagas de hoje foram R${diario}')
    print('')

pagamento()