from pathlib import Path
from shutil import rmtree

######################### Gera/Exibe caminho de pasta/diretório NA MEMÓRIA PYTHON #########################
'''
caminho_diretorio = Path()                   #Caminho absoluto do DIRETÓRIO "pathlib.py"
print(caminho_diretorio.absolute())          #Exibe o caminho no terminal

caminho_arquivo = Path(__file__)                        #Caminho absoluto do ARQUIVO     
print(caminho_arquivo)                                  #Exibe o caminho no terminal
print(caminho_arquivo_parent_parent)                    #Exibe o caminho até um local determinado por você

#Gera o caminho de um Diretório/Arquivo criado APENAS na memória Python 
gera_caminho = caminho_arquivo/'Pasta1'/'Arquivo1.txt'   
print(gera_caminho)                                     #Exibe o caminho do Diretorio/Arquivo gerado
'''

######################### Cria Arquivo no caminho desejado #########################
'''
create_file = Path.home() /'Desktop'/'CAÍQUE'/'Senai'/'Aulas - Programação em Python'/'VS Code'/'ArquivoTeste.txt'

create_file.touch()                                 #Cria 'ArquivoTeste.txt' no caminho determinado acima  
print(create_file)                                  #Exibe o caminho do arquivo criado
create_file.write_text('Hello World!')              #Escreve na primeira linha do arquivo
print(create_file.read_text())                      #Exibe no terminal o conteúdo escrito no arquivo
#create_file.unlink()                                #Apaga o arquivo
'''

######################### Escreve em 2 ou mais linhas do arquivo criado acima #########################
'''
with create_file.open('a+') as file:
    file.write('Primeira linha \r\n')               #\r\n: QUEBRA DE LINHA
    file.write('Segunda linha')              
print(create_file.read_text())

'''

######################### Cria Diretório no caminho desejado #########################

#Cria 'PastaTeste' no caminho pré-determinado 
create_path = Path.home() /'Desktop'/'CAÍQUE'/'Senai'/'Aulas - Programação em Python'/'VS Code'/'PastaTeste'
create_path.mkdir(exist_ok = True)               

#Cria 'subPasta' dentro da pasta >>> create_path
create_subpath = create_path /'subPasta'        
create_subpath.mkdir(exist_ok=True)    

#Cria arquivo dentro do diretório 'PastaTeste' ou 'subPasta'
subArquivo = create_path /'subArquivo.txt'
subArquivo.touch()
subArquivo.write_text('Heeeeey!')
subArquivo_2 = create_subpath /'subArquivo_2.txt'
subArquivo_2.touch()
subArquivo_2.write_text('Hey! Hey! Hey!')

#Cria diversos arquivos dentro do diretório que deseja
variosArquivos = create_path /'variosArquivos'
variosArquivos.mkdir(exist_ok=True)
for i in range(10):
    arquivo = variosArquivos /f'arquivo{i}.txt'

    #Apaga diretório/arquivo gradativamente até chegar no final
    if arquivo.exists():        #Verificar se existe
        arquivo.unlink()
    else:
        arquivo.touch()

    with arquivo.open('a+') as text_arquivo:
        text_arquivo.write('Olá mundo! \r\n')   #Cria arquivo de texto
        text_arquivo.write(f'Arquivo Nº{i}.txt')   #Cria arquivo de texto

#rmtree(create_path)            #Apaga diretório com todo o conteúdo que tiver dentro
#arquivo.is_file():             #Verificar se o arquivo existe
#arquivo.is_dir():              #Verificar se o diretório existe
#arquivo.exists():              #Verificar se existe
#rmdir >>> apagar diretório
#mkdir >>> criar diretório
#exist_ok = True >>> se a pasta já existir, não fazer nada




