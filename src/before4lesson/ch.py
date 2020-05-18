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
