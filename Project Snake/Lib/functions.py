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
