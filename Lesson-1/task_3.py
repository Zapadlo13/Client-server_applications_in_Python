# 3. Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в байтовом типе.

def get_byte_type(el):
    try:
        return bytes(el, 'ascii')
    except:
        return f'{el} нельзя записать в байтовом виде'

def main():
    lst = ['attribute', 'класс', 'функция', 'type']

    for el in lst:
        print(get_byte_type(el))

if __name__ == '__main__':
    main()
