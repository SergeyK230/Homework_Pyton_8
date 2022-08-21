def vibor():
    return input('1. Создать новый список\n2. Добавить нового ученика\n3. Удалить ученика\n\
4. Вывести список учеников\n5. Вывести схему класса\n6. Поиск по параметру\n-> ')

def vvod_student(par):
    return input(f'Введите {par} -> ')

def delete_vvod(par):
    return input(f'Введите {par} -> ')


def delete_vibor():
    return input('1. Удаление по id\n2. Удаление по фамилии\n-> ')

def find_vibor():
    return input('1. Поиск по фамилии\n2. Поиск по имени\n3. Поиск по году рождения\n\
4. Поиск по классу\n5. Поиск месту в классе\n6. Поиск по успеваимости\n7. Поиск по id\n-> ')

def find_vvod(par):
    return input(f'Введите {par} -> ')