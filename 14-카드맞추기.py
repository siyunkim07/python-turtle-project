import turtle as t
import random
import time

def score_update(m):
    score_pen.clear()
    score_pen.write(f'{m} {score}점/{attempt}번 시도',False,'center',('',15))


def find_card(x,y):
    min_idx = 0
    min_dis = 100

    for i in range(16):
        distance = turtles[i].distance(x, y)
        if distance < min_dis:
            min_dis = distance
            min_idx = i
    return min_idx



def result(m):
    t.goto(0, -60)
    t.write(m, False, 'center', ("",30,'bold'))

def play(x, y):
    global click_num
    global first_pick
    global second_pick
    global attempt
    global score


    if attempt == 12:
        result('GAME OVER')
    else:
        click_num += 1

        # 클릭한 이미지 찾기 
        card_idx = find_card(x,y) # == 함수를 정의
        turtles[card_idx].shape(img_list[card_idx])

    # 매 2회 클릭시 마다 정답 check
    if click_num ==1:
        first_pick = card_idx
    elif click_num ==2:
        second_pick = card_idx
        click_num = 0
        attempt += 1
        if img_list[first_pick] == img_list[second_pick]:
            # 정답
            score += 1
            score_update('정답')
            if score == 8:
                result('성공')
        else:
            # 오답
            score_update('오답')
            turtles[first_pick].shape(default_img)
            turtles[second_pick].shape(default_img)
t.bgcolor('pink')
t.setup(700, 700)
t.ht()
t.up()
t.goto(0, 280)
t.write('카드 매칭 게임', False, 'center', ("", 30, 'bold'))


# 점수 pen 객체 생성

score_pen = t.Turtle()
score_pen.up()
score_pen.ht()
score_pen.goto(9, 230)

# 카드의 turtle 객체들을 생성

turtles = []
pos_x = [-210, -70, 70, 210]
pos_y = [-250, -110, 30, 170]

for x in range(4):
    for y in range(4):
        new_turtle = t.Turtle()
        new_turtle.up()
        new_turtle.color('pink')
        new_turtle.speed(0)
        new_turtle.goto(pos_x[x], pos_y[y])
        turtles.append(new_turtle)


default_img = "images/default_img.gif"
t.addshape(default_img)
img_list = []
for i in range(8):
    img = f'images/img{i}.gif'
    t.addshape(img)
    img_list.append(img)
    img_list.append(img)

# shuffle() : 정해져 있는 데이터를 무작위로 썪는다.
random.shuffle(img_list)
for i in range(16):
    turtles[i].shape(img_list[i])


time.sleep(3)

for i in range(16):
    turtles[i].shape(default_img)


# 전역변수 설정 
click_num = 0 # 클릭 횟수 (매 2회 클릭마다 정답을 체크하기 위해서)
score = 0
attempt = 0 # 시도한 횟수
first_pick = "" # 첫번째 클릭한 이미지
second_pick = "" #두번째 클릭한 이미지

t.onscreenclick(play)

t.mainloop()