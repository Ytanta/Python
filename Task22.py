# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. 
# m - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.
import random

n = int(input("Введите количество чисел для первого множества: "))
m = int(input("Введите количество чисел для второго множества: "))

list_a=[random.randint(1, 10) for i in range(int(n))]
print(list_a)
list_b=[random.randint(1, 10) for i in range(int(m))]
print(list_b)
list_c  = list_a + list_b
print(list_c)
list_c = list(set(list_c))
list_c.sort()
print(list_c)
