# Python modules
# In this class we are going to talk about Python modules.

'''
Python just like the other programming languages works with installables modules and predefined modules.
It means that everytime we create a program in Python it comes with the basics functionalities which makes the program to be fast and avoids the waste of memory.
So, everytime we need a different functionality we have to import it.

To use it in Python we need to think in modules as a code library.
For example:
            | Food |
Pizza, Hotdogs, Hamburger, Soup, Steak
            | Drinks |
Juice, Tea, Soda, Coffee, Milk
            | Sweets |
Cookies, Cake, Pudim, Ice Cream, Pie, Donuts

We can import the whole food library by using the command: import Food
Or we can import just one of the foods from this food library by using the command: from Food import Pizza

We are going to be using a common library in Python and its modules for next examples. 
The library we are going to use is the math library.

Here are some modules of the math library:

math.ceil(x)
    Return the ceiling of x, the smallest integer greater than or equal to x.

math.floor(x)
    Return the floor of x, the largest integer less than or equal to x.

math.trunc(x)
    Return x with the fractional part removed, leaving the integer part. It is equivalent to floor() for positive x, and equivalent to ceil() for negative x.

math.pow(x, y)
    Return x raised to the power y. It is like x**y.

math.sqrt(x)
    Return the square root of x.

math.factorial(x)
    Return x factorial as an integer. Raises ValueError if x is not integral or is negative.
'''
import math  # We could import only the sqrt module by writing 'from math import sqrt' 
num = int(input('Write a number: '))
root = math.sqrt(num) # Utilizing 'from math import sqrt' we just need to write 'sqrt(num)'
print('The square root of {} is {:.2f}'.format(num, root))

# Another Python library
import random
n = random.randint(1, 10) # It will select a random number from 1 to 10
print(n)
