'''Write an algorithm that reads the price of a product and shows its new price, with 5% off'''
price = float(input('What is the price of the product? US$ '))
new = price - (price * 5 / 100)
print("The product that cost US$ {:.2f}, with a 5% discount, will cost US$ {:.2f}".format(price, new))
