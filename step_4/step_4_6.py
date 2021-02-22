from itertools import cycle, count
from time import sleep
n=0
z = 0
print(z)
for z in count(3, 2):
   # sleep(.5)
    print(z)
    if z > 15: break
l = [1, 2, 4]
for z in cycle(l):
   # sleep(.5)
    print(z)
    n=n+1
    if n > 10: break