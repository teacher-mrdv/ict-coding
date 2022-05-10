import turtle         # allows us to use the turtle and turtle commands/functions
bob = turtle.Turtle() # my turtle's name is bob (we skip the name and the dot in the exam)
bob.shape("turtle")   # makes the turtle look like a turtle, useless otherwise
bob.color("green")    # sets the turtle --and therefore drawing colour-- to green.
bob.left(90)          # we start with the turtle facing north/up

bob.pendown()

# long way
# bob.forward(50)
# bob.right(90)
# bob.forward(50)
# bob.right(90)
# bob.forward(50)
# bob.right(90)
# bob.forward(50)
# bob.right(90)

# bob.forward(50)
# bob.right(90)
# bob.penup()
# bob.forward(50)
# bob.right(90)
# bob.pendown()
# bob.forward(50)
# bob.right(90)
# #bob.penup()
# bob.forward(50)
# bob.right(90)


for times in range(4): # equivalent in exam: repeat 4
    bob.forward(50)
    bob.left(90)
    

turtle.done()
