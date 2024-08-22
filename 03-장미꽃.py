import turtle as t

t.bgcolor('black')
t.color('red')
# turtle이 그림을 그리는 속도 1 ~ 10, 0 = 제일 빠른 속도
t.speed(0)

for i in range(200):
    # 선의 굵기 지정
    t.pensize(i/50)
    t.forward(i)
    t.left(65)

# pen이 끝나는 지점에서 줄기 그리기
t.color('green')
t.setheading(270)

# 줄기는 아래로 내려갈 수록 가늘어진다
for i in range(50):
    t.pensize(25-i/2)
    t.forward(i/4)

# 잎 그리기 

t.color('yellowgreen')
t.setheading(60)
for i in range(100):
    t.pensize(100 - i)
    t.forward(i/10)

t.hideturtle()
t.mainloop()