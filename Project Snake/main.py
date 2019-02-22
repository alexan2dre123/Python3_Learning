from Lib.functions import *
import os

jogador = obj(1, 1, 'o')

while (True):
    mapa(jogador, jogador)
    keyboard_setup(jogador)
    sleep(0.2)
    os.system('cls')
