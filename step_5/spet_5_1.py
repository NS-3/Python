a=0
with open("my_f_1.txt", 'w+', encoding='UTF8') as f_o:
    while a < 5:
        f_o.write(input()+'\n')
        a = a + 1
    f_o.seek(0)
    content = f_o.read()
    print(content)



