n = int(input())
sumOfSeries = 1
if n == 1:
    print(sumOfSeries)
else:
    for i in range(2, n + 1):
        self = 1 / (i * i)
        sumOfSeries = sumOfSeries + self
    print(sumOfSeries)
