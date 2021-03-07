from random import randint


class Matrix:
    def __init__(self, lst):
        self.lst = lst


    def __str__(self):
          return '\n'.join(map(str, self.lst))


    def __add__(self, other):
        mxs = [[self.lst[i][j] + other.lst[i][j] for j in range(len(self.lst[0]))] for i in range(len(self.lst))]
        print(mxs)
        return '\n'.join(map(str, mxs))



x = randint(2, 5)
y = randint(2, 5)
print(f'матрица {y} на {x}')

lst1 = [[randint(0, 100) for j in range(x)] for i in range(y)]
lst2 = [[randint(0, 100) for j in range(x)] for i in range(y)]
#list1 = [[1,2,3], [4,5,6], [7,8,9]]

#print(f'\n'.join(map(str, list1[]))
#new_list = list(map(str, list1))
#new_list1 = '\n'.join(map(str, lst1))
#print('m1 \n', new_list1)
#new_list2 = '\n'.join(map(str, lst2))
#print('m2 \n', new_list2)

mx1 = Matrix(lst1)
#mx1.run()

mx2 = Matrix(lst2)
print('mx1 \n', mx1,'\n' 'mx2 \n', mx2, '\n' 'mxs \n', mx1+mx2)
