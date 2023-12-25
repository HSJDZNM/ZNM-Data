import turtle
a=turtle.Pen()
b=turtle.Pen()
c=turtle.Pen()
d=turtle.Pen()

canvas = turtle.Screen()
t = turtle.Turtle()

a.forward(100)
a.left(90)
a.forward(50)
a.right(90)
a.forward(50)

b.forward(110)
b.left(90)
b.forward(25)
b.right(90)
b.forward(30)

c.forward(110)
c.right(90)
c.forward(25)
c.left(90)
c.forward(30)

d.forward(100)
d.right(90)
d.forward(50)
d.left(90)
d.forward(50)

canvas.exitonclick()
