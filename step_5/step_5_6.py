import re
s = 0
sjs = {}
with open("my_f_6.txt", 'r', encoding='UTF8') as f_o:
    for line in f_o:
        print(line)
        sj, cl = line.split(':')
        cls = cl.split()
        s = 0
        for n in cls:
            n = re.findall(r'\d+', n)
            for el in n: s = s + int(el)

        sjs[sj] = s
print(sjs)