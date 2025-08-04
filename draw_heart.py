import turtle

t = turtle.Turtle()
screen = turtle.Screen()
screen.setup(500, 600, startx=0, starty=450)
t.color('red', 'pink')

def curve():
    for i in range(200):
        t.right(1)
        t.forward(1)

t.speed(0)  # ปรับความเร็วในการวาด (0 คือเร็วที่สุด)

t.begin_fill()
t.left(140)
t.forward(111.65)
curve()
t.left(120)
curve()
t.forward(111.65)
t.end_fill()

t.hideturtle()
turtle.done()
