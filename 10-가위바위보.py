import turtle as t 
import random

def result_print(user_c, com_c):
    global user_score, com_score
    t.clear()
    t.goto(0, -250)
    if user_c == com_c:
        t.write('무승부', False,'center',('',50))
    elif winning_list[user_c] == com_c:
        user_score += 1
        user_pen.clear()
        user_pen.write(user_score, False, 'center', ('',50))
        t.write('승', False, 'center', ('',50))
    else:
        com_score += 1
        com_pen.clear()
        user_pen.write(com_score,False,'center'('', 50))
        t.write('패', False,'center',("",50))


def com_choice():
    rand_choice = random.randint(0, 2)
    com.shape(images[rand_choice])
    return com_list[rand_choice]


def rock(x, y):
    user.shape(rock_gif)
    com = com_choice()
    result_print('rock', com)
def scissors(x, y):
    user.shape(rock_gif)
    com = com_choice()
    result_print('scissors', com)
def paper(x, y):
    user.shape(rock_gif)
    com = com_choice()
    result_print('scissors', com)
t.bgcolor('lavender')
t.title('가위바위보 게임')

t.up()

rock_gif = './images/rock.gif'
scissors_gif = './images/scissors/gif'
paper_gif = './images/paper/gif'
# 이미지 파일을 정의
t.addshape(rock_gif)
t.addshape(scissors_gif)
t.addshape(paper_gif)

t.shape(rock_gif)
# shape을 추가
images = [rock_gif, scissors_gif, paper_gif]
com_list = ['rock', 'scissors', 'paper']
winning_list = {'rock' : 'scissors', 'scissors' : 'paper', 'paper' : 'rock'}
# 전역변수를 설정
user_score = 0
com_score = 0


# 나의 이미지 선택
user = t.Turtle() # 새로운 turtle 객체를 생성한다.
user.speed(0)
user.goto(-150, 200)
user.write('나의 선택', False, 'center', ('', 30))
user.goto(-150, -50)
user.shape(images[0])


# 컴퓨터 이미지 선택
com = t.Turtle() # 새로운 turtle 객체를 생성한다.
com.speed(0)
com.goto(150, 200)
com.write('컴퓨터의 선택', False, 'center', ('', 30))
com.goto(150, -50)
com.shape(images[0])


# user의 점수판

user_pen = t.Turtle()
user_pen.ht()
user_pen.up()
user_pen.goto(-150, 100)
user_pen.write(user_score, False, 'center', ("", 50))

# com의 점수판

com_pen = t.Turtle()
com_pen.ht()
com_pen.up()
com_pen.goto(150, 100)
com_pen.write(com_score, False, 'center', ("", 50))

t.onscreenclick(rock, 1)
t.onscreenclick(scissors, 2)
t.onscreenclick(paper, 3)

t.mainloop()