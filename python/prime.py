N = int(input( "Enter N "))
I = 2
PRIME = True
while I < N:
    if N % I == 0:
        PRIME = False
        break
    I = I + 1 
if PRIME == True:
    print( "Prime" )
else:
    print("Not a prime")