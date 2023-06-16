#> > > > > CRIANDO ARQUIVOS < < < < <

arquivo = open('texto.txt', 'a')
#arquivo.write('Manupilando Arquivos')

varios = list()
varios.append('Teste \n')
varios.append('Teste_2 \n')
varios.append('Teste_3 \n')
varios.append('Teste_4 \n')

arquivo.writelines(varios)


#> > > > > LENDO ARQUIVOS < < < < <
'''
arquivo = open('texto.txt', 'r')
print(arquivo.readlines())
#print(arquivo.readline())
#print(arquivo.readline())
#print(arquivo.readline())
'''

#> > > > > Trabalhando com Arquivos < < < < <
'''
arquivo = open(input('Nome do arquivo a ser editado: '), 'a')
#arquivo = open(input('Nome do arquivo a ser editado: '), 'r')
texto = arquivo.readlines()
texto.append(input('Insira o texto: '))

arquivo = open(input('Nome do arquivo a ser editado: '), 'w')
arquivo.writelines(texto)
arquivo.close()
'''