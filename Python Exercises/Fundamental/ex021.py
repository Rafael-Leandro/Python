'''Create a program that reads a person's full name and displays:
- The name in all upper and lower case letters.
- How many letters in total (not considering spaces).
- How many letters are in the first name.'''

name = str(input('Write your full name: ')).strip()
print('Analysing your name...')
print('Your name in uppercase is {}'.format(name.upper()))
print('Your name in lowercase is {}'.format(name.lower()))
print('Your name has a total of {} letters'.format(len(name) - name.count(' ')))
print('Your first name has a total of {} letters'.format(name.find(' ')))

# Another way to count how many letters your first name have
separate = name.split()
print('Your first name is {} and it has {} letters'.format(separate[0], len(separate[0])))
