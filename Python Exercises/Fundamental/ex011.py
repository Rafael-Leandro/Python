'''Make a program that reads the width and height of a wall in meters, calculates its area and the amount of paint needed to paint it, knowing that each liter of paint paints an area of 2 square meters'''
width = float(input('Width of the wall: '))
height = float(input('Height of the wall: '))
area = width * height
print('This wall has the dimension of {:.2f} x {:.2f} and its area is of {:.2f}m².'.format(width, height, area))
ink = area / 2
print('To paint this wall you will need of {:.2f}L of paint.'.format(ink))
