# 4. Преобразовать слова «разработка», «администрирование», «protocol», «standard» из строкового представления в байтовое
# и выполнить обратное преобразование (используя методы encode и decode).


def encode_byte(el):
    return el.encode('utf-8')


def decode_byte(el):
    return el.decode('utf-8')


def main():
    lst = ['разработка', 'администрирование', 'protocol', 'standard']
    lst_bit = []
    for el in lst:
        tmp = encode_byte(el)
        print(f'Слово:{tmp} тип {type(tmp)}')
        lst_bit.append(tmp)

    for el in lst_bit:
        tmp = decode_byte(el)
        print(f'Слово:{tmp} тип {type(tmp)}')


if __name__ == '__main__':
    main()
