'''Write a program that reads a value in meters and displays it converted to different measurements'''
meters = float(input('Write a distance in meters: '))
centimeters = meters * 100
millimeters = meters * 1000
kilometer = meters / 1000
mile = meters / 1609
# The mile is adopted in English-speaking countries, such as England and the United States.
yards = meters * 1.094
# It is currently used to measure sports fields such as soccer, American football, cricket and golf, it is also used to measure boat sizes.
foots = meters * 3.281
# This measurement is widely used in aviation.
inches = meters * 39.37
# Currently, the inch measurement is widely used in everyday situations, as a reference for the screen size of televisions and computer monitors.

print('The distance of {}m corresponds to {}cm'.format(meters, centimeters))
print('-' * 25)
print('The distance of {}m corresponds to {}mm'.format(meters, millimeters))
print('-' * 25)
print('The distance of {}m corresponds to {}km'.format(meters, kilometer))
print('-' * 25)
print('The distance of {}m corresponds to {:.3f} miles'.format(meters, mile))
print('-' * 25)
print('The distance of {}m corresponds to {:.2f} yards'.format(meters, yards))
print('-' * 25)
print('The distance of {}m corresponds to {:.2f} foots'.format(meters, foots))
print('-' * 25)
print('The distance of {}m corresponds to {:.2f} inches'.format(meters, inches))
