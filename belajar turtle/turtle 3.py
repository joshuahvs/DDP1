import turtle

nicki = turtle.Turtle()

nicki.getscreen().bgcolor("#994444")

def star(turtle, size):
    if size<= 10:
        return
    else:
        for i in range(5):
            turtle.forward(size)
            star(turtle, size /3)
            turtle.left(216)
star(nicki, 120)

turtle.done()