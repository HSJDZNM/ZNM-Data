import turtle

t = turtle.Pen()
t.forward(100)
t.left(90)
t.forward(200)
t.left(90)
t.forward(100)
t.left(90)
t.forward(200)

t.clear()

t.left(90)
t.forward(100)
t.left(120)
t.forward(100)
t.left(120)
t.forward(100)

t.clear()

t.left(30)
t.up()
t.forward(20)
t.down()
t.forward(100)
t.up()
t.forward(20)

for i in range(3):
    t.left(90)
    t.forward(20)
    t.down()
    t.forward(100)
    t.up()
    t.forward(20)



turtle.exitonclick()