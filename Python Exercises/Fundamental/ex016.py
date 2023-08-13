'''
Write a program that reads any real number from the keyboard and displays its integer portion on the screen.
Example: The integer part of the number 6.587 is going to be the number 6.
'''
import math
num = float(input('Write a number: '))
print('The number that was wrote is {} and its integer part is {}'.format(num, math.trunc(num)))

'''
There are other ways to achieve the same results

from math import trunc
num = float(input('Write a number: '))
print('The number that was wrote is {} and its integer part is {}'.format(num, trunc(num)))

or

num = float(input('Write a number: '))
print('The number that was wrote is {} and its integer part is {}'.format(num, int(num)))
'''
