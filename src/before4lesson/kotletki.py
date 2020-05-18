k, m, n = int(input()), int(input()), int(input())
# k - сколько можно жарить сразу
# m - минут пожарить на одной стороне
# m1 = 2*m - сколько нужно жарить одну котлету
# n - кол-во котлет
m1 = 2 * m
if n == 0 or m == 0 or k == 0:
    print(0)
if n <= k:
    print(int(m1))
elif 2*n % k != 0:
    a = int(n / k)
    print((a * m1) + m1)
else:
    print(int((n/k) * m1))
# k = int(input())  # сторон за один заход
# m = int(input())  # minutes
# n = int(input())  # всего котлет дано
# a = n * 2  # всего сторон дано
# if n <= k:
#     print(int(2 * m))
# elif a % k != 0:
#     print(m * (a // k + 1))
# else:
#     print(m * (a // k))
