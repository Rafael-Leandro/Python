'''Write a program that reads two grades of a student, calculates it and displays its average'''
grade1 = float(input("First student's grade: "))
grade2 = float(input("Second student's grade: "))
average = (grade1 + grade2) / 2
print('The average between {:.1f} and {:.1f} is equal to {:.1f}'.format(grade1, grade2, average))
