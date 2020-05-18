a = int(input())
maxim = a
count = 0
while a != 0:
    if a > maxim:
        maxim = a
        count = 0
    if a == maxim:
        count = count + 1
    a = int(input())
print(count)
