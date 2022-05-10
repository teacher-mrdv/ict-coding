import turtle         # allows us to use the turtle and turtle commands/functions
bob = turtle.Turtle() # my turtle's name is bob (we skip the name and the dot in the exam)
bob.shape("turtle")   # makes the turtle look like a turtle, useless otherwise
bob.color("green")    # sets the turtle --and therefore drawing colour-- to green.
bob.left(90)          # we start with the turtle facing north/up

bob.pendown()

# bob.forward(100)
# bob.right(180-45)
# bob.forward(141.4)
# bob.right(180-45)
# bob.forward(100)

# Right angle
bob.forward(100)
bob.left(180-45)
bob.forward(141.4)
bob.left(180-45)
bob.forward(100)
wait = input("Press [Return] / [Enter] to continue")

# Equilateral
bob.reset() # clear the screen and reset the turtle to starting position and facing left/east
for sides in range(3):
  bob.left(120)
  bob.forward(175)

turtle.done()
