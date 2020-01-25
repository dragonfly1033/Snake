from tkinter import *
from random import randint
from copy import deepcopy
from time import sleep
import restartSnake, sys

tail = [[9,9]]
squares = []

curDir = 'right'
foodPos = [randint(0,19), randint(0,19)]
after_id = None


def toggle(coord):
    s = squares[coord[1]][coord[0]]
    cc = s.g.cget('bg')
    if (cc == 'black'):
        s.g.configure(bg='green')
    else:
        s.g.configure(bg='black')


def move():
    tempTail = deepcopy(tail)

    if (curDir == 'up'):
        tail[0][1] -= 1
    elif (curDir == 'down'):
        tail[0][1] += 1
    elif (curDir == 'right'):
        tail[0][0] += 1
    elif (curDir == 'left'):
        tail[0][0] -= 1

    for i in range(1, len(tail)):
        tail[i] = tempTail[i-1]

def food():
    global foodPos
    squares[foodPos[1]][foodPos[0]].g.configure(bg='black')
    foodPos = [randint(0, 19), randint(0, 19)]
    squares[foodPos[1]][foodPos[0]].g.configure(bg='red')


def addTail():
    global tail
    if(curDir == 'up'):
        tail.append([tail[-1][0], tail[-1][1]+1])
    elif(curDir == 'down'):
        tail.append([tail[-1][0], tail[-1][1]-1])
    elif(curDir == 'left'):
        tail.append([tail[-1][0]+1, tail[-1][1]])
    elif(curDir == 'right'):
        tail.append([tail[-1][0]-1, tail[-1][1]])

def endGame(id):
    root.destroy()
    restartSnake.restart(__file__) 
    sys.exit() 

def update():
    global after_id
    for i in tail:
        toggle(i)
    move()

    if(tail[0] == foodPos):
        food()
        addTail()
    elif(tail[0] in tail[1:]):
        endGame(after_id)
    elif(max(tail[0]) > 19 or min(tail[0]) < 0):
        endGame(after_id)

    for i in tail:
        toggle(i)

    after_id = root.after(100, update)


def changeDir(dir):
    global curDir
    if(curDir == 'right' and dir == 'left'):
        pass
    elif(curDir == 'left' and dir == 'right'):
        pass
    elif(curDir == 'up' and dir == 'down'):
        pass
    elif(curDir == 'down' and dir == 'up'):
        pass
    else:
        curDir = dir


class square(object):
    """docstring for square"""

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.g = Frame(root, bg='black', width=30, height=30)
        self.g.grid(column=x, row=y, padx=1, pady=1)


root = Tk()

root.configure(bg='dark grey')
root.bind('<Up>', lambda x: changeDir('up'))
root.bind('<Down>', lambda x: changeDir('down'))
root.bind('<Right>', lambda x: changeDir('right'))
root.bind('<Left>', lambda x: changeDir('left'))

for y in range(20):
    squares.append([])
    for x in range(20):
        q = square(x, y)
        squares[y].append(q)

toggle(tail[0])
food()
root.after(3000, update)

root.mainloop()


