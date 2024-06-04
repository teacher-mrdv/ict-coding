name = input('Enter your name ')
times= int(input( 'How many times? '))
print( list(range(times) ) )
#for i in range(times):
#    print(str(i) + ": " + name)

a = 0
while a < times:
    print(name)
    a = a + 1
