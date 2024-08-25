''' Write a program that reads a person's full name, then displays the first name and last name separately.
Ex: Ana Maria de Souza 
• First name = Ana 
• Last name = Souza '''

n = str(input('Write your full name: ')).strip()
name = n.split()
print('Nice to meet you!')
print('Your first name is {}.'.format(name[0]))
print('Your last name is {}.'.format(name[len(name)-1]))
