i = float(input())
splitted = '{:.2f}'.format(i).split(".")
print(splitted[0], int(splitted[1]))
