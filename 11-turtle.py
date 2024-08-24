import turtle as t

t.bgcolor('lavender')
t.shape('turtle')

t.up()
t.goto(200,200)
t.write('첫번째 거북이', False, 'center', ('', 30))

t1 = t.Turtle()
t1.color('red')
t1.shape('turtle')
t1.write('두번째 거북이', False, 'center', ('', 30))

t2 = t.Turtle()
t2.color('blue')
t2.shape('turtle')
t2.up()
t2.goto(-200,200)
t2.write('세번째 거북이', False, 'center', ('', 30))


t.clear()
t1.clear()
t2.clear()

t.mainloop()