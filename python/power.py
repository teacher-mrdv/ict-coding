def positive_power(base, exponent):
    result = 1
    counter = exponent
    print(str(base) + "^" + str(exponent) )
    while counter > 0:
        #print( "result=" + str(result) + 'counter=' + str(counter) )
        result = result * base
        counter = counter - 1
    #print( "result=" + str(result) + 'counter=' + str(counter) )
    return result

def power(base, exponent):
    if exponent < 0:
        return 1/positive_power(base, -exponent)
    else:
        return positive_power(base, exponent)

print( power(2, 8) )
print( power(2, 0) )
print( power(2, -2) )