#Importar o módulo > > > #pip install 'biblioteca'
from pytube import YouTube, streams
from pytube.cli import on_progress

#Para inserir URL do vídeo do YouTube
link = input('Insira o link: ')

#Mostrar o progresso de donwload
yt = YouTube(link, on_progress_callback= on_progress)

#Mostrar o título do Vídeo
print(f'{yt.author} - {yt.title}')

#Mostrar que o donwload iniciou
print('Baixando... ... ...')

#Para baixar a maior resolução do vídeo
ys = yt.streams.get_highest_resolution().download()

print('')
print('O download do seu vídeo foi concluído com sucesso!')