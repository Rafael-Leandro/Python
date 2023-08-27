'''Write a program that reads any angle and shows on the screen the value of sine, cosine and tangent of that angle'''
import math
angle = float(input('Write the angle that you want: '))
sine = math.sin(math.radians(angle))
print('The angle of {} has its sine of {:.2f}'.format(angle, sine))
cosine = math.cos(math.radians(angle))
print('The angle of {} has its cosine of {:.2f}'.format(angle, cosine))
tangent = math.tan(math.radians(angle))
print('The angle of {} has its tangent of {:.2f}'.format(angle, tangent))
