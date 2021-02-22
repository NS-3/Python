from random import randint
from functools import reduce
lst = [randint(1, 1500) for el in range(20)]
print(lst)
l = [lst[el] for el in range(1,len(lst)) if lst[el] % 2 == 0 and lst[el] >=100 and lst[el] <=1000]
print(l)
pl= reduce(lambda x,y: x * y, l)
print(pl)