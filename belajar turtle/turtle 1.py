import turtle

bob = turtle.Turtle()

# bob.forward(100)
# bob.left(45)
# bob.forward(100)
# bob.right(100)
# bob.forward(100)

bob.color("red", "orange")
# making square

bob.begin_fill() # untuk fill color
bob.forward(100)
bob.left(90)
bob.forward(100)
bob.left(90)
bob.forward(100)
bob.left(90)
bob.forward(100)
bob.end_fill()

# change location or position without drawing line
bob.penup()
bob.forward(100)
bob.pendown()


bob.forward(100)
bob.left(90)
bob.forward(100)
bob.left(90)
bob.forward(100)
bob.left(90)
bob.forward(100)


turtle.done()