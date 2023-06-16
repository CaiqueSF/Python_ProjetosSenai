contador = 0

x = int(input('Digite um número inteiro: '))

while contador < 10:
    contador += 1
    resultado = x * contador
    print(f'{x} x {contador} = {resultado}')
print(f'Essa é a tabuada do número {x}')