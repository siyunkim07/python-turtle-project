from turtle import Turtle, Screen
import time
import random

def up():
    if snakes[0].heading() != 270:
        snakes[0].setheading(90)
def down():
    if snakes[0].heading() != 90:
        snakes[0].setheading(270)
def left():
    if snakes[0].heading() != 0:
        snakes[0].setheading(180)
def right():
    if snakes[0].heading() != 180:
        snakes[0].setheading(0)

def rand_pos():
    rand_x = random.randint(-250, 250)
    rand_y = random.randint(-250, 250)
    return rand_x, rand_y

def create_snake(pos):
    snake_body = Turtle()
    snake_body.shape('square')
    snake_body.color('orangered')
    snake_body.up()
    snake_body.goto(pos)
    snakes.append(snake_body)

def score_update():
    global score
    score += 1
    score_pen.clear()
    score_pen.write(f'점수 {score}', font=("", 15, "bold"))


screen = Screen()

screen.setup(600, 600)
screen.bgcolor('khaki')
screen.title('SNAKE GAME')
screen.tracer(0) # 뱀 이동 시 깜빡이지 않게 하기 위해서 screen.update()와 함께 사용.

# snake 변수값들
start_pos = [(0, 0), (-20, 0), (-40, 0)]
snakes = []
score = 0

# 먹이를 하나 먹을 때 마다 몸통을 하나씩 추가
for pos in start_pos:
    create_snake(pos)

# 먹이 만들기
food = Turtle()
food.shape('circle')
food.color('snow')
food.up()
food.speed(0)
food.goto(rand_pos())

# 점수 표시
score_pen = Turtle()
score_pen.ht()
score_pen.up()
score_pen.goto(-270, 250)
score_pen.write(f'점수 : {score}', font ={"", 16, 'bold'})

screen.listen()
screen.onkeypress(up, 'Up')
screen.onkeypress(down, 'Down')
screen.onkeypress(left, 'Left')
screen.onkeypress(right, 'Right')


game_on = True
while game_on:
    screen.update() # 꼬리가 모두 이동한 다음에 화면을 update함
    time.sleep(0.1)
    for i in range(len(snakes) -1, 0, -1):
        snakes[i].goto(snakes[i-1].pos())

    snakes[0].forward(10)
    
    # snake이 먹이를 먹었을 때 

    if snakes[0].distance(food) < 15:
        score_update()
        food.goto(rand_pos())     
        create_snake(snakes[-1].pos())

    # snake의 머리가 벽에 닿으면 게임 종료.
    if snakes[0].xcor() > 280 or snakes[0].xcor() < -280 or snakes[0].ycor() > 280 or snakes[0].ycor() < -280:
        game_on = False
        score_pen.goto(0, 0)
        score_pen.write('Game Over',False,'center',("", 30, 'bold'))


    # snake의 머리가 자기 몸에 닿으면 게임 종료..
    for body in snakes[1:]:
        if snakes[0].distance(body) < 5:
            game_on = False
            score_pen.goto(0, 0)
            score_pen.write('Game over', False, 'center',("", 30, "bold"))
    

screen.mainloop()