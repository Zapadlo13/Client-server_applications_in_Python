"""
3. Задание на закрепление знаний по модулю yaml.
 Написать скрипт, автоматизирующий сохранение данных
 в файле YAML-формата.
Для этого:

Подготовить данные для записи в виде словаря, в котором
первому ключу соответствует список, второму — целое число,
третьему — вложенный словарь, где значение каждого ключа —
это целое число с юникод-символом, отсутствующим в кодировке
ASCII(например, €);

Реализовать сохранение данных в файл формата YAML — например,
в файл file.yaml. При этом обеспечить стилизацию файла с помощью
параметра default_flow_style, а также установить возможность работы
с юникодом: allow_unicode = True;

Реализовать считывание данных из созданного файла и проверить,
совпадают ли они с исходными.
"""

import yaml

data = {'items': ['computer', 'printer', 'keyboard', 'mouse'],

           'items_ptice': {'computer': '200₽-1000₽',
                           'printer': '100¥-300¥',
                           'keyboard': '5€-50€',
                           'mouse': '4₿-7₿'},
        'items_quantity': 4
        }

with open('file_1.yaml', 'w', encoding='utf-8') as f:
    yaml.dump(data, f,default_flow_style=False)

with open("file_1.yaml", 'r', encoding='utf-8') as f:
    data_load = yaml.load(f, Loader=yaml.SafeLoader)

if data==data_load:
    print(f'Данные совпадают с исходными.')
else:
    print(f'Данные не совпадают с исходными.')