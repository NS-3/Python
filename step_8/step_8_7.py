from random import randint

class Comp:
    def __init__(self, par1, par2):
        self.par1 = par1
        self.par2 = par2
    def make_comp(self):
        n = complex(self.par1, self.par2)
        return n

    def __add__(self, other):
        return Comp(self.par1 + other.par1, self.par2 + other.par2)

    def __sub__(self, other):
        return Comp(self.par1 - other.par1, self.par2 - other.par2)

cmp1 = Comp(randint(-20, 20),randint(-20, 20))
cmp2 = Comp(randint(-20, 20),randint(-20, 20))
print(f'результат cmp1 \n{cmp1.make_comp()}')
print(f'результат cmp2 \n{cmp2.make_comp()}')
cmp_add = cmp1+cmp2
print(f'результат cmp_add\n{cmp_add.make_comp()}')

cmp_sub = cmp1-cmp2
print(f'результат cmp_sub\n{cmp_sub.make_comp()}')
