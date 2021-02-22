from random import randint
#lst = [randint(1, 1500) for el in range(20)]
lst = [5, 6, 7, 5, 7, 7, 8, 30, 65]

print(lst)
l = [lst[el] for el in range(len(lst)) if lst.count(lst[el]) < 2]
print(l)

#print(pl)

