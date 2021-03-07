from random import randint


class Cell:
    def __init__(self, par):
        self.par = par
       # self.ch = ch
    def make_order(self, ch):
       # mxs = [['*' for j in range(self.par[1])]]
        y = self.par // ch
        ost = self.par % ch
        moc = [['*' * ch] for el in range(y)]
        moc.append(['*' * ost])
      #  print(moc)
      #  print('ltktybt\n','\n'.join(map(str, moc)))
        return '\n'.join(map(str, moc))


    def __add__(self, other):
        return Cell(self.par + other.par)

    def __mul__(self, other):
        return Cell(self.par * other.par)
    def __sub__(self, other):
        if (self.par - other.par) <= 0:
            raise TypeError(
                print("операция невозможна, результат отрицательный"))
        return Cell(self.par - other.par)

    def __truediv__(self, other):
        if (self.par // other.par) <= 0:
            raise TypeError(
                print("операция невозможна, так нельзя поделиться"))
        return Cell(self.par // other.par)


#c = 0
#while c==0:
cl1 = randint(1, 20)
cl2 = randint(1, 20)
n = randint(2, 20)
 #   if cl1> n and cl2 > n: c = 1

print(f'число ячеек cl1 {cl1} \nчисло ячеек cl2 {cl2}\nчисло ячеек в строке n {n}')


cls1 = Cell(cl1)
cls2 = Cell(cl2)
print(f'результат mo cls1 \n{cls1.make_order(n)}')
print(f'результат mo cls2 \n{cls2.make_order(n)}')
cls_add = cls1+cls2
print(f'результат cls_add\n{(cls_add.make_order(n))}')

cls_mul = cls1*cls2
print(f'результат cls_mul\n{(cls_mul.make_order(n))}')

cls_sub = cls1-cls2
print(f'результат cls_sub\n{(cls_sub.make_order(n))}')


cls_truediv = cls1/cls2
print(f'результат cls_truediv\n{(cls_truediv.make_order(n))}')