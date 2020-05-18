all_languages = set()
how_all = 0
we_all_know_this = set()
how_unique = 0
N = int(input())
list_with_language_packets = [[] for i in range(N)]
for teen in range(N):
    how_much_languages = int(input())
    for language in range(how_much_languages):
        list_with_language_packets[teen][language] = input()
for teen in range(len(list_with_language_packets)):
    for language in range(len(list_with_language_packets[teen])):
        this = list_with_language_packets[teen][language]
        if this not in all_languages:
            all_languages.add(this)
            how_all += 1
apply_for_first = list_with_language_packets[0]
for teen in range(len(list_with_language_packets)):
    # this = list_with_language_packets[teen]
    for language in list_with_language_packets[teen]:
        if language in we_all_know_this:
            continue
        for each in apply_for_first:
            if each == language:
                we_all_know_this.add(language)
                how_unique += 1
                break
print(how_unique)
# for i in range(len(we_all_know_this)):
print(we_all_know_this)
print(how_all)
# for i in range(len(all_languages)):
print(all_languages)
