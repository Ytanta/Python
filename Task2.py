# Задача 2: Найдите сумму цифр трехзначного числа.

# *Пример:*

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

N = int(input('Введите число: '))
Result=0
while N>0:
    
    Result =  Result + (N%10)
    N=N//10
print(Result)