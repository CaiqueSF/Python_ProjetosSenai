import pyautogui
import time
#teste = pyautogui.position()
#print(teste)

#Pop-Up com mensagem durante 0.5 segundos
pyautogui.alert('O arquivo será copiado. Não mexa no PC enquanto o código está rodando!')
pyautogui.PAUSE = 0.5

pyautogui.hotkey('winleft', 'd')    #Windows esquerdo doteclado + 'd' ---> DESKTOP

pyautogui.moveTo(350, 250)          #Move o mouse (x,y,z): DIREÇÕES 'x,y' TEMPO 'z'       
pyautogui.mouseDown()               #Seleciona o arquivo (clicando uma vez)]
pyautogui.moveTo(800, 600)          #Move o mouse (x,y,z): DIREÇÕES 'x,y' TEMPO 'z'

pyautogui.hotkey('ctrl', 'c')
time.sleep(5)                       #Aguarde 2 segundos

pyautogui.hotkey('alt', 'tab')      #Altera para a última janela aberta 
#pyautogui.mouseUp()                 #Solta o arquivo

pyautogui.hotkey('ctrl', 'v')
time.sleep(5)                       #Aguarde 2 segundos

pyautogui.alert('O arquivo foi colado no destino. Pode usar seu PC novamente!')