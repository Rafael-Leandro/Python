'''Write a program that reads a person's full name and tells if they have "SILVA" in their name'''
name = str(input('What is your full name? ')).strip()
print('Does your name have Silva? {}'.format('silva' in name.lower()))
