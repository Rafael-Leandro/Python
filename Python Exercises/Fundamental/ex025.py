''' Write a program that reads a sentence from the keyboard and display:
• How many times the letter "A" appears;
• In which position it appears the first time;
• In which position it appears the last time. '''

phrase = str(input('Write a phrase: ')).upper().strip()
print('The letter "A" appears {} times in the sentence.'.format(phrase.count('A')))
print('The first letter "A" appears in the position {}.'.format(phrase.find('A')+1))
print('The last letter "A" appears in the position {}.'.format(phrase.rfind('A')+1))
