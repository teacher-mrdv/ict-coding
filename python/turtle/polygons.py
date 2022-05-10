import turtle
bob = turtle.Turtle() # my turtle's name is bob (skip it in exam)
bob.shape("turtle")
bob.color('green')
bob.left(90) # we start with the turtle facing north/up

bob.pendown()

# sides  = int(input("Enter # of sides: "))
# length = int(input("Enter length: "))

sides = 8
length= 40

for s in range(sides):
    bob.forward(length)
    bob.right(360/sides)
    
turtle.done()