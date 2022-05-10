import turtle
bob = turtle.Turtle() # my turtle's name is bob (skip it in exam)
bob.shape("turtle")
bob.color('green')

bob.pendown()
step = 0.1
for i in range(360):
    bob.forward(step)
    bob.left(10)
    step = step + 0.1

turtle.done()