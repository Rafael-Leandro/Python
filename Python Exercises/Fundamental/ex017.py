'''Write a program that reads the length of the opposite and adjacent sides of a right triangle and then calculate it and show the length of the hypotenuse'''

import math 
OppositeSide = float(input('Length of the opposite side: '))
AdjacentSide = float(input('Length of the adjacent side: '))
Hypo = math.hypot(OppositeSide, AdjacentSide)
print('The hypotenuse length is going to be {:.2f}'.format(Hypo))

'''
Another way to solve this problem without use the math module

OppositeSide = float(input('Length of the opposite side: '))
AdjacentSide = float(input('Length of the adjacent side: '))
Hypo = (OppositeSide ** 2 + AdjacentSide ** 2) ** (1/2)
print('The hypotenuse length is going to be {:.2f}'.format(Hypo))
'''
