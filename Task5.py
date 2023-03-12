i = int(input('в какой вагон сел Витя? '))
j = int(input('Номер вагона: '))
if j==i:
    print("Невозможно определить")
else:
    r = i+j-1
    print(r)