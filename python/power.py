def power(base, exponent):
    result = 1
    counter = exponent
    while counter > 0:
        result = result * base
        counter = counter - 1
    return result

print( power(2, 8) )