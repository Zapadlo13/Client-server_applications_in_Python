import logging
import os
from common.variables import FORMATTER, DEFAULT_LEVEL

MAX_BACKUP_COUNT = 100

PATH = os.path.dirname(os.path.abspath(__file__))
PATH = os.path.join(PATH, 'client.log')

Handler = logging.FileHandler(PATH, encoding='utf8')
Handler.setFormatter(FORMATTER)

logger = logging.getLogger('client')
logger.addHandler(Handler)
logger.setLevel(DEFAULT_LEVEL)


def test_log():
    logger.debug('test debug')
    logger.info('test info')
    logger.warning('test warning')
    logger.error('test error')
    logger.critical('test critical')


if __name__ == '__main__':
    test_log()
