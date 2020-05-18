A, B = int(input()), int(input())
N = int(input())
# A- rub, B- cents, N- how much
cost = A * N
cents = B * N
if cents < 100:
    print(cost, cents)
else:
    cost = cost + cents / 100
    print(int(cost), cents % 100)
