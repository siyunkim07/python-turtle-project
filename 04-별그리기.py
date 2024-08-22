import turtle as t 
import random

def draw_star():
    t.color(random.choice(color))
    t.begin_fill()
    star_size = random.randint(5, 15)
    for i in range(5):
        t.forward(star_size)
        t.left(72)
        t.forward(star_size)
        t.right(144)
    t.up()    
    t.goto(random.randint(-300, 300), random.randint(-300,300))        
    t.down()
    for i in range(3):
        t.forward(star_size)
        t.left(120)
    t.hideturtle()
        

    t.end_fill()    



color = ('red', 'orange', 'blue', 'lightblue', 'white', 'indigo', 'yellow')

t.bgcolor('black')
t.speed(0)

for i in range(20):
    t.up()
    t.goto(random.randint(-300, 300), random.randint(-300,300))
    t.down()

    # t.dot(5, random.choice(color))
    draw_star()

t.mainloop()