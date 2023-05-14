'''Write a program that reads an integer number and displays its successor and predecessor on the screen'''
num = int(input('Write a number: '))
pre = num - 1
suc = num + 1
print('Analyzing the value {}, its predecessor is {} and its successor is {}'.format(num, pre, suc))

# Displaying the same result without the use of variables
num = int(input('Write a number: '))
print('Analyzing the value {}, its predecessor is {} and its successor is {}'.format(num, (num - 1), (num + 1)))
'''
The less you use variables, the more memory you will save on your device 
but if you had to use the predecessor and successor variables further in the code it would be necessary to write them.
'''
