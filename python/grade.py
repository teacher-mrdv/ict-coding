# IB grades https://www.clastify.com/blog/ib-computer-science-grade-boundaries
score = int(input('Enter your IB CS HL final score (%) = '))
grade = 0
if score < 15:
    grade = 1
elif score < 30:
    grade = 2
elif score < 41:
    grade = 3
elif score < 52:
    grade = 4
elif score < 62:
    grade = 5
elif score < 73:
    grade = 6
else: # also --> elif score > 72 and score <= 100
    grade = 7

print( 'A final percentage score of %d is a %d grade out of 7 for IB HL CompSci.' % (score, grade) )
