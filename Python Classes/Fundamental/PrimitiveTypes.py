#Introduction
#In this class we are going to talk about the Python primitive types.

'''
Integer Type (int)
The integer type is a type composed of integer numeric characters (digits).

It is a type used for a number that can be written without a decimal component, with or without a sign, which means: being positive or negative.

For example, 21, 4, 0, and −2048 are integer numbers, while 9.75, 1/2, 1.5 are not.

Examples:
'''
n1 = int(input('Write your age: '))
n2 = int(input('Write your birth year: '))
print('You are {} years old and you were born in {}.'.format(n1, n2))
print(type(n1))
print(type(n2))

'''
Floating Point or Decimal (float)
It is a type composed of numeric decimal characters (digits).

The famous floating point is a type used for rational numbers (numbers that can be represented by a fraction) informally known as "broken numbers".

Examples:
'''
n3 = float(input('Write your height: '))
n4 = float(input('Write your weight: '))
print('You are {} tall and weigh {} kg.'.format(n3, n4))
print(type(n3))
print(type(n4))

'''
String (str)
It is a set of characters arranged in a certain order, generally used to represent words, phrases or texts.

Examples:
'''
name = str(input('Write your name: '))
profession = str(input('Write your profession: '))
print('Your name is {} and you work as a {}.'.format(name, profession))
print(type(name))
print(type(profession))

'''
Boolean (bool)
Logical data type that can take only two values: False or True.

In computational logic, these values can be considered as 0 or 1.

Examples:
'''
lightsOn = True
lightsOff = False
print(type(lightsOn))
print(type(lightsOff))

'''
Lists (list)
A very important type of data that is used a lot in the Python developer's day-to-day life!

Lists groups up a set of varied elements, and may contain: integers, floats, strings, other lists and other types.

They are defined using square brackets to delimit the list and commas to separate the elements, see some examples below:
'''
students = ['Julia', 'Rafael', 'Ana', 'Chris']
grades = [10, 8.5, 7.8, 8.0]
print('The student {} received the grade {} in math.'.format(students[2], grades[1]))
print(type(students))
print(type(grades))

'''
Tuples (tuple)
Like List, Tuple is a type that groups up a set of elements as well.

However, its definition is different: we use parentheses and it is also separated by a comma.

The difference with List is that Tuples are immutable, which means that after their definition, Tuples cannot be modified.

Let's see some examples:
'''
people = ('Alice', 'Leo', 'Britney', 'Michael')
year = (1995, 2000, 2005, 2010)
print('{} was born in {}.'.format(people[0], year[1]))
print(type(people))
print(type(year))

'''
Dictionaries (dict)
Dict is a very flexible Python data type.

They are used to group up elements using the key and value structure, where the key is the first element followed by a colon and the value.

Let's see some examples:
'''
car = {'Ford': 'Mustang', 'Dodge': 'Charger', 'Lamborghini': 'Aventador'}
speed = {'Ford': 250, 'Dodge': 327, 'Lamborghini': 355}
print(type(car))
print(type(speed))
