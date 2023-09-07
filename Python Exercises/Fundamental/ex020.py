'''The same teacher from ex019.py wants to raffle the order in which students' work will be presented. Make a program that reads the names of the four students and shows the order drawn'''
import random
n1 = str(input('First student: '))
n2 = str(input('Second student: '))
n3 = str(input('Third student: '))
n4 = str(input('Fourth student: '))
list = [n1, n2, n3, n4]
random.shuffle(list)
print('The presentation order will be ')
print(list)
