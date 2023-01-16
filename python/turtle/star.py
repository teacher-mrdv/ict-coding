import turtle
bob = turtle.Turtle() # my turtle's name is bob (skip it in exam)
#bob.mode('logo') # face north by def.
bob.shape("turtle")
bob.color('green')
# NOTE that the Python turtle starts facing left
bob.pendown()

for i in range(5):
    bob.right(144)
    bob.forward(100)
    
turtle.done()
