
wks = {}
s=0
l = 0
print('список сотрудников с окладом < 20000:')
with open("my_f_3.txt", 'r', encoding='UTF8') as f_o:
    for line in f_o:
        l += 1
        fio, fix = line.split()
        wks[fio] = fix
        s = s + int(fix)
        if int(fix) < 20000:
            print (fio, fix)
    print("средняя зарплата:", s/l)

