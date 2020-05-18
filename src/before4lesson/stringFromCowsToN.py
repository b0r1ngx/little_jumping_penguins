# a = input() # n < 100, n - lyuboe chislo
# var = {'symbol': 'XRPBNB', 'price': '0.01505000'}
# a = ("{price}".format(**var))
# b = str(input())
# print(b.isdigit())
# print(a)
# qwe = int(input("Количество коров:"))
# print("На лугу пасется "+str(qwe))
# a = int(" ".join(filter(lambda s: s.isnumeric(), input().split())))
a = int(input())
if a % 100 == 11:
    print(str(a) + " korov")
elif a % 10 == 1:
    print(str(a) + " korova")
elif a % 100 in range(5, 21):
    print(str(a) + " korov")
elif a % 10 == 2 or a % 10 == 3 or a % 10 == 4:
    print(str(a) + " korovy")
else:
    print(str(a) + " korov")

# На лугу пасется n коров (n принадлежит целому множеству чисел - любое число и даже больше 100!)
# На лугу пасется
# 1 корова
# 2 коровы
# 3 коровы
# 4 коровы
# 5 коров
# 6 коров
# 7 коров
# 8 коров
# 9 коров
# 10 коров
# 11 коров
# 12 коров
# 13 коров
# 14 коров
# 15 коров
# 16 коров
# 17 коров
# 18 коров
# 19 коров
# 20 коров
# 21 корова
# 22 коровы
