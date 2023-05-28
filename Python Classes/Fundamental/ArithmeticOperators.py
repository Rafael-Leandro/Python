# Python Arithmetic Operators
# In this class we are going to talk about Python arithmetic operators and its precedence order.

'''
Arithmetic operators are used with numeric values to perform common mathematical operations:

Operator       Name
   +         Addition
   -         Subtraction
   *         Multiplication
   /         Division
   **        Exponentiation
   //        Floor Division
   %         Modulus

Now it's important to know the precedence order of these operators in order to avoid wrong results on future programs.
The precedence order it's going to be:

1º = () - Anything inside a parentheses comes first
2º = **
3º = *, /, //, %
4º = +, -

---Additional Information---
We can do the exponentiation of a number using the inner function of exponentiation.
Example: 
pow(4, 3) which is going to give us the result 64.

We can also find the square root of a number using the exponentiation operator.
Example:
81 ** (1/2) which is going to give us the result 9.
If you use (1/3) you will find the cubic root.
'''

n1 = int(input('Write a number: '))
n2 = int(input('Write another number: '))
add = n1 + n2
sub = n1 - n2
mult = n1 * n2
div = n1 / n2
exp = n1 ** n2
fld = n1 // n2
mod = n1 % n2
print('The addition result is {}'.format(add))
print('The subtraction result is {}'.format(sub))
print('The multiplication result is {}'.format(mult))
print('The division result is {}'.format(div))
print('The exponentiation result is {}'.format(exp))
print('The floor division result is {}'.format(fld))
print('The modulus result is {}'.format(mod))

# Different ways to print
print('-' * 25)
print('The division result is {:.2f}'.format(div))
# It will show on the screen the division with two decimal places.
print('The addition result is {}'.format(add), end=' ')
print('The subtraction result is {}'.format(sub))
# The (end=' ') won't let the code break the line and will print the next sentence aside it. To break the line we use (\n).
name = 'Rafael'
print('Nice to meet you {:20}!'.format(name))
# The name will be written in 20 spaces.
print('Nice to meet you {:>20}!'.format(name))
# The name will be aligned to the right. {:<20} will align it to the left.
print('Nice to meet you {:^20}!'.format(name))
# It will centralize it.
print('Nice to meet you {:=^20}!'.format(name))
