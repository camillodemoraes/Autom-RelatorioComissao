import pyautogui
import time

# Aguardar 2 segundos
time.sleep(6)

# Obter as coordenadas do cursor do mouse
coordenadas = pyautogui.position()
print("Coordenadas do mouse:", coordenadas)
time.sleep(10)