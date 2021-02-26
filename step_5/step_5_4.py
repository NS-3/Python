num_1={}
num_2={1:'один', 2:'два',3:'три',4:'четыре',5:'пять',6:'шесть',7:'семь'}

with open("my_f_4.txt", 'r', encoding='UTF8') as f_o:
    for line in f_o:
        num_a, n = line.split(' — ')
        num_1[int(n)] = num_a
print(num_1)



l = []
for n in num_1:
    print(num_2[n], '—', n)
    l = l + [num_2[n]+' — '+ str(n)]
print(l)

with open("my_f_4_1.txt", 'w+', encoding='UTF8') as f_ob:
    print (l, file = f_ob)
