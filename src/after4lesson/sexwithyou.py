# <->ЗАДАНИЕ: Каждый из N школьников некоторой школы знает Mᵢ языков.
# Определите, какие языки знают все школьники и языки, которые знает хотя бы один из школьников.
# <->ФОРМАТ ВВОДА: Первая строка входных данных содержит количество школьников N.
# Далее идет N чисел Mᵢ, после каждого из чисел идет Mᵢ строк, содержащих названия языков,
# которые знает i-й школьник. Длина названий языков не превышает 1000 символов,
# количество различных языков не более 1000. 1≤N≤1000, 1≤Mᵢ≤500.
# <->ФОРМАТ ВЫВОДА: В первой строке выведите количество языков, которые знают все школьники.
# Начиная со второй строки - список таких языков. Затем - количество языков,
# которые знает хотя бы один школьник, на следующих строках - список таких языков.
# Входные данные:
# 3
# 3
# Russian
# English
# Japanese
# 2
# Russian
# English
# 1
# English
# Вывод программы:
# 1
# English
# 3
# Russian
# Japanese
# English

all_languages = set()
how_all = 0
N = int(input())
list_with_language_packets = [[] for i in range(N)]
for teen in range(N):
    how_much_languages = int(input())
    while how_much_languages >= 1:
        how_much_languages -= 1
        list_with_language_packets[teen].append(input())

for teen in range(len(list_with_language_packets)):
    for language in range(len(list_with_language_packets[teen])):
        this = list_with_language_packets[teen][language]
        if this not in all_languages:
            all_languages.add(this)
            how_all += 1

we_all_know_this = set(list_with_language_packets[0])
for teen in range(1, len(list_with_language_packets)):
    we_all_know_this = (we_all_know_this & set(list_with_language_packets[teen]))

print(len(we_all_know_this))
for i in we_all_know_this:
    print(i)
print(how_all)
for i in all_languages:
    print(i)
