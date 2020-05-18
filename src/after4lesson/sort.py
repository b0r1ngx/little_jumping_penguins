surnames = []
# with open('input.txt', 'r', encoding='utf8') as in_file, \
#     open('output.txt', 'w', encoding='utf8') as out_file:
#     for line in in_file:
#         a = in_file
#         surnames.append(in_file)
# print(in_file)
for line in open('input.txt', 'r', encoding='utf8'):
    row = line.split()
    surnames.append((row[0] + ' ' + row[1] + ' ' + row[3] + '\n'))
    surnames.sort()
out = open('output.txt', 'w', encoding='utf8')
out.writelines(surnames)
# in_file.close()
# out_file.close()

