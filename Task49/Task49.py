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

def open_file(filename):
    print("Файл найден!")
def add_item(filename, id, lastname, firstname, secondname, phone):
    print("Запись добавлена!")
def show_all_items(filename):
    with open(filename, 'r') as data:
        for line in data:
            item = line.split(sep = ",")
            print("ID: ", line[0], "Фамилия: ", line[1], "Имя: ", line[2], "Отечество: ", line[3], "Телефон: ", line[4],)

def menu():
    print("Добро пожаловать в телефонный справочник!")
    print("1 - Показать все записи")
    print("2 - Добавить запись")
    user_operation = int(input())

    if user_operation == 1:
        show_all_items(filename)


filename = "file.txt"
menu()