"""Константы"""
import logging


"""Настройки логера"""

LOG_CLIENT = logging.getLogger('client')
LOG_SERVER = logging.getLogger('server')
FORMATTER = logging.Formatter("%(asctime)-15s  %(levelname)-10s %(module)-20s %(funcName)-20s  %(message)s")
DEFAULT_LEVEL = logging.INFO

# Порт по умолчанию для сетевого ваимодействия
DEFAULT_PORT = 7777
# IP адрес по умолчанию для подключения клиента
DEFAULT_IP_ADDRESS = '127.0.0.1'
# Максимальная очередь подключений
MAX_CONNECTIONS = 5
# Максимальная длинна сообщения в байтах
MAX_PACKAGE_LENGTH = 1024
# Кодировка проекта
ENCODING = 'utf-8'

# Прококол JIM основные ключи:
ACTION_LIST = ['presence', 'prоbe', 'msg', 'quit', 'authenticate', 'join', 'leave']
ACTION = 'action'
TIME = 'time'
USER = 'user'
ACCOUNT_NAME = 'account_name'
SENDER = 'sender'
MESSAGE = 'message'
MESSAGE_TEXT = 'mess_text'

# Прочие ключи, используемые в протоколе

PRESENCE = 'presence'
PROBE = 'prоbe'
MSG = 'msg'
QUIT = 'quit'
AUTHENTICATE = 'authenticate'
JOIN = 'join'
LEAVE = 'leave'

RESPONSE = 'response'
ERROR = 'error'

