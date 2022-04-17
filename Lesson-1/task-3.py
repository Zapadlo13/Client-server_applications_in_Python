# 3. Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в байтовом типе.

lst = ['attribute', 'класс', 'функция', 'type']

for el in lst:
    try:
        print(bytes(el, 'ascii'))
    except:
        print(f'{el} нельзя записать в байтовом виде')
