## Pr 1 
n = input('Enter a number ')
power = 1
for i in range(n + 1):
    print power
    power = 2*power



## Pr 2 
n = input('Enter a number ')
for i in range(1, n+1):
    if i % 2 != 0:
        print i,

## Pr 3 
n = input('Enter a number ')
for i in range(1, n+1, 2):
    print i,

n = input('Enter a number ')
for i in range(1, n+1):
    if i % 2 !=0 and i % 3 !=0:
        print i,

## Pr 4 
c=0
for i in range(1, 1000000):
    if i % 2 !=0 and i % 3 !=0 and i % 5 !=0 and i % 7 !=0:
        c=c+1

print c


## Pr 5 
a = input('Enter value for a ')
b = input('Enter value for b ')
c = input('Enter value for c ')

if a + b > c and a + c > b and b + c > a:
    print ' Three sides make a triangle '

else:
    print ' Three sides fail to make a triangle '


## Pr 6  
n = input('Enter the number of terms ')
t = 0
for i in range(1, n+1):
    t = t + i
    print t,



## Pr 7

import math

t = 0
for i in range(1, n+1):
    t = t + i
    s = int( math.sqrt( t ) )
    if s * s == t:
        print t,
