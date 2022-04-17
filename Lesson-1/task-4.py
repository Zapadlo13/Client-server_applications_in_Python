#4. Преобразовать слова «разработка», «администрирование», «protocol», «standard» из строкового представления в байтовое
# и выполнить обратное преобразование (используя методы encode и decode).
lst = ['разработка', 'администрирование', 'protocol','standard']
lst_bit =[]
for el in lst:
    tmp = el.encode('utf-8')
    print(f'Слово:{tmp} тип {type(tmp)}')
    lst_bit.append(tmp)

for el in lst_bit:
    tmp = el.decode('utf-8')
    print(f'Слово:{tmp} тип {type(tmp)}')
