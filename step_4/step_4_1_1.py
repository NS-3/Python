
from sys import argv

def ot(*args, **kwargs):
    print(f"при выработке {argv[1]} часов за месяц, ставке за час {argv[2]} рублей и премии в размере {argv[3]} рублей")
    s = int(argv[1]) * int(argv[2]) + int(argv[3])
    print(f"ваша зарплата {s} рублей")
    return s

#ot(10, 40, 50)
ot (*argv[1:])
