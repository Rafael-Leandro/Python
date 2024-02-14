# Python Text Manipulation
# In this class we are going to talk about text manipulation with Python.

'''
Let's begin understanding what is a string chain.
For example: "This is how we code in Python".
We know it as a phrase but for every programming language it is known as a string chain. 
For Python, every string chain is enclosed in single quotes or double quotes.

Let's see how it works with the following variable.
phrase: 'Coding with Python'
The Python is going to save this phrase in the computer memory but the phrase will be splitted and every part will be saved in a certain space in the memory. Even the spaces that exist in the phrase will be saved.
Every memory space will receive a index that is a sequential number where the first number begins with 0 and it goes till the necessary number of letters of the phrase.

We will have something like that:
C | o | d | i | n | g |   | w | i | t | h |    | p | y | t | h | o | n |
0   1   2   3   4   5   6   7   8   9   10  11   12  13  14  15  16  17

By knowing it we can use some operations.

The first one is the string slicing:
Utilizing this operation we can return a specified or a range of characters by using the slice syntax. Let's see how it works.

>> print(phrase)
Writing this line the program will print the whole phrase.

>> print(phrase[12])
Writing this line the program will print the letter that corresponds to the 12 index.

>> print(phrase[0:5])
Writing this line the program will print the characters range beginning in 0 index and going till the 5 index.
Note: It's going to print 'Codin' with the letter 'g' missing because it stops to count when it achieves the 5 index. So, if we want to print it correctly we should use the range [0:6]. 

>> print(phrase[12:18:2])
Writing this line the program will print the characters range beginning in 12 index and going till the 18 index but jumping of two by two.
The result we are going to have is the following character sequence: pto

>> print(phrase[:7])
Writing this line the program will print the characters range beginning in 0 index (even it wasn't declared the program will assume it begins in 0 index) and going till the 7 index.

>> print(phrase[12:])
Writing this line the program will print the characters range beginning in 12 index and going till the final index (even it wasn't declared the program will assume it ends in the last index).

>> print(phrase[7::3])
Writing this line the program will print the characters range beginning in 7 index and going till the final index but jumping of three by three.

------------------------------------------------------------------------------------------------------------------------------------------------

The second operation is the string analysis:
This operation is going to be one that you will use the most. It's used to get strings information, like string length, which letter it begins, what is the first word, and much more.

>> len(phrase)
Writing this line the program will return the number of characters in the string. In this case, the number of characters will be 18.

>> phrase.count('o')
Writing this line the program will count how many times the letter "o" appears in the phrase. If we had a upper case letter "O" it wouldn't count it because "O" is different of "o" in Python.

>> phrase.count('o', 0, 16)
Writing this line the program will count how many times the letter appears in the phrase but already slicing the string.

>> phrase.find('with')
Writing this line the program will find the first occurrence of the specified value. It will return 7 because it's the position where 'with' begins.
Note: The find() method returns -1 if the value is not found.

>> 'python' in phrase
Writing this line the program will return a boolean result of "True" if there is the word in the phrase and "False" if there isn't.

------------------------------------------------------------------------------------------------------------------------------------------------

Another operation we can use is the string transformation:
Through this method we can change the strings.

>> phrase.replace('python', 'android')
Writing this line the program will find the word 'python' in the phrase and then replace it to the word 'android'.

>> phrase.upper()
Writing this line the program will make all the letters in the phrase change to uppercase letters.
Note: The letters that already are in uppercase will remain.

>> phrase.lower()
Writing this line the program will make all the letters in the phrase change to lowercase letters.
Note: The letters that already are in lowercase will remain.

>> phrase.capitalize()
Writing this line the program will convert the first character of a string to uppercase and the remaining characters to lowercase.

>> phrase.title()
Writing this line the program will return a string where the first character in every word is upper case.

>> phrase.strip()
Writing this line the program removes any leading, and trailing whitespaces. 
Note: Leading means at the beginning of the string, trailing means at the end.

>> phrase.rstrip()
Writing this line the program removes only the trailing whitespaces.

>> phrase.lstrip()
Writing this line the program removes only the leading whitespaces.

------------------------------------------------------------------------------------------------------------------------------------------------

Operations we can use to divide and join strings:

>> phrase.split()
Writing this line the program splits a string into a list where each word is a list item.

>> '-'.join(phrase)
Writing this line the program will join all items in a list into a string, using a dash character as separator.
Note: We will have something like that 'Coding-with-Python'

------------------------------------------------------------------------------------------------------------------------------------------------

We can combine methods to achieve an expected result. Let's see how it works in the examples below.
'''
phrase = 'Coding with Python'
print(phrase.upper().count('O'))
print(phrase.lower().find('python'))
print('Coding' in phrase)
Splited = phrase.upper().split()
print('-'.join(Splited))
