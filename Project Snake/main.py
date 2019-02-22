from Lib.functions import *
import random
import os

jogador = obj(1, 1, 'o')
fruta = obj(random.randint(0,LARGURA),random.randint(0,ALTURA), '*')

while (True):
    if jogador.x == fruta.x and jogador.y == fruta.y:
        fruta.x = random.randint(0,LARGURA)
        fruta.y = random.randint(0,ALTURA)

    mapa(jogador, fruta)
    keyboard_setup(jogador)
    sleep(0.2)
    os.system('cls')
