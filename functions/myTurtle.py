import random
from tkinter.simpledialog import *
from tkinter import Tk

root = Tk()
root.withdraw()
def getString():
    resStr = ''
    resStr = askstring("문자열 입력", "거북이 쓸 문자 입력")
    print(resStr)
    return resStr

def getRGB():
    r, g, b = 0,0,0
    r = random.random()
    g = random.random()
    b = random.random()

    return (r, g, b)


def getXYAS(sw, sh):
    x , y , angle, size = 0,0,0,0
    x = random.randrange(-sw/2 , sw/2)
    y = random.randrange(-sh/2 , sh/2)
    angle = random.randrange(0 , 360)
    size = random.randrange(10, 50)
    return [x , y,angle, size ]

# data = getString()
# getXYAS(500,400)