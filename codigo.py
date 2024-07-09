

import time
import pyautogui #pyautogui - pacote para automação de mouse, teclado e tela.
import pandas #interação / importação de dados
#PyPDF ou tabula importam dados de PDF

#pyautogui.click - clicar com o mouse
#pyautogui.write - escrever algo 
#pyautogui.press - pressiona um tecla
#pyautogui.hotkey - pressiona uma combinação de teclas
#pyautogui.scroll - correr a tela
#pyautogui.screenshot - captura uma imagem da tela
#pyautogui.size - tamanho da tela
#pyautogui.position - posição do mouse
#pyautogui.moveTo - mover o mouse para uma posição
#pyautogui.moveRel - mover o mouse em relação a posição atual
#pyautogui.doubleClick - duplo clique
#pyautogui.tripleClick - clique triplo
#pyautogui.rightClick - clique direito
#pyautogui.middleClick - clique do meio

pyautogui.PAUSE = 0.5 #considera um tempo de meio segundo entre cada comando executado

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

time.sleep(2) #Defini uma espera antes de continar apenas nesse ponto do código. A função time já vem instalada no python
pyautogui.press("tab")
pyautogui.hotkey("ctrl","a") #seleciona algo que porventura esteja escrito no campo
pyautogui.write("user")
pyautogui.press("tab")
pyautogui.write("senha")
pyautogui.press("enter")

time.sleep(2)
pyautogui.press("tab")


dados = pandas.read_csv("produtos.csv")
print(dados)

for linha in dados.index: #o Python chama cada linha de uma lista de index

    codigo =  str(dados.loc[linha,"codigo"])  #loc localiza um campo(linha e coluna) em uma lista
    marca =  str(dados.loc[linha,"marca"])
    tipo =  str(dados.loc[linha,"tipo"])
    categoria =  str(dados.loc[linha,"categoria"])
    preco =  str(dados.loc[linha,"preco_unitario"])
    custo =  str(dados.loc[linha,"custo"])
    obs =  str(dados.loc[linha,"obs"])

    pyautogui.write(codigo)
    pyautogui.press("tab")

    pyautogui.write(marca)
    pyautogui.press("tab")

    pyautogui.write(tipo)
    pyautogui.press("tab")

    pyautogui.write(categoria)
    pyautogui.press("tab")

    pyautogui.write(preco)
    pyautogui.press("tab")

    pyautogui.write(custo)
    pyautogui.press("tab")

    if obs!= "nan":
        pyautogui.write(obs)
    pyautogui.press("tab")

    pyautogui.press("enter")

    pyautogui.scroll(1000) #roda 100 pixels para cima, para rodar para baixo o número seria negativo
    pyautogui.press("f5")
    pyautogui.press("tab")