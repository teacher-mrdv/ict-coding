# conditionals -- bouncer
name = input('Enter your name: ')
age  = int(input( 'How young are you? '))
print( name, end = '' )

if age >= 18:
    print(', you are welcome to the club')
else:
    print(", you should come back when you're 18" )
    
if age < 21:
    print('You can not drink alcohol, though, ' + name + ' :(')
else:
    print("Don't drink and drive, " + name)