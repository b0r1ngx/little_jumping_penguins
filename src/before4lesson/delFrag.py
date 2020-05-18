string = str(input())
firstH = string.find('h')
lastH = string.rfind('h')
sequenceBetweenH = string[firstH:lastH+1]
s = string.replace(sequenceBetweenH, "")
print(s)
