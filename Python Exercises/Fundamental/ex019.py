'''A teacher wants to draw one of his four students to erase the blackboard. Make a program that helps him, reading the students' names and writing the name of the chosen one on the screen'''
import random
n1 = str(input('First student: '))
n2 = str(input('Second student: '))
n3 = str(input('Third student: '))
n4 = str(input('Fourth student: '))
list = [n1, n2, n3, n4]
ChosenOne = random.choice(list)
print('The chosen one student was {}'.format(ChosenOne))
