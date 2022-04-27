"""Лаунчер"""

import subprocess

PROCESS = []

while True:
    ACTION = input('Выберите действие: q - выход, '
                   's - запустить сервер и клиенты, x - закрыть все окна: ')

    if ACTION == 'q':
        break
    elif ACTION == 's':
        PROCESS.append(subprocess.Popen('python server.py -p 7777 -a 127.0.0.1',
                                        creationflags=subprocess.CREATE_NEW_CONSOLE))

        PROCESS.append(subprocess.Popen('python client.py 127.0.0.1 7777 presence',
                                        creationflags=subprocess.CREATE_NEW_CONSOLE)) # Выдает привествие

        PROCESS.append(subprocess.Popen('python client.py 127.0.0.1 7777 presece',
                                        creationflags=subprocess.CREATE_NEW_CONSOLE)) # Выдает ошибку!!!

    elif ACTION == 'x':
        while PROCESS:
            VICTIM = PROCESS.pop()
            VICTIM.kill()
