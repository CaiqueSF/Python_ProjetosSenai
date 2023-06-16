#= = = = = SERVIÇOS = = = = =
meses = ('JANEIRO', 'FEVEREIRO', 'MARÇO', 'ABRIL', 'MAIO', 'JUNHO', 'JULHO', 'AGOSTO', 'SETEMBRO', 'OUTUBRO', 'NOVEMBRO', 'DEZEMBRO')
opcao = int(input('Escolha: 1- ADICIONAR SERVIÇO ===== 2- SAIR DO SISTEMA: '))
print('')

totalServicos = [] #LIST PARA IR ADICIONAR SERVIÇOS NO 'append'
totalValor = [] #LIST PARA IR ADICIONAR VALORES NO 'append'

def servicos():
    if opcao == 1:
        for x in range(len(meses)): 
            servico = input(f'Qual o serviço prestado em {meses[x]}? ')
            totalServicos.append(servico)
            valor = float(input('Valor o valor do serviço? R$'))
            totalValor.append(valor)
            continuar = input('Deseja adicionar mais serviços? S/N ou F para FINALIZAR: ')
            print('')

            while(True):
                if continuar == 'S' or continuar == 's':
                    servico = input(f'Qual o serviço prestado em {meses[x]}? ')
                    totalServicos.append(servico)
                    valor = float(input('Valor o valor do serviço? R$'))
                    totalValor.append(valor)
                    continuar = input('Deseja adicionar mais serviços? S/N ou F para FINALIZAR: ') 
                    print('') 

                elif continuar == 'N' or continuar == 'n':
                    print(f'Seus serviços prestados até o momento foram: {totalServicos}')
                    print(f'Dinheiro recebido até o momento R${totalValor}')
                    print('')
                    break
                
                else:
                    print(f'Seus serviços prestados foram: {totalServicos}')
                    print(f'Dinheiro TOTAL recebido R${totalValor}')
                    print('')
                    print('======================================')
                    print('Obrigado por utilizar nossos serviços!')
                    print('======================================')
                    print('')
                    break         
    
    if opcao == 2:
        print('======================================')
        print('Obrigado por utilizar nossos serviços!')
        print('======================================')
                    
servicos()