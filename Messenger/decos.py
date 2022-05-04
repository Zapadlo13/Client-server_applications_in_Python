import sys
import logging
import traceback
import inspect

if sys.argv[0].find('client') == -1:
    LOG_FILE = logging.getLogger('server')
else:
    LOG_FILE = logging.getLogger('client')


def log(func):
    def wrap(*args, **kwargs):
        ret = func(*args, **kwargs)
        LOG_FILE.info(f'Функция {func.__name__} ({args}, {kwargs}). '
                      f' {func.__module__} /  {traceback.format_stack()[0].strip().split()[-1]}'
                      f' Вызов из функции {inspect.stack()[1][3]}')
        return ret

    return wrap
