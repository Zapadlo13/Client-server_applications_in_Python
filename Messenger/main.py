"""Лаунчер"""

import subprocess

PROCESS = []

while True:
    ACTION = input('Выберите действие: q - выход, '
                   's - запустить сервер c- запустить клиенты, x - закрыть все окна: ')

    if ACTION == 'q':
        break
    elif ACTION == 's':
        PROCESS.append(subprocess.Popen('python server.py',
                                        creationflags=subprocess.CREATE_NEW_CONSOLE))
    elif ACTION == 'c':
        PROCESS.append(subprocess.Popen('python client.py -m listen',
                                        creationflags=subprocess.CREATE_NEW_CONSOLE))  # Слушаем

        PROCESS.append(subprocess.Popen('python client.py -m send',
                                        creationflags=subprocess.CREATE_NEW_CONSOLE))  # Говорит


    elif ACTION == 'x':
        while PROCESS:
            VICTIM = PROCESS.pop()
            VICTIM.kill()
