#Backup de Arquivos - Módulo de Automação PyAutoGUI - Mouse Position
#Controla mouse/teclado fazendo interações com arquivos e outros aplicativos
import pyautogui
import time

#Pop-Up com mensagem durante 0.5 segundos
pyautogui.alert('O código vai começar. Não use o seu PC enquanto o código está rodando!!!')
pyautogui.PAUSE = 0.5
pyautogui.hotkey('winleft', 'd')    #Windows esquerdo doteclado + 'd' ---> DESKTOP

'''
#> > > > > AUTOMAÇÃO ABRINDO NAVEGADOR < < < < <
#pyautogui.hotkey('winleft', 'r')    #Pressiona 'Windows esquerdo' + 'r' ---> EXECUTAR
pyautogui.press('winleft')          #Pressiona 'Windows esquerdo' 
pyautogui.write('chrome')           #Escreve nome do app para pesquisar
pyautogui.press('enter')            #pressiona 'enter'
time.sleep(1)                       #Pausa o código entre as chamadas

pyautogui.write('https://www.google.com.br/')   #Escreve o endereço do site
pyautogui.press('enter')                        #pressiona 'enter'
pyautogui.alert('Pode navegar a vontade!')
'''

#> > > > > AUTOMAÇÃO COPIA/COLA ARQUIVO < < < < <
#teste = pyautogui.position()
#print(teste)

pyautogui.moveTo(350, 250)          #Move o mouse (x,y,z): DIREÇÕES 'x,y' TEMPO 'z'       
pyautogui.mouseDown()               #Seleciona o arquivo (clicando uma vez)]
pyautogui.moveTo(800, 600)          #Move o mouse (x,y,z): DIREÇÕES 'x,y' TEMPO 'z'
pyautogui.hotkey('ctrl', 'c')
time.sleep(1)

#pyautogui.hotkey('alt', 'tab')      #Altera para a última janela aberta 
pyautogui.press('winleft')       
time.sleep(1)
#pyautogui.write('C:/Users/caiferreira/Documents/Docs Pessoais/Projetos/Python/Teste_Python') 
pyautogui.write('Teste_Python') 
time.sleep(5)        
pyautogui.press('enter') 
time.sleep(1)
   
#pyautogui.mouseUp()                 #Solta o arquivo
pyautogui.hotkey('ctrl', 'v')
time.sleep(3)
pyautogui.alert('O arquivo foi colado no destino. Pode usar seu PC novamente!')