"""Программа-сервер"""

import socket
import sys
import json
from common.variables import ACTION_LIST, ACTION, ACCOUNT_NAME, RESPONSE, MAX_CONNECTIONS, \
    PRESENCE, TIME, USER, ERROR, DEFAULT_PORT, PROBE, MSG, QUIT, AUTHENTICATE, JOIN, LEAVE, LOG_SERVER
from common.utils import get_message, send_message
import log.server_log_config


def check_action(message):
    if (message[ACTION]) in ACTION_LIST:
        return True
    else:
        return False


def presence_message(message):
    LOG_SERVER.info(f'Добро пожаловать в наш чат {message[USER][ACCOUNT_NAME]} ')


def process_message(message):
    if message[ACTION] == PRESENCE:
        presence_message(message)
    elif message[ACTION] == PROBE:
        pass
    elif message[ACTION] == MSG:
        pass
    elif message[ACTION] == QUIT:
        pass
    elif message[ACTION] == AUTHENTICATE:
        pass
    elif message[ACTION] == JOIN:
        pass
    elif message[ACTION] == LEAVE:
        pass


def process_client_message(message):
    '''
    Обработчик сообщений от клиентов, принимает словарь -
    сообщение от клинта, проверяет корректность,
    возвращает словарь-ответ для клиента

    :param message:
    :return:
    '''
    if ACTION in message and check_action(message) and TIME in message \
            and USER in message and message[USER][ACCOUNT_NAME] == 'Guest':
        process_message(message)

        return {RESPONSE: 200}
    return {
        RESPONSE: 400,
        ERROR: 'Bad Request'
    }


def main():
    '''
    Загрузка параметров командной строки, если нет параметров, то задаём значения по умоланию.
    Сначала обрабатываем порт:
    server.py -p 8079 -a 192.168.0.100
    :return:
    '''

    try:
        if '-p' in sys.argv:
            listen_port = int(sys.argv[sys.argv.index('-p') + 1])
        else:
            listen_port = DEFAULT_PORT
        if listen_port < 1024 or listen_port > 65535:
            raise ValueError
    except IndexError:
        LOG_SERVER.critical('После параметра -\'p\' необходимо указать номер порта.')
        sys.exit(1)
    except ValueError:
        LOG_SERVER.critical(
            'В качастве порта может быть указано только число в диапазоне от 1024 до 65535.')
        sys.exit(1)

    # Затем загружаем какой адрес слушать

    try:
        if '-a' in sys.argv:
            listen_address = sys.argv[sys.argv.index('-a') + 1]
        else:
            listen_address = ''

    except IndexError:
        LOG_SERVER.critical(
            'После параметра \'a\'- необходимо указать адрес, который будет слушать сервер.')
        sys.exit(1)

    # Готовим сокет

    transport = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    transport.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    transport.bind((listen_address, listen_port))

    # Слушаем порт

    transport.listen(MAX_CONNECTIONS)

    while True:
        client, client_address = transport.accept()
        try:
            message_from_cient = get_message(client)
            # print(message_from_cient)
            # {'action': 'presence', 'time': 1573760672.167031, 'user': {'account_name': 'Guest'}}
            response = process_client_message(message_from_cient)
            send_message(client, response)
            client.close()
        except (ValueError, json.JSONDecodeError):
            LOG_SERVER.error('Принято некорретное сообщение от клиента.')
            client.close()


if __name__ == '__main__':
    main()
