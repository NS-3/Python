from random import randint


class Odej:
    def __init__(self, par):
        self.par = par
    @property
    def cal(self):
        ...

    def __add__(self, other):
        return self.cal + other.cal

class Coat(Odej):
    @property
    def cal(self):
        sum = round(self.par / 6.5, 1) + 0.5
        #print(sum)
        return sum



class Costm(Odej):
    @property
    def cal(self):
        sum = round(2 * self.par/100) + 0.3
        #print(sum)
        return sum



v = randint(32, 56)
h = randint(150, 230)
print(f'размер {v}, рост {h}')


ct = Coat(v)


cm = Costm(h)
sum = round((ct + cm)*10) / 10

print(f'на пальто {ct.cal}м,\nна костюм {cm.cal}м,\nвсего {sum}м')
