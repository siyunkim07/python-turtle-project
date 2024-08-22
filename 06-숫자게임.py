import turtle as t
import time 
import random

t.bgcolor('pink')
t.hideturtle()
t.up()
play = True
while play: 
    num_times = int(t.numinput('숫자 기억 게임', '몇개의 숫자를 기억하시겠습니까? : '))
    t.write('숫자 기억하기 게임을 시작합니다!!', False, 'center',("",30))
    time.sleep(3)
    t.clear()
    num = ""
    for i in range(num_times):
        rand_num = random.randint(1,20)
        t.write(rand_num, False, 'center',("",70))
        num += str(rand_num) + " "
        time.sleep(1)
        t.clear()

    user_input = t.textinput('숫자 기억 게임','기억한 숫자를 입력하세요. (공백) : ' )
    t.goto(0,0)
    if num.strip()== user_input.strip():
        t.write('정답입니다!', False, 'center',("",30))
    else:    
        t.write('오답입니다!', False, 'center',("",30))
        t.goto(0,-50)
        t.write(f'정답은 "{num}" 입니다.', False, 'center',("",30))
        t.goto(0,-100)
        t.write(f'입력한 숫자는 "{user_input}" 입니다.', False, 'center',("",30))

    time.sleep(2)       
    t.clear()
    go = t.textinput('숫자 기억 게임', '게임을 계속 하시겠습니까?(y or n)')
    if go != 'y':
        play = False


t.mainloop()