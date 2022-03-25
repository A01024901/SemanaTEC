from turtle import *

from freegames import line


def grid():
    """Draw tic-tac-toe grid."""
    line(-67, 200, -67, -200)
    line(67, 200, 67, -200)
    line(-200, -67, 200, -67)
    line(-200, 67, 200, 67)


def drawx(x, y):
    """Draw X player."""
    color("blue")
    line(x, y, x + 100, y + 100)
    line(x, y + 100, x + 100, y)


def drawo(x, y):
    """Draw O player."""
    color("red")
    up()
    goto(x + 58, y + 2)
    down()
    circle(55)


def floor(value):
    """Round value down to grid with square size 133."""
    return ((value + 185) // 133) * 133 - 185


state = {'player': 0}
players = [drawx, drawo]
board=[-1,-1,-1,-1,-1,-1,-1,-1,-1]

def tap(x, y):
    """Draw X or O in tapped square."""
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

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
grid()
update()
onscreenclick(tap)
done()
