# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

# *Пример:*

# 3 2 4 -> yes
# 3 2 1 -> no

while True:
    n = (input('Длина шоколадки: '))
    m = (input('Ширина шоколадки: '))
    k = (input('Сколько хочешь долик, если оба перфекционисты? '))
    if n.isdigit() == False and n.isdigit() == False and k.isdigit() == False:
        print('He уговоришь...Давай количество')
    else:
        break
if int(n) * int(m)<int(k):
        print("He жадничай!!!")
elif int(n) * int(m) ==int(k):
        print("Хочешь всю? Держи")
elif int(k)%2==0:
    print("Держи свои дольки")
else:
    print("Никаких долик. Пойдем заедать ОКР")