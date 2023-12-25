import turtle
t = turtle.Turtle()

t.forward(100)
t.left(90)
t.forward(50)
t.left(90)
t.forward(100)
t.left(90)
t.forward(50)

for _ in range(3):
    t.forward(100)
    t.left(120)
turtle.exitonclick()
