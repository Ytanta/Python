n= int(input("Введите число"))
res=1

if n<0:
    print('Введите целое неотрицательное число')
else:
    while n>0:
        res *=n
        n-=1
print(res)