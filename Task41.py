# Дан массив, состоящий из целых чисел. Напишите
# программу, которая в данном массиве определит
# количество элементов, у которых два соседних и, при
# этом, оба соседних элемента меньше данного. Сначала
# вводится число N — количество элементов в массиве
# Далее записаны N чисел — элементы массива. Массив
# состоит из целых чисел.
# Ввод: Ввод:
# 5 5
# 1 2 3 4 5 1 5 1 5 1
# Вывод: Вывод:
# 0 2

# A = int(input("Введите количество чисел: "))
# array1=[random.randint(1, 10) for i in range(int(A))]
# import random
# data = [random.randint(0, 9) for i in range(10)]
# print(data)

# count = 0 
# i=1
# for i in range(1, len(data)-1): 
#     if data[i-1] < data[i] and data[i+1] < data[i]: 
#         count+=1
# print(count)