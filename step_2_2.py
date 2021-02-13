
a = int(input('введите длину списка: '))
x=0
r_list = []
while x<a:
    n =input('введите значение:  ')
    r_list.append(n)
    x=x+1

print('введен список:', r_list)

#a=7
x=0
while x<a:
    n = r_list[x]
    r_list.insert(x+2,n)
    r_list.pop(x)
    x=x+2
print('изменен список:', r_list)
