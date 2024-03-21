import os
import time
import pyautogui

# Caminho para o arquivo do LibreOffice Calc
caminho_arquivo = r'G:\FOLHA\COMISSAO DE PEÇAS E SERVIÇOS.xlsx'

# Abrir o arquivo Calc usando o LibreOffice
os.startfile(caminho_arquivo)

# Aguarde alguns segundos para o LibreOffice abrir completamente
time.sleep(4)

# Passo 2: Clicar em "DADOS" na barra de ferramentas
# Substitua as coordenadas pelo local onde o botão "DADOS" está localizado
pyautogui.click(x=410, y=46)

# Passo 3: Clicar em "ATUALIZAR TODOS" na opção dados
time.sleep(2)  # Esperar um pouco para que a janela de "DADOS" seja aberta
# Substitua as coordenadas pelo local onde o botão "ATUALIZAR TODOS" está localizado
pyautogui.click(x=426, y=91)

# Passo 4: Esperar 30 segundos
time.sleep(5)

# Passo 5: Salvar a planilha e fechar o arquivo Calc
pyautogui.hotkey('ctrl', 's')  # Atalho para salvar
time.sleep(2)  # Esperar um pouco para a janela de salvar aparecer
pyautogui.press('enter')  # Pressionar Enter para confirmar a ação de salvar

time.sleep(2)  # Aguardar um pouco antes de fechar o arquivo
pyautogui.hotkey('ctrl', 'q')  # Atalho para fechar o arquivo

print("O arquivo foi atualizado, salvo e fechado com sucesso.")