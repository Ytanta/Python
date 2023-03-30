# Дан список чисел. Посчитайте, сколько в нем пар
# элементов, равных друг другу. Считается, что любые
# два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать. Вводится список
# чисел. Все числа списка находятся на разных
# строках.
# Ввод: Вывод:
# 1 2 3 2 3 2

import random
import math
from collections import Counter
A = int(input("Введите количество чисел: "))
array1=[random.randint(1, 10) for i in range(int(A))]

res = Counter()

for i in array1:
    res[i]+=1
print(res)

Count = 0
for k,v in res.items():
    if v >1:
        Count+=v//2
print(Count)