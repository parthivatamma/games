A = 4
B = 3
C = 2
D = 1
F = 0

gpa = 0

amountofgrades = int(input('How many grades do you want to calculate a GPA for? '))
print(amountofgrades)
#aog1 = amountofgrades - 1 
for x in range (0,amountofgrades):
    gpaval = input('Enter your grade(Choose between A, B, C, D, F):')
    if gpaval == A:
        gpa = gpa + A
    elif gpaval == B:
        gpa = gpa + B
    elif gpaval == C:
        gpa = gpa + C
    elif gpaval == D:
        gpa = gpa + D
    elif gpaval == F:
        gpa = gpa
    else:
        print('Please insert a number.')
finalgpa = gpa/amountofgrades