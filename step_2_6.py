nam = [1,2,3]
tvr = []
a=0
while a<3:
    name = input('введите наименование товара: ')
    prc = int(input('введите цену товара: '))
    n= int(input('введите количество товара: '))
    ed = input('введите единицы измерения: ')
    tv_a = {"название":name, "цена":prc, "количество":n, "el":ed}
    print(tv_a)
    a=a+1
    tvr.insert(a, tv_a)

print (tvr)
cat = list(zip(nam,tvr))
print (cat)
#не понимаю, как дальше сделать

