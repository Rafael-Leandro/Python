'''Write a program that will read something from the keyboard and show on the screen your primitive type and all the possible information about it'''
a = input('Write something: ')
print('The primitive type of this value is ', type(a))
# All input without definition (int, float, bool) will be a string type.
print('Is there only spaces? ', a.isspace())
print('Is it a number? ', a.isnumeric())
print('Is it alphabetical? ', a.isalpha())
print('Is it alphanumeric? ', a.isalnum())
print('Is it in capital letters? ', a.isupper())
print('Is it in lower case? ', a.islower())
print('Is it capitalized? ', a.istitle())

'''
'a' is an object and all objects have characteristics and accomplish functionalities. 
It means that the objects have attributes and methods, where Attributes are the properties of an object and Methods are the actions that an object can perform.
'a.code()' is a method.
'''
