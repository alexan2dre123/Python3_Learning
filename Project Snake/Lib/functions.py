import keyboard
from time import sleep

TECLA_A = 'a'
TECLA_S = 's'
TECLA_D = 'd'
TECLA_W = 'w'


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
    print("-"*20)
    for i in range(0,20):
        for j in range(0,20):
            if (j == 0):
                print("|")
            if (jogador.x == i and jogador.y == j):
                print(jogador.value, end = "")
            elif (fruta.x == i and fruta.y == j):
                print(fruta.value, end = "")
            else:
                print (' ', end = "")
            if (j == 19):
                print("|")
        print (' ')
    print("-"*20)            

def keyboard_setup(jogador):
    if (keyboard.is_pressed("d")):
        jogador.movePlayer("d")
    elif (keyboard.is_pressed("s")):
        print("s")
    elif (keyboard.is_pressed("a")):
        print("a")
    elif (keyboard.is_pressed("w")):
        print("w")
    else:
        pass
