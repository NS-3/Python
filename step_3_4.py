def my_func(x, y):
    z=1
    y = abs(y)
    for el in range (y):
        z = z * 1/x
        print(z)
    return (z)
x = int(input("введите число >0:  "))
y = int(input("введите число <0:  "))


m_dl = my_func(x, y)
print(m_dl)
