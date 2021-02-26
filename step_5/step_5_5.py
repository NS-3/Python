s=0
print("введите числа через пробел:")
with open("my_f_5.txt", 'w+', encoding='UTF8') as f_o:
    f_o.write(input())
    f_o.seek(0)
    content = f_o.read()
sum = content.split()
for el in  sum:
    s = s + int(el)
print(s)
