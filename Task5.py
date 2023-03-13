while True:
    i = (input('в какой вагон сел Витя? '))
    j = (input('Номер вагона: '))
    if i.isdigit() == False and j.isdigit() == False:
        print('Неверный тип')
    else:
        break
if j==i:
    print("Невозможно определить")
else:
    r = int(i) + int(j) - 1
    print(r)