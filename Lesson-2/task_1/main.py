"""
1. Задание на закрепление знаний по модулю CSV. Написать скрипт,
осуществляющий выборку определенных данных из файлов info_1.txt, info_2.txt,
info_3.txt и формирующий новый «отчетный» файл в формате CSV.

Для этого:

Создать функцию get_data(), в которой в цикле осуществляется перебор файлов
с данными, их открытие и считывание данных. В этой функции из считанных данных
необходимо с помощью регулярных выражений или другого инструмента извлечь значения параметров
«Изготовитель системы», «Название ОС», «Код продукта», «Тип системы».
Значения каждого параметра поместить в соответствующий список. Должно
получиться четыре списка — например, os_prod_list, os_name_list,
os_code_list, os_type_list. В этой же функции создать главный список
для хранения данных отчета — например, main_data — и поместить в него
названия столбцов отчета в виде списка: «Изготовитель системы»,
«Название ОС», «Код продукта», «Тип системы». Значения для этих
столбцов также оформить в виде списка и поместить в файл main_data
(также для каждого файла);

Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл.
В этой функции реализовать получение данных через вызов функции get_data(),
а также сохранение подготовленных данных в соответствующий CSV-файл;

Пример того, что должно получиться:

Изготовитель системы,Название ОС,Код продукта,Тип системы

1,LENOVO,Windows 7,00971-OEM-1982661-00231,x64-based

2,ACER,Windows 10,00971-OEM-1982661-00231,x64-based

3,DELL,Windows 8.1,00971-OEM-1982661-00231,x86-based

Обязательно проверьте, что у вас получается примерно то же самое.

ПРОШУ ВАС НЕ УДАЛЯТЬ СЛУЖЕБНЫЕ ФАЙЛЫ TXT И ИТОГОВЫЙ ФАЙЛ CSV!!!
"""

import csv
import os


def get_files(format=''):
    return [f for f in os.listdir() if f.lower().endswith(format)]


def get_header(row):
    return row[0].split(':')[0]


def get_value(row):
    return ' '.join(row[0].split(':')[1].split())


def get_data(headers):
    files = get_files('.txt')
    data = []
    for file in files:
        dict_row = {}
        with open(file) as f_n:
            f_n_reader = csv.reader(f_n)
            for row in f_n_reader:
                header = get_header(row)
                if header in headers:
                    dict_row[header] = get_value(row)

        data.append(dict_row)

    return data


def write_to_csv(headers, data):
    with open('task-1.csv', 'w', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(headers)

        for row in data:
            writer.writerow([row['Изготовитель системы'], row['Название ОС'], row['Код продукта'], row['Тип системы']])


headers = ['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']

data = get_data(headers)
write_to_csv(headers, data)
