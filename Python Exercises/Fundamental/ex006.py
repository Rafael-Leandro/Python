'''Write a program that reads a number and displays its double, its triple and its square root'''
num = int(input('Write a number: '))
double = num * 2
triple = num * 3
SquareRoot = num ** (1/2)
print('The double of {} is {}.'.format(num, double))
print('The triple of {} is {}.'.format(num, triple))
print('The square root of {} is equal to {:.2f}.'.format(num, SquareRoot))

# We can achieve the same results without the use of variables
print('The double of {} is {}.'.format(num, (num * 2)))
print('The triple of {} is {}.'.format(num, (num * 3)))
print('The square root of {} is equal to {:.2f}.'.format(num, pow(num, (1/2))))
