"""
#= = = = = = = = DESCONTOS PREMIERE = = = = = = = = 
print('Qual o seu time do coração?')
time = input()

match time:
    case 'Corinthians' | 'Palmeiras' | 'São Paulo' | 'Santos':
        print('')
        print('Acompanhe todos os jogos do CAMPEONATO PAULISTA COM 30% DE DESCONTO')
        print('')

    case 'Flamengo' | 'Fluminense' | 'Vasco' | 'Botafogo':
        print('')
        print('Acompanhe todos os jogos do CAMPEONATO CARIOCA COM 30% DE DESCONTO')
        print('')

    case 'Internacional' | 'Gremio':
        print('')
        print('Acompanhe todos os jogos do CAMPEONATO GAÚCHO COM 30% DE DESCONTO')
        print('')

    case 'Cruzeiro' | 'Atlético Mineiro':
        print('')
        print('Acompanhe todos os jogos do CAMPEONATO MINEIRO COM 30% DE DESCONTO')
        print('')

    case _:
        print('')
        print('No momento não temos promoção para os jogos do seu time')
        print('')
"""

"""
#= = = = = = = = DESCONTOS PREMIERE = = = = = = = = 
valor = float(input('Qual o valor da sua mercadoria: '))
opcao = int(input('Escolha 1 para parcelar ou 2 para pagamento a vista: '))
print('')

match opcao:
    case 1:
        if valor > 1000:
            parcelas = valor/5
            print(f'Mercadorias nesse valor, você pode parcelar em até 5x de R$ {parcelas}') 
            print('')
        else:
            parcelas = valor/3
            print(f'Mercadorias nesse valor, você pode parcelar em até 3x de R$ {parcelas}') 
    case 2:
        if valor > 1000:
            avista = (valor - valor * 0.4)
            print(f'Mercadorias nesse valor A VISTA, tem 40% de desconto. Você pagará {avista}')
        else:
            avista = (valor - valor * 0.2)
            print(f'Mercadorias nesse valor A VISTA, tem 20% de desconto. Você pagará {avista}')

    case _:
        print('OPÇÃO INVÁLIDA, escolha: 1-PARCELADO ou 2-A VISTA')
"""

print('---------------------------')
print('---- CRIANÇA ESPERANÇA ----')
print('---------------------------')
print('')
print('Muito obrigado por ajudar!!')
print('[1] para doar R$10,00')
print('[2] para doar R$25,00')
print('[3] para doar R$50,00')
print('[4] para outros valores')
print('[5] para cancelar')
print('')

valor = 0
x = int(input())

match x:
    case 1:
        valor = 10
    case 2:
        valor = 25
    case 3:
        valor = 50
    case 4:
        valor = int(input('Qual o valor da sua doação R$'))
    case 5:
       print('Que pena, mas agradecemos mesmo assim!')

print('----------------------------')
print(f'  Sua doação foi de R${valor},00')
print('>>>>>> MUITO OBRIGADO <<<<<<')
print('----------------------------')
