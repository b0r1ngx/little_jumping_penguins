a = int(input())
maxim = 0
lessThanMaxim = 0
while a != 0:
    if a >= maxim:
        lessThanMaxim = maxim
        maxim = a
    if a < maxim and a > lessThanMaxim:
        lessThanMaxim = a
    a = int(input())
print(lessThanMaxim)
