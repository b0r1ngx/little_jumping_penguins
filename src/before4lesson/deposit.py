# idiotism of course..

P = int(input())
X, Y = int(input()), int(input())
number = (float(str(X) + "." + str(Y)) / 1000)
value = float((number * (1 + P / 100)) * 1000) - 0.0049
appValue = '{:.2f}'.format(value).split(".")
print(appValue[0], int(appValue[1]))
