"""Программа-клиент"""

import log.client_log_config
import sys
import json
import socket
import time

from common.variables import ACTION, PRESENCE, TIME, USER, ACCOUNT_NAME, \
    RESPONSE, ERROR, DEFAULT_IP_ADDRESS, DEFAULT_PORT, PROBE, MSG, QUIT, AUTHENTICATE, JOIN, LEAVE,LOG_CLIENT
from common.utils import get_message, send_message



def create_presence(account_name='Guest'):
    '''
    Функция генерирует запрос о присутствии клиента
    :param account_name:
    :return:
    '''
    # {'action': 'presence', 'time': 1573760672.167031, 'user': {'account_name': 'Guest'}}
    out = {
        ACTION: PRESENCE,
        TIME: time.time(),
        USER: {
            ACCOUNT_NAME: account_name
        }
    }
    return out


def process_ans(message):
    '''
    Функция разбирает ответ сервера
    :param message:
    :return:
    '''
    if RESPONSE in message:
        if message[RESPONSE] == 200:
            return '200 : OK'
        return f'400 : {message[ERROR]}'
    raise ValueError


def main():

    '''Загружаем параметы коммандной строки'''
    # client.py 192.168.0.100 8079
    try:
        server_address = sys.argv[1]
        server_port = int(sys.argv[2])
        message = sys.argv[3]
        if server_port < 1024 or server_port > 65535:
            raise ValueError
    except IndexError:
        server_address = DEFAULT_IP_ADDRESS
        server_port = DEFAULT_PORT
        LOG_CLIENT.error('Не указан порт подключения')
    except ValueError:
        LOG_CLIENT.critical('В качестве порта может быть указано только число в диапазоне от 1024 до 65535.')
        sys.exit(1)

    # Инициализация сокета и обмен

    transport = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    transport.connect((server_address, server_port))

    if message == PRESENCE:
        message_to_server = create_presence()
    elif message == PROBE:
        pass
    elif message == MSG:
        pass
    elif message == QUIT:
        pass
    elif message == AUTHENTICATE:
        pass
    elif message == JOIN:
        pass
    elif message == LEAVE:
        pass

    send_message(transport, message_to_server)

    try:
        answer = process_ans(get_message(transport))
        print(answer)
        if '200' in  answer:
            LOG_CLIENT.info(f'Сообщение прошло успешно')
        else:
            LOG_CLIENT.error(f'В сообщении есть ошибки: {answer}')

    except (ValueError, json.JSONDecodeError):
        LOG_CLIENT.error('Не удалось декодировать сообщение сервера.')


if __name__ == '__main__':
    main()
