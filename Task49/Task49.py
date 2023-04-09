def read_file(filename):
    with open(filename, 'r') as data:
        data_array = []
        for line in data:
            item = line.replace('\n','').split(sep = ',')
            data_array.append(item)
    return data_array

def write_file(filename, data_array):
    with open(filename, 'w') as data:
        for i in data_array:
            write_element = ','.join(i)
            data.write((f'{write_element}\n'))

def add_write_elementtem(filename, lastname = '', firstname = '', secondname = '', phone = ''):
    data_array = read_file(filename) 
    max_id = 0
    for i in range(1,len(data_array)):
        if max_id < int(data_array[i][0]): 
            max_id = int(data_array[i][0])
    next_id = max_id + 1
    print(next_id)
    lastname = input('Фамилия: ')
    firstname = input('Имя: ')
    secondname = input('Отчество: ')
    phone = input('Телефон: ')
    new_item = []
    new_item.append(str(next_id))
    new_item.append(lastname)
    new_item.append(firstname)
    new_item.append(secondname)
    new_item.append(phone)
    print(new_item)
    print(data_array)
    data_array.append(new_item)
    print(data_array)
    write_file(filename, data_array)

def show_all_items(filename):
    data_array = read_file(filename)    
    for i in range(1,len(data_array)):
        print("ID: ", data_array[i][0], "Фамилия: ", data_array[i][1],"Имя: ", data_array[i][2], "Отчество: ", data_array[i][3], "Телефон: ", data_array[i][4])

# def search_ID(filename,id_user):
#     # id_user = input('Введите ID: ')
    
#     data_array = read_file(filename) 
#     for i in range(len(data_array)):
#         if data_array[i][0] == id_user:
#             print(*(data_array[i]))
#             break
#             return True
#     else:
#         False
        

def change_items(filename):
    data_array = read_file(filename)
    id_user = input('Введите ID: ')
    for i in range(len(data_array)):
        if data_array[i][0] == id_user:
            print(*(data_array[i]))
            break
    else:
        return print("Пользователь с таким ID не найден")
    print('Введите номер, данные которых вы хотите изменить')
    print(f'1 - Фамилия - {data_array[i][1]}')
    print(f'2 - Имя - {data_array[i][2]}')
    print(f'3 - Отечство - {data_array[i][3]}')
    print(f'4 - Телефон - {data_array[i][4]} ')
    user_operation2 = int(input())
    if user_operation2 == 1:
        data_array[i][1] = input("Введите новую фамилию: ")
    elif user_operation2 == 2: 
        data_array[i][2] = input("Введите новое имя: ")
    elif user_operation2 == 3:
       data_array[i][3] = input("Введите новое отчество: ")
    elif user_operation2 == 4:
       data_array[i][4] = input("Введите новый телефон: ")
    print(*(data_array[i]))
    write_file(filename, data_array)
    
def delete_user(filename):
    data_array = read_file(filename)
    id_user = input('Введите ID: ')
    for i in range(len(data_array)):
        if data_array[i][0] == id_user:
            print(*(data_array[i]))
            break
    else:
        return print("Пользователь с таким ID не найден") 
    del data_array[i]
    print("Пользователь удален")
    write_file(filename, data_array)


def menu():
    print('Добро пожаловать в телефонный справочник!')
    print('1 - Показать все записи')
    print('2 - Добавить запись')
    print('3 - Изменить запись')
    print('4 - Удалить запись')
    user_operation = int(input())

    if user_operation == 1:
        show_all_items(filename)
    elif user_operation == 2: 
        add_item(filename)
    elif user_operation == 3:
       change_items(filename)
    elif user_operation == 4:
        delete_user(filename) 



filename = 'file.txt'
menu()