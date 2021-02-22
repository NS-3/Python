def my_sm(*args):
    y = sum(*args)
    return (y)
try:
    x = input("введите числа через пробел:  ")
    sp = [float(n) for n in x.split()]
except ValueError:
    print('ошибочка, введие числа')
#print(sp)
m_sm = my_sm(sp)
print(m_sm)

import string
sm = [_ for _ in string.punctuation]
#print(sm)
try:
    x = input("введите числа через пробел:  ")
    sp = [_ for _ in x.split()]
    b = float(0)
    for n in sp:
        if n in sm:
            break
        b = b + float(n)
        #print(b)



 #   print(x.index('!'))
except ValueError:
    print('ошибочка')
#    print (sp.index())



m_sm = m_sm + b
print(m_sm)

