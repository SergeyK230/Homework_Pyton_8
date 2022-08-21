import input_data as id
import data_keeper as dk
import pandas as pd
import output_data as od

def new_student():
    student_id = id.vvod_student('id')
    first_name = id.vvod_student('Имя')
    last_name = id.vvod_student('фамилию')
    second_name = id.vvod_student('отчество')
    birth_year = id.vvod_student('год рождения')
    class_number = id.vvod_student('номер класса и буква класса')
    od.vivod(dk.raspologenie_part)
    mesto = id.vvod_student('место в классе (смотреть в схеме класса)')
    status_ocenok = id.vvod_student('статус по оценкам')
    mem = {'id':student_id, 'Фамилия':last_name, 'Имя': first_name, 'Отчество': second_name, 'Год Рождения': birth_year,
        'Класс': class_number, 'Место в классе': mesto,'Статус по оценкам': status_ocenok}
    return mem

def add_new_student(par):
    par = par.append(new_student(), ignore_index=True)
    par.to_csv('E:/Документы/GeekBrains/Знакомство c Python/homework_8/students_data.csv', index=False)

def add_new_spisok():
    par = new_spisok()
    par = par.append(new_student(), ignore_index=True)
    par.to_csv('E:/Документы/GeekBrains/Знакомство c Python/homework_8/students_data.csv', index=False)

def new_spisok():
    return pd.DataFrame({'id': [], 'Фамилия':[], 'Имя': [], 'Отчество': [], 'Год Рождения': [], 'Класс': [],
                         'Место в классе': [],'Статус по оценкам': []})

def delite_student():
    match id.delete_vibor():
        case '1':
            mem = pd.read_csv('E:/Документы/GeekBrains/Знакомство c Python/homework_8/students_data.csv')
            mem = mem.set_index('id')
            mem.drop([id.delete_vvod('Личный идентификатор студента (id)')], axis=0, inplace=True)
            mem.to_csv('E:/Документы/GeekBrains/Знакомство c Python/homework_8/students_data.csv', index=False)
        case '2':
            mem = pd.read_csv('E:/Документы/GeekBrains/Знакомство c Python/homework_8/students_data.csv')
            mem = mem.set_index('Фамилия')
            mem.drop([id.delete_vvod('Фамилию')], axis=0, inplace=True)
            mem.to_csv('E:/Документы/GeekBrains/Знакомство c Python/homework_8/students_data.csv', index=True)

def find_student():
    mem = pd.read_csv('E:/Документы/GeekBrains/Знакомство c Python/homework_8/students_data.csv')
    match id.find_vibor():
        case '1':           
            od.vivod(mem.loc[mem['Фамилия'] == id.find_vvod("Фамилию")])
        case '2':
            od.vivod(mem.loc[mem['Имя'] == id.find_vvod("Имя")])
        case '3':
            od.vivod(mem.loc[mem['Год рождения'] == id.find_vvod("Год рождения")])
        case '4':
            od.vivod(mem.loc[mem['Класс'] == id.find_vvod("Номер и букву класса")])
        case '5':
            od.vivod(dk.raspologenie_part)
            od.vivod(mem.loc[mem['Место в классе'] == id.find_vvod("Номер и букву места")])
        case '6':
            od.vivod(mem.loc[mem['Статус по оценкам'] == id.find_vvod("Успеваимость")])
        case '7':
            od.vivod(mem.loc[mem['id'] == id.find_vvod("Личный идентификатор студента (id))")])
