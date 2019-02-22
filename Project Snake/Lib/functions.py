import keyboard
from time import sleep

TECLA_A = 'a'
TECLA_S = 's'
TECLA_D = 'd'
TECLA_W = 'w'

ALTURA = 20
LARGURA = 60

class obj(object):
    def __init__(self, x, y, value):
        self.x = x
        self.y = y
        self.value = value
    def movePlayer(self, tecla):
        if (tecla==TECLA_A):
            self.x -= 1
        elif (tecla==TECLA_S):
            self.y += 1
        elif (tecla==TECLA_D):
            self.x += 1
        elif (tecla==TECLA_W):
            self.y -= 1

def mapa(jogador, fruta):
    print("-"*ALTURA*3)
    for i in range(0,ALTURA):
        for j in range(0,LARGURA):
            if (j == 0):
                print("|", end = "")
            if (jogador.x == j and jogador.y == i):
                print(jogador.value, end = "")
            elif (fruta.x == j and fruta.y == i):
                print(fruta.value, end = "")
            else:
                print (' ', end = "")
            if (j == LARGURA-1):
                print("|")

    print("-"*ALTURA*3)

def keyboard_setup(jogador):
    if (keyboard.is_pressed("d")):
        jogador.movePlayer("d")
    elif (keyboard.is_pressed("s")):
        jogador.movePlayer("s")
    elif (keyboard.is_pressed("a")):
        jogador.movePlayer("a")
    elif (keyboard.is_pressed("w")):
        jogador.movePlayer("w")
    else:
        pass
