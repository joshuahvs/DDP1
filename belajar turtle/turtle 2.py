import turtle

nicki = turtle.Turtle()
nicki.speed(10)

nicki.color("red", "yellow")

nicki.begin_fill()
for i in range(100):
    nicki.forward(300)
    nicki.left(174)
nicki.end_fill()
    

turtle.done()