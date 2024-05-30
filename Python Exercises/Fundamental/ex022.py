''' Write a program that reads a number from 0 to 9999 and displays each of them in separated digits on the screen
Ex: 
Enter a number: 1834
Thousands: 1 • Hundreds: 8 • Dozens: 3 • Unit: 4 '''

num = int(input('Write the number: '))
unit = num // 1 % 10
dozens = num // 10 % 10
hundreds = num // 100 % 10
thousands = num // 1000 % 10
print('Analysing the number {}'.format(num))
print('Unit: {}'.format(unit))
print('Dozens: {}'.format(dozens))
print('Hundreds: {}'.format(hundreds))
print('Thousands: {}'.format(thousands))
