from random import random, randint, randrange
#print(random())
lst = [randint(1, 100) for el in range(20)]
print(lst)
l = [lst[el] for el in range(1,len(lst)) if lst[el] > lst[el-1]]
print(l)
