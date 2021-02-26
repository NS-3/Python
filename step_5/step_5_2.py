l = 0
sl = 0
with open("my_f_2.txt", 'r', encoding='UTF8') as f_o:
    for line in f_o:
        for letter in line:
            if letter ==' ':
                sl += 1

        print('в строке', l+1, 'слов', sl+1)
        sl = 0
        l = l + 1

print('число строк:', l)
        #tx = x.split()