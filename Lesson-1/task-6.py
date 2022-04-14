# 6. Создать текстовый файл test_file.txt, заполнить его тремя строками: «сетевое программирование», «сокет», «декоратор».
# Проверить кодировку файла по умолчанию. Принудительно открыть файл в формате Unicode и вывести его содержимое.


def createfile(filename, lst):
    with open(filename, 'w') as f:
        for el in lst:
            f.write(f'{el}\n')


def getencoding(filename):
    from chardet.universaldetector import UniversalDetector

    detector = UniversalDetector()
    with open(filename, 'rb') as f:
        for line in f:
            detector.feed(line)
            if detector.done:
                break
        detector.close()
    return detector.result['encoding']


def encoding_convert(filename, encoding):
    with open(filename, 'rb') as f:
        textfile = f.read()

    text = textfile.decode(encoding)
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(text)


def readfile(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            print(line)


lst = ['сетевое программирование', 'сокет', 'декоратор']
filename = 'test_file.txt'

createfile(filename, lst)
encoding = getencoding(filename)
print(f'Кодировка файла:{encoding}')
if encoding != 'utf-8':
    encoding_convert(filename,encoding)

encoding = getencoding(filename)
print(f'Кодировка файла:{encoding}')
readfile(filename)
