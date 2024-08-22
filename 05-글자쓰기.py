import turtle as t
import time

t.bgcolor('pink')
t.color('red')
t.hideturtle()
t.up()
for i in range(3,0,-1):
    t.up()
    t.goto(0,0)
    t.write(str(i), True, 'center', ("", 100))
    time.sleep(1)
    t.clear()
t.down()
t.write('RONALDO',True,'center',("",100))
t.mainloop()
