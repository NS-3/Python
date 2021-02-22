from random import random, randint, randrange
#print(random())
#print(randint(1, 2))
#print(randrange(1, 10, 2))
from sys import argv

def ot(*args, **kwargs):

    for el in args:
        print(f"сотрудник {el}")
        vr = randint(0, 160)
        st = randint(1000, 2000)
        pr = randint(0, 10000)
        if vr == 0:
            pr = 0
        el = vr * st + st
        print(f"ваша выработка {vr} часов за месяц")
        print(f"ваша ставка за час {st} рублей за час")
        print(f"ваша премия {pr} рублей")
        print(f"ваша зарплата {el} рублей")

#ot(1, 2, 3)
ot (*argv[1:])


