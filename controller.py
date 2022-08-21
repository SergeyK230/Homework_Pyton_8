import input_data as id
import func
import pandas as pd
import output_data as od
import data_keeper as dk

def start():
    match id.vibor():
        case '1':
            func.add_new_spisok()
        case '2':
            func.add_new_student(pd.read_csv('E:/Документы/GeekBrains/Знакомство c Python/homework_8/students_data.csv'))
        case '3':
            func.delite_student()
        case '4':
            od.vivod(pd.read_csv('E:/Документы/GeekBrains/Знакомство c Python/homework_8/students_data.csv'))
        case '5':
            od.vivod(dk.raspologenie_part)
        case '6':
            func.find_student()