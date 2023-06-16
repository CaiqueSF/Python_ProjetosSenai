'''
#= = = = = Tuple = = = = = VETOR IMUTÁVEL: VARIÁVEIS FIXAS
nome = ('Caíque', 'Senai', 'Curso', 'Python')
print(type(nome))

#= = = = = LIST = = = = = VETOR MUTÁVEL: VARIÁVEIS CONFIGURÁVEIS
nome = ['Caíque', 30, 1.77, 'Dados Pessoais']
print(type(nome[0]))
print(type(nome[1]))
print(type(nome[2]))
print(type(nome[3]))
'''
################################################################################
'''
#= = = = = VETORES = = = = = Len (Length) = Comprimento
nome = [0,0,0,0,0]

for x in range(len(nome)):
    nome[x] = input('Digite o nome do aluno: ')

for x in range(len(nome)):
    print(nome[x])


#= = = = = VETORES = = = = = Len (Length) = Comprimento
n = [0] * 5

for x in range (len(n)):
    n[x] = input(f'Digite o {x+1}º número: ')

for x in range (len(n)):
    print(n[x])
'''
'''
################################################################################
# = = = = = VETORES = = = = =
notas = [0] * 4
media = 0

for x in range(len(notas)):
    notas[x] = float(input(f'Digite a {x+1}º nota: '))
print('')

for x in range(len(notas)):
    print(f'Nota da P{x+1}: {notas[x]}')
    media = media + notas[x]
print('')

print(f'> > > > > Média Final = {media/4} < < < < <')
'''




soma = 0

for numero in range(1, 1000):
    if numero % 3 == 0 or numero % 5 == 0:
        soma += numero

print("A soma dos múltiplos de 3 e 5 abaixo de 1000 é:", soma)
