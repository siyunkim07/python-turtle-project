import turtle as t 
import time 
import random 
import winsound 

t.bgcolor('lavender')
t.up()
t.speed(0)
t.goto(0,200)
t.write('turtle racing', False, 'center',("",35))

# 경기장 그리기

t.goto(-400, 170)
t.down()
t.color('lightpink')
t.begin_fill()


for i in range(2):
    t.forward(800)
    t.right(90)
    t.forward(400)
    t.right(90)

t.end_fill()

# 결승선 그리기
t.color('black')
t.up()
t.goto(330, 200)
t.down()
t.goto(330,-250)

# 경기에 참여할 거북이 숫자입력
num_turtle = int(t.textinput('터틀 수를 입력', '몇 마리의 거북이를 레이싱에 참여시킬건가요?\n (최소 2마리, 최대 7마리)'))


# 선수들 좌표, 색상 정의 
top_ycor = 170
start_ycor = []
space = int(400 / num_turtle)
for i in range(num_turtle):
    start_ycor.append(top_ycor - (space * i) - (space / 2))
print(start_ycor)

color_list = ['hotpink', 'white', 'red', 'green', 'yellow', 'purple', 'blue']

# 레이스 라인 그리기

for i in range(num_turtle - 1):
    t.up()
    t.goto(-400, start_ycor[i] - (space / 2))
    t.color('white')
    t.down()
    t.goto(400, start_ycor[i] - (space / 2))


# 터틀 선수들 생성
turtles = []
for i in range(num_turtle):
    new_turtle = t.Turtle()
    new_turtle.color(color_list[i])
    new_turtle.up()
    new_turtle.shape('turtle')
    new_turtle.goto(-370, start_ycor[i])
    new_turtle.write(i)
    new_turtle.goto(-350, start_ycor[i])
    turtles.append(new_turtle)

# # 1등 터틀 맞추기

user_choice = int(t.textinput('터틀 레이스','몇 번 거북이가 이길까요?'))
t.up()
t.goto(0, -200)
t.color('black')
t.write(f'{user_choice}번 터틀을 응원하셨습니다.', False, 'center', ("", 30))
t.ht()

# 경기시작알림
winsound.Beep(523, 300)
time.sleep(0.3)

game_over = False

while not game_over:
    for i in turtles:
        rand_speed = random.randint(1, 10)
        i.forward(rand_speed)
        if i.xcor() > 330:
            game_over = True
who = 0
max = 0
for i in range(num_turtle):
    if turtles[i].xcor() > max:
        max = turtles[i].xcor()
        who = i
    

# 결과 출력 
t.goto(0,0)
if user_choice == who:
    t.write('응원하신 거북이가 1등했습니다.', False, 'center',('',30))
else:
    t.write(f'아깝습니다. {who}번 거북이가 1등했습니다.', False, 'center',('',30))
    

t.mainloop()