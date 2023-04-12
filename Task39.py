# Даны два массива чисел. Требуется вывести те элементы
# первого массива (в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве. Пользователь вводит
# число N - количество элементов в первом массиве, затем N
# чисел - элементы массива. Затем число M - количество
# элементов во втором массиве. Затем элементы второго массива
# Ввод: Вывод:
# 7 3 3 2 12
# 3 1 3 4 2 4 12
# 6
# 4 15 43 1 15 1 (каждое число вводится с новой строки)

import random

A = int(input("Введите количество чисел: "))
B = int(input("Введите количество чисел: "))

array1=[random.randint(1, 10) for i in range(int(A))]
array2=[random.randint(1, 10) for i in range(int(B))]
print(array1,array2)
array3 = list()
for template in array1:
    if template not in array2:
        array3.append(template)
    else:
        array2.remove(template)
print(array3)
h=len(array2)
for i in range(len(array1)):
    for j in range(len(array2)):
        if array1[i]!=array2[j]:
            h-=1
            if h==0:
                print(array1[i])
                h=len(array2)

print(list(filter(lambda x: x not in array2, array1)))
        