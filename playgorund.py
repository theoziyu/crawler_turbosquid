"""url_file = open("url_dict.txt", "r")
lines = url_file.readlines()
url_file.close()
clean_list = list()
for line in lines:
    words = line.split(',')
    if words[1].endswith('\n'): words[1] = words[1].rstrip()
    # for word in words:
    #     word.rstrip()
    clean_list.append(words)
print(clean_list)

for couple in clean_list:
    a, b = couple[0], couple[1]
    print(a, b)
"""

import os

patika = "http://www.policeman.sk/Police%20vehicles/PVAS.jpg"

print(os.path.basename(patika))