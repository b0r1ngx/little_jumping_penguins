a = list(map(int, input().split()))
ourFamily = set()
for i in range(len(a)):
    if a[i] not in ourFamily:
        print('NO')
        ourFamily.add(a[i])
    else:
        print('YES')
print(len(ourFamily))
