# 1. Каждое из слов «разработка», «сокет», «декоратор» представить в строковом формате и проверить тип и содержание соответствующих переменных.
# Затем с помощью онлайн-конвертера преобразовать строковые представление в формат Unicode и также проверить тип и содержимое переменных.


def encode_list(lst):
    lst_uni = []
    for el in lst:
        lst_uni.append(el.encode('unicode-escape').decode())
    return lst_uni


def main():
    lst = ['разработка', 'сокет', 'декоратор']

    lst_uni = encode_list(lst)
    for el in lst_uni:
        print(el, type(el))


if __name__ == '__main__':
    main()
