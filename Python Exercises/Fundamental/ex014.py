'''Write a program that converts a temperature typed into Celsius degrees and converts to Fahrenheit degrees'''
C = float(input('Enter the temperature in Celsius degrees: '))
F = ((9 * C) / 5) + 32  # We also can use the expression F = C * 1.8 + 32
print('The temperature of {:.1f}°C corresponds to {:.1f}°F!'.format(C, F))
# We can also convert Celsius degrees to Kelvin
K = C + 273.15
print('The temperature of {:.1f}°C corresponds to {:.2f} K!'.format(C, K))
