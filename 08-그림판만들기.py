import turtle as t
def green_color():
    t.color("greenyellow")

def pink_color():
    t.color('lightpink')

def blue_color():
    t.color('blue')

def white_color():
    t.color('white')

def pen_up():
    t.up()

def pen_down():
    t.down()


def begin_fill():
    t.begin_fill()

def end_fill():
    t.end_fill()

    
def draw_ondrag(x,y):
    t.ondrag(None)
    t.goto(x,y)
    t.ondrag(draw_ondrag)


t.speed(0)
t.bgcolor('lightblue')
t.pensize(3)


# turtle event 처리하는 방법

t.onscreenclick(draw_ondrag)
t.onkeypress(green_color,'g')
t.onkeypress(pink_color,'p')
t.onkeypress(blue_color,'b')
t.onkeypress(white_color,'w')
t.onkeypress(pen_up,'Up')
t.onkeypress(pen_down,'Down')
t.onkeypress(begin_fill,'Left')
t.onkeypress(end_fill,'Right')

t.listen()

t.mainloop()