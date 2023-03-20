

import random

n = input("Введите количество чисел: ")
list1 = []
list1=[random.randint(1, 10) for i in range(int(n))]
print(list1)
print(len(set(list1)))