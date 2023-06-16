"""
#= = = = = = = = = = NOME & IDADE = = = = = = = = = =
nome = input ('Qual o seu nome? ')
idade = int (input ('Qual sua idade? '))

if idade < 18:
    print('')
    print('Desculpe Sr(a)', nome)
    print('Você tem', idade, 'anos, ainda não é permitido tirar a CNH!')
    print('')
else:
    print('')
    print('Parabéns Sr(a)', nome, )
    print('Você tem', idade, 'anos, pode tirar sua CNH!')
    print('')
"""

#= = = = = = = = = = AUMENTO DE SALÁRIO = = = = = = = = = =
print('')
funcionario = input('Digite o nome do funcionário: ')
salario = float(input(f'Qual o salário do {funcionario}: R$'))
print('')

print(f'O Salário do {funcionario} é R$ {salario}')

if salario < 1302:
    print('')
    print(f'O(a) {funcionario} terá um aumento de 50%')
    print(f'A partir de abril, o salário do {funcionario} será R$', (salario * 0.5 + salario))
    print('')
else:  
    print('')
    print(f'O(a) {funcionario} terá um aumento de 30%')
    print(f'A partir de abril, o salário do(a) {funcionario} será R$', (salario * 0.30 + salario))
    print('')

'''
#= = = = = = = = = = MÉDIA ESCOLAR FINAL = = = = = = = = = =
print('')
aluno = input('Digite o nome do aluno: ')
p1 = float(input(f'Qual a nota da Prova 1 do {aluno}: '))
p2 = float(input(f'Qual a nota da Prova 2 do {aluno}: '))
p3 = float(input(f'Qual a nota da Prova 3 do {aluno}: '))
p4 = float(input(f'Qual a nota da Prova 4 do {aluno}: '))
print('')

media = (p1 + p2 + p3 + p4) / 4

if media >= 7:
    print(f'Parabéns {aluno}, sua média é {media}. Você está APROVADO!')
    print('')
elif media >= 4 and media <=6:
    print(f'Estude mais {aluno}, sua média é {media}. Você está DE EXAME!')
    print('')
else:
    print(f'Que pena {aluno}, sua média é {media}. Você está REPROVADO!')
    print('')
'''