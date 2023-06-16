'''#Importar o módulo > > > #pip install 'biblioteca'
from pytube import YouTube, streams
from pytube.cli import on_progress


#Para inserir URL do vídeo do YouTube
link = input('Insira  link: ')

#Mostrar o progresso de donwload
yt = YouTube(link, on_progress_callback = on_progress)

#Mostrar o título do Vídeo
print('Título = ', yt.title)

#Mostrar que o donwload iniciou
print('Baixando... ... ...')

#Para baixar a maior resolução do vídeo
ys = yt.streams.get_highest_resolution().download()

print('')
print('Seu vídeo foi concluído com sucesso!')
'''

import os, sys
if getattr(sys, 'frozen', False):
    application_path = os.path.dirname(sys.executable)
    os.chdir(application_path)

print('CWD: ' + os.getcwd())