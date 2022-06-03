# Output
print("Welcome to our first Python lesson")

# Input
name = input('What is your name? ')
age = int(input("What is your age? "))
height = float(input("What is your height "))

# Output including what was input
print( 'Hello ' + name )
#print( 'You said your age is ' + age + ' and your height is ' + height)
print( 'You said your age is ' + str(age) + ' and your height is ' + str(height) )
if age > 18:
    print('You are old!')
    print('You will die soon. Unfortunately. Oh.')
if name == "Robert":
    print("May I call you Bob?")