import turtle as t

t.speed(0)
t.bgcolor("black")
t.color("aqua")
t.hideturtle()
for i in range(360):
    t.circle(i - 5)
    t.left(5)
t.left(90)
