# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть
import random

n = int(input("Введите количество монеток: "))
if(n<=1):
    print("Закинь еще монеток")
    
heads_tailst=[random.randint(0, 1) for i in range(int(n))]
print(heads_tailst)
head=0
tailst=0
for i in range(int(n)):
    if ((heads_tailst[i]) == 1):
        head+=1
    if ((heads_tailst[i]) == 0):
        tailst+=1
if(head==0 and tailst==0):
    print("Вот так удача. Нет лишней работы")
elif(head==tailst):
    print("Равное количество")
elif(head>tailst):
    print("Перевернуть хвосты")
else:
    print("Перевернуть головы")


    

