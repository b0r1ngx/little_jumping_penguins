a = int(input()) #1  1   3
b = int(input()) #2  3   2
c = int(input()) #3  2   1

if (a >= b) and (a >= c):
    print(a)
elif (b >= a) and (b >= c):
    print(b)
else:
    print(c)

# print(max(a, b, c))
