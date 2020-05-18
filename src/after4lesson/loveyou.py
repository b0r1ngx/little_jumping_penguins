surnames = []
for line in open('input.txt', 'r', encoding='utf8'):
    row = line.split()
    surnames.append((row[0] + ' ' + row[1] + ' ' + row[3] + '\n'))
    surnames.sort()
out = open('output.txt', 'w', encoding='utf8')
out.writelines(surnames)
