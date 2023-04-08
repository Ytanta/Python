# Создать телефонный справочник с
# возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться
# в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в
# текстовом файле
# 3. Пользователь может ввести одну из
# характеристик для поиска определенной
# записи(Например имя или фамилию
# человека)
# 4. Использование функций. Ваша программа
# не должна быть линейной

def read_file(filename):
    with open(filename, 'r') as data:
        data_array = []
        for line in data:
            item = line.replace('\n', '').split(sep = ',')
            data_array.append(item)
    return data_array

def write_file(filename, data_array):
    with open(filename, 'w') as data:
        for i in data_array:
            write_element = ', '.join(i)
            data.write(f'{write_element}\n')



def add_item(filename, id = '', lastname = '', firstname = '', secondname = '', phone = ''):
    data_array = read_file(filename)
    max_id = 0
    for i in range(1,len(data_array)):
        if max_id < int(data_array[i][0]): max_id = int(data_array[i][0])
    next_ad = max_id + 1
    lastname = input('Фамилия: ')
    firstname = input('Имя: ')
    secondname = input('Отечество: ')
    phone = input('Телефон: ')
    new_item = []
    new_item.append(str(next_ad))
    new_item.append(lastname)
    new_item.append(firstname)
    new_item.append(secondname)
    new_item.append(phone)
    data_array.append(new_item)
    write_file(filename, data_array)

def show_all_items(filename):
    data_array = read_file(filename)
    for i in range(1,len(data_array)):
        print("ID:", data_array[i][0],  "Фамилия:", data_array[i][1], "Имя:", data_array[i][2], "Отечество:", data_array[i][3], "Телефон:", data_array[i][4],)

def menu():
    print("Добро пожаловать в телефонный справочник!")
    print("1 - Показать все записи")
    print("2 - Добавить запись")
    user_operation = int(input())

    if user_operation == 1:
        show_all_items(filename)
    elif user_operation == 2:
        add_item(filename)



filename = "file.txt"
menu()