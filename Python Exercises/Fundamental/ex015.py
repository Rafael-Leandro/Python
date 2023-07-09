'''Write a program that asks for the number of kilometers traveled by a rented car and the number of days it was rented.
Calculate the price to pay, knowing that the car costs US$60 per day and US$0.15 per km driven'''
days = int(input('How many days was it rented? '))
km = float(input('How many kilometers was it driven? '))
pay = (days * 60) + (km * 0.15)
print('The total amount to be paid is US${:.2f}'.format(pay))
