#5. Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать результаты из байтовового в строковый тип на кириллице.

import subprocess
import chardet

def ping(resource):
    args = ['ping', resource]
    subproc_ping = subprocess.Popen(args, stdout=subprocess.PIPE)
    for line in subproc_ping.stdout:
        line = line.decode( chardet.detect(line)['encoding']).encode('utf-8')
        print(line.decode('utf-8'))


ping('yandex.ru')
ping('youtube.co')