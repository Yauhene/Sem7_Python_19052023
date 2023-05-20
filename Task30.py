﻿# Задача 30: Заполните массив элементами арифметической
# прогрессии. Её первый элемент, разность и количество
# элементов нужно ввести с клавиатуры. Формула для
# получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

# Ввод: 7 2 5
# Вывод: 7 9 11 13 15

print('-------------------------------------------------------------')
a1 = int(input('Введите первое число прогрессии: '))
n = int(input('Введите число элементов прогрессии: '))
d = int(input('Введите разность: '))
array = []

# def calk(a1,d,el):
#     res = a1+(el-1)*d
#     return res
    
calk = lambda a1,d,i: a1+(i-1)*d

for i in range(1, n+1):
    #res = calk(a1,d,i)
    array.append(calk(a1,d,i))
    
print(array)