# 2. Каждое из слов «class», «function», «method» записать в байтовом типе без преобразования в последовательность кодов
# (не используя методы encode и decode) и определить тип, содержимое и длину соответствующих переменных.


def str_type_len(el):
    return f'Слово:{el} тип:{type(el)} длинна:{len(el)}'


def main():
    srt_1 = b'class'
    srt_2 = b'function'
    srt_3 = b'method'

    lst = [srt_1, srt_2, srt_3]
    for el in lst:
        print(str_type_len(el))


if __name__ == '__main__':
    main()
