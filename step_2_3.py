from typing import List

a = int(input('введите номер месяца: '))
#print(y_list.index(a))
w_list=[1, 2, 12]
s_list=[3, 4, 5]
sum_list= [6, 7, 8]
o_list=[9, 10, 11]

if (a in w_list):
    print('зима')
if a in s_list:
    print('весна')
if a in sum_list:
    print('лето')
if a in o_list:
    print('осень')

a = int(input('введите номер месяца: '))
y_dict = {1:'зима',2:'зима',12:'зима',3:'весна',4:'весна',5:'весна',6:'лето',7:'лето',8:'лето',9:'осень',10:'осень',11:'осень'}
print(y_dict.get(a))