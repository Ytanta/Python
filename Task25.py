# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2

letters = "a a a b c a a d c d d"
dict_letters = {}
result_string = ""

letters = letters.split(" ")
for i in range(len(letters)):
    if dict_letters.get(letters[i]) == None:
        dict_letters[letters[i]] = 0
        result_string += f" {letters[i]} "
    else:
        dict_letters[letters[i]] +=1
        result_string +=f" {letters[i]}_{dict_letters[letters[i]]} "
print(result_string)

