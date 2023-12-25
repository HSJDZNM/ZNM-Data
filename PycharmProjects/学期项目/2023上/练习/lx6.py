import turtle

colors = ['red', 'purple', 'blue', 'green', 'yellow', 'orange']
t = turtle.Pen()
turtle.bgcolor('black')
turtle.speed(1000000)
for x in range(10000000000):
    t.pencolor(colors[x % 6])
    t.width(x / 100 + 1)
    t.forward(x)
    t.left(59)