
def m_del():
    a = int(input('введите a: '))
    b = int(input('введите b: '))
    if b == 0:
        y = "на ноль делить нельзя"
    else:
        y= a/b
  # print(y)
    return y
m_rez = m_del()
print(m_rez)

