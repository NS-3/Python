def my_func(x):
    y = x.lower()
    y = y.title()
    return (y)
x = input("введите текст ")
tx = x.split()


m_text = my_func(x)
print(m_text)