import json

prof = 0
l = 0
n=0
itog =[]
prb1 = {}
prof_i = {}
with open("my_f_7.txt", 'r', encoding='UTF8') as f_o:
    for line in f_o:
        print(line)
        prb =line.split()
        n = n+1
        pb = (int(prb[2]) - int(prb[3]))
        print(pb)
        #sj, cl = line.split(':')
        #cls = cl.split()
        prb1[prb[0]] = pb

        if pb>0:
            prof = prof + pb
            l = l + 1
    profit = prof/l
    print(profit)

    prof_i['profit'] = profit
    itog.append(prb1)
    itog.append(prof_i)
    print(itog)

with open("my_f_5_7.json", "w") as write_f:
    json.dump(itog, write_f)
    #json.dump(prb1, write_f)
    #json.dump(prof_i, write_f)

