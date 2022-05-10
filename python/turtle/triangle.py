import turtle
bob = turtle.Turtle() # my turtle's name is bob (skip it in exam)
bob.shape("turtle")
bob.color('green')
bob.left(90) # we start with the turtle facing north/up

bob.pendown()

# bob.forward(100)
# bob.right(180-45)
# bob.forward(141.4)
# bob.right(180-45)
# bob.forward(100)

bob.forward(100)
bob.left(180-45)
bob.forward(141.4)
bob.left(180-45)
bob.forward(100)

turtle.done()