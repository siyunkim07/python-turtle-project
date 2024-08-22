import turtle as t
import random
def draw_dot(x,y):
    t.up()
    t.goto(x,y)
    t.dot(size)
def rand_color():
    t.color(random.choice(color))

def draw_triangle(x,y):
    t.up()
    t.goto(x,y)
    t.down()
    t.begin_fill()
    for i in range(3):
        t.forward(size)
        t.left(360 / 3)
    t.end_fill()
def draw_square(x,y):
    t.up()
    t.goto(x,y)
    t.down
    t.begin_fill()
    t.setheading(random.randint(0,360))
    for i in range(4):
        t.forward(size)
        t.left(90)
    t.end_fill()

def size_up():
    global size
    size = size + 10

def size_down():
    global size
    if size >= 10:
        size = size - 10

def draw_ondrag(x,y):
    t.ondrag(None)
    t.goto(x,y)
    t.dot(size)
    t.ondrag(draw_ondrag)
    t.up()

size = 50
color = ['red', 'pink', 'lightblue','greenyellow', 'black', ]

t.bgcolor('ivory')
t.speed(0)
t.onscreenclick(draw_ondrag)
# t.onscreenclick(draw_dot, 1)
# t.onscreenclick(draw_triangle, 2)
# t.onscreenclick(draw_square,3)
t.onkeypress(rand_color, 'space')
t.onkeypress(size_up,'Up')
t.onkeypress(size_down,'Down')
t.listen()
t.mainloop()


