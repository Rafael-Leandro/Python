'''Create a program that reads the name of a city and tells whether or not it begins with the name "SANTO".'''
city = str(input('What city were you born in? ')).strip()
print(city[:5].upper() == 'SANTO')
