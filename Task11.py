# Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не
# является числом Фибоначчи, выведите число -1.
# Input: 5
# Output: 6
n = int(input("Введите число"))
a = 0
b=1
count = 1
if n ==0:
    print(count)
else:
    while(a<n):
        a,b=b,a
        b+=a
        count+=1
    if n ==a:
        print(f"Число на позиции{count}")
    else:
        print("-1")