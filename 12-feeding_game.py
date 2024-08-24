import turtle as t
import random

def rand_pos():
    x_cor = random.randint(-350, 350)
    y_cor = random.randint(-350, 350)
    return x_cor, y_cor
def turn_left():
    player.left(30)
def turn_right():
    player.right(30)


t.setup(800,800) # 창크기를 설정

t.bgcolor('skyblue')
t.up()
t.ht()

player_speed = 5
score = 0
game_over = False

t.goto(0, 350)
t.write(f'score: {score}', False, 'center', ("",20))


# player turtle 생성

player = t.Turtle()
player.shape('turtle')
player.shapesize(2)
player.up()
player.color('lavender')
player.speed(0)

# 먹이 생성

food = t.Turtle()
food.ht()
food.shape('triangle')
food.up()
food.color('darkgreen')
food.speed(0)
food.setheading(90)
food.goto(rand_pos())
food.st() 

# 독초  생성
p_herbs = t.Turtle()
p_herbs.ht()
p_herbs.shape('triangle')
p_herbs.up()
p_herbs.color('red')
p_herbs.speed(0)
p_herbs.setheading(90)
p_herbs.goto(rand_pos())
p_herbs.st() 



t.onkeypress(turn_left, "Left")
t.onkeypress(turn_right, "Right")
t.listen()

while not game_over:
    player.fd(player_speed)
    if player.xcor() > 360 or player.xcor() < -360 or player.ycor() > 360 or player.ycor() < -360:
        player.right(180)
    if player.distance(food) < 20:
        food.goto(rand_pos())
        p_herbs.goto(rand_pos())
        player_speed += 1
        score += 1
        t.clear()
        t.write(f'score: {score}', False, 'center', ("",20))     
    if player.distance(p_herbs) < 20:
        game_over = True
t.goto(0, 0)
t.color('red')
t.write(f'GAME OVER', False, 'center', ("",50))     




t.mainloop()
