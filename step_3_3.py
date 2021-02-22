def my_func(x_1, x_2, x_3):
    y_1 = min(x_1, x_2, x_3)
    y = x_1 + x_2 + x_3 - y_1
    return (y)

x_1 = int(input("введите число:  "))
x_2 = int(input("введите число:  "))
x_3 = int(input("введите число:  "))

m_max = my_func(x_1, x_2, x_3)
print(m_max)
