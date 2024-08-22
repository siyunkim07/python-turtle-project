# turtle 라이브러리를 import 한다.
import turtle as t

# turtle의 모양 지정
t.shape('turtle') # triangle, square, arrow, circle

# 화면의 바탕색을 지정
t.bgcolor('light green')

# 선의 색을 지정
t.color('blue')

# # 선 그리기

# # 앞으로 가기
# t.forward(100)
# # 회전(반시계방향)
# t.left(90)

# t.color('red')
# t.forward(100)
# t.left(90)


# t.color('white')
# t.forward(100)
 
# t.left(90)
polgon = int(t.numinput('다각형 그리기', '몇각형을 그릴까요?'))

for i in range(polgon):
    t.forward(100)
    t.left(360 / polgon)

t.mainloop()