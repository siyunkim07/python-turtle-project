import turtle as t
import random



def random_color():
    t.colormode(255)
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b

rand_position_x = 0
rand_position_y = 0

def petal(size,angle):
    t.up()
    t.goto(rand_position_x,rand_position_y)
    for j in range(2):
        t.circle(size,angle)
        t.left(180 - angle)

def drawflower(num,size,angle):
    t.color(random_color())
    t.begin_fill()
    for i in range(num):
        petal(size,angle)
        t.left(360 / num)
    t.end_fill()

    t.goto(rand_position_x + 3,rand_position_y -30)
    t.color('yellow')
    t.begin_fill()
    t.circle(30)
    t.end_fill()        
t.speed(0)
t.hideturtle()
t.bgcolor('ivory')


for i in range(5):
    num = random.randint(4,10)
    size = random.randint(90,150)
    angle = random.randint(60,130)
    rand_position_x = random.randint(-300,300)
    rand_position_y = random.randint(-300,300)
    drawflower(num,size,angle)



t.mainloop()