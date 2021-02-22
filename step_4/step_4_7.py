from math import factorial
from random import randint


def fact(n):
    g = [factorial(el) for el in range(1, n+1)]
 #   for el in g:
    yield g
n = randint(1, 10)
print(n)
g = fact(n)
print(g)
for el in g:
    print(el)

