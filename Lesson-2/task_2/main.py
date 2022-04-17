"""
2. Задание на закрепление знаний по модулю json. Есть файл orders
в формате JSON с информацией о заказах. Написать скрипт, автоматизирующий
его заполнение данными.

Для этого:
Создать функцию write_order_to_json(), в которую передается
5 параметров — товар (item), количество (quantity), цена (price),
покупатель (buyer), дата (date). Функция должна предусматривать запись
данных в виде словаря в файл orders.json. При записи данных указать
величину отступа в 4 пробельных символа;
Проверить работу программы через вызов функции write_order_to_json()
с передачей в нее значений каждого параметра.

ПРОШУ ВАС НЕ УДАЛЯТЬ ИСХОДНЫЙ JSON-ФАЙЛ
ПРИМЕР ТОГО, ЧТО ДОЛЖНО ПОЛУЧИТЬСЯ

{
    "orders": [
        {
            "item": "printer",
            "quantity": "10",
            "price": "6700",
            "buyer": "Ivanov I.I.",
            "date": "24.09.2017"
        },
        {
            "item": "scaner",
            "quantity": "20",
            "price": "10000",
            "buyer": "Petrov P.P.",
            "date": "11.01.2018"
        }
    ]
}

вам нужно подгрузить JSON-объект
и достучаться до списка, который и нужно пополнять
а потом сохранять все в файл
"""

import json


def load_data_json():
    with open('orders.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data


def write_order_to_json(item, quantity, price, buyer, date):
    data = load_data_json()

    with open('orders.json', 'w', encoding='utf-8', ) as f:
        order_info = {'item': item, 'quantity': quantity, 'price': price, 'buyer': buyer, 'date': date}
        data['orders'].append(order_info)

        json.dump(data, f, indent=4, ensure_ascii=False)


write_order_to_json('computer', '1', '5000', 'Ivanov', '17.04.2022')
write_order_to_json('компьютер', '1', '15000', 'Петров', '17.04.2022')

write_order_to_json('printer', '1', '5000', 'Ivanov', '17.04.2022')
write_order_to_json('принтер', '1', '15000', 'Петров', '17.04.2022')
