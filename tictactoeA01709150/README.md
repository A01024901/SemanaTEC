## Diego Perdomo Salcedo (A01709150)

### TicTacToe Code

    from turtle import *

    from freegames import line

Draws the tic tac toe grid

    def grid():
            line(-67, 200, -67, -200)
            line(67, 200, 67, -200)
            line(-200, -67, 200, -67)
            line(-200, 67, 200, 67)

Draws the symbol X.
Changed the value of the numbers so the X could be smaller and changed its color to blue.

    def drawx(x, y):
            color("blue")
            line(x, y, x + 100, y + 100)
            line(x, y + 100, x + 100, y)

Draws the circle/O.
Changed the values that represent the size of the circle to make it smaller, as well as the color from black to red.

    def drawo(x, y):
            color("red")
            up()
            goto(x + 58, y + 2)
            down()
            circle(55)

Centers the symbols in each box of the grid.
Changed the values from 200 to 185 to center the symbols after the size of the symbols was changed.

    def floor(value):
            return ((value + 185) // 133) * 133 - 185

Players turn to draw the symbols.

    state = {'player': 0}
    players = [drawx, drawo]
   

Draws the X or O in the tapped square.
Changed so it prints in what coordinate the symbol is and in what box it was drawn.

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

New function added that tells in what box the symbol is depending on its coordinates.

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

Following functions make the code run.

    setup(420, 420, 370, 0)
    hideturtle()
    tracer(False)
    grid()
    update()
    onscreenclick(tap)
    done()



