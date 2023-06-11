'''
Write a program that reads how much money a person has in their wallet and shows how many dollars they can buy.
Considering the dollar values of June 11th of 2023
US$ 1,00 = R$ 4,8922
'''
real = float(input('How much money do you have in your wallet? R$ '))
dollar = real / 4.8922
print('With R${:.2f} you can buy US${:.2f}'.format(real, dollar))
print('-' * 25)
# Considering the euro values of June 11th of 2023
# € 1,00 = R$ 5,2591
euro = real / 5.2591
print('With R${:.2f} you can buy €{:.2f}'.format(real, euro))
print('-' * 25)
# Considering the yen values of June 11th of 2023
# R$ 1,00 = ¥ 28,4819
yen = real * 28.4819
print('With R${:.2f} you can buy ¥{:.2f}'.format(real, yen))
