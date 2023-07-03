'''Write an algorithm that reads an employee's salary and outputs their new salary, with a 15% increase'''
salary = float(input('How much the employee earns? US$ '))
new = salary + (salary * 15 / 100)
print('The employee that used to earn US$ {:.2f}, now with a 15% increase, will receive US$ {:.2f}'.format(salary, new))
