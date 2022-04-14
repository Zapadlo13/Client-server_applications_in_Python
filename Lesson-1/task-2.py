# 2. Каждое из слов «class», «function», «method» записать в байтовом типе без преобразования в последовательность кодов
# (не используя методы encode и decode) и определить тип, содержимое и длину соответствующих переменных.

srt_1 = b'class'
srt_2 = b'function'
srt_3 = b'method'

lst = [srt_1, srt_2, srt_3]

for el in lst:
    print(f'Слово:{el} тип:{type(el)} длинна:{len(el)}')
