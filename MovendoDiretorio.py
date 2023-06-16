#> > > > > ORIGEM - DESTINO < < < < <

import shutil
import os

origem = 'C:/Users/Caíque/Desktop/CAÍQUE/Senai/Aulas - Programação em Python/VS Code/Origem'
destino = 'C:/Users/Caíque/Desktop/CAÍQUE/Senai/Aulas - Programação em Python/VS Code/Destino'
extensao = '.jpg'

for nomearquivo in os.listdir('Origem'):
    if nomearquivo.endswith(extensao):
        shutil.copy(os.path.join('Origem', nomearquivo), os.path.join('Destino', nomearquivo))
        #os path join: Junção de caminho


#> > > > > REMOVER ARQUIVOS DO DIRETÓRIO < < < < <
'''
import os

diretorio = 'C:/Users/Caíque/Desktop/CAÍQUE/Senai/Aulas - Programação em Python/VS Code/Origem'
extensao = '.jpg'

for nomearquivo in  os.listdir(diretorio):
    if nomearquivo.endswith(extensao):
        os.remove(os.path.join(diretorio, nomerquivo))
'''