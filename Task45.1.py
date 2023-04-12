import random
array1 = list(range(1, 10))

# A = int(input("Твой ход(от 1 до 9): "))
def User_Move(array):
    A = int(input("Твой ход: "))
    if 0>A and A>9:
        print("Некорректное число")
        if array[A] == 0 or 10:
            print("Уже занято. Перехаживай")
            print(User_Move(array1))
        else:
            array[A] = 0
        return array

print(array1)
print(User_Move(array1))
print(array1)



# def check(array):
#     if len(set(array)) == 0 and 10:
#         print("Ничья!!")
#         if ((array[1], array[2], array[3] == 10 or 0) or (array[4], array[5], array[6] == 10 or 0) or (array[7], array[8], array[9] == 10 or 0) or (array[1], array[4], array[7] == 10 or 0) or (array[2], array[5], array[8] == 10 or 0) or (array[3], array[6], array[9] == 10 or 0) or (array[1], array[5], array[9] == 10 or 0) or (array[3], array[5], array[7] == 10 or 0)):
#             print("С победкой!!")
#     array[A] = 0
# def AI_Move(array):
#     B = random.randint(1, 10)
#     if array[B] == 0 or 10:
#         AI_Move
#     else:
#         print(f"А я хожу сюда {B}")
# def Tic_Tac_Toe (array):
#     User_Move(array)
#     check(array)
#     AI_Move
#     check(array)



