from turtle import *

from freegames import line


def grid():
    line(-67, 200, -67, -200)
    line(67, 200, 67, -200)
    line(-200, -67, 200, -67)
    line(-200, 67, 200, 67)


def drawx(x, y):
    color("blue")
    line(x, y, x + 100, y + 100)
    line(x, y + 100, x + 100, y)


def drawo(x, y):
    color("red")
    up()
    goto(x + 58, y + 2)
    down()
    circle(55)


def floor(value):
    return ((value + 185) // 133) * 133 - 185


state = {'player': 0}
players = [drawx, drawo]


def tap(x, y):
    x = floor(x)
    y = floor(y)
    print(x,y)
    boxpos=box(x,y)
    print(boxpos)
    player = state['player']
    draw = players[player]
    draw(x, y)
    update()
    state['player'] = not player
  
def box(x, y):
    if x==-52 and y==-52:
       return 4
    if x==-185 and y==81:
       return 0
    if x==-52 and y==81:
       return 1
    if x==81 and y==81:
       return 2
    if x==-185 and y==-52:
       return 3
    if x==81 and y==-52:
       return 5
    if x==-185 and y==-185:
       return 6
    if x==-52 and y==-185:
       return 7 
    if x==81 and y==-185:
       return 8

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
grid()
update()
onscreenclick(tap)
done()
