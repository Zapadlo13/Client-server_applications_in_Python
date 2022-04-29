import logging
import os
from logging.handlers import TimedRotatingFileHandler
from common.variables import FORMATTER, DEFAULT_LEVEL

PATH = os.path.dirname(os.path.abspath(__file__))
PATH = os.path.join(PATH, 'server.log')

fileHandle = logging.handlers.TimedRotatingFileHandler(PATH, encoding='utf8', interval=100, when='D', backupCount=1000)

fileHandle.setFormatter(FORMATTER)
fileHandle.doRollover()

logger = logging.getLogger('server')
logger.addHandler(fileHandle)
logger.setLevel(DEFAULT_LEVEL)


def test_log():
    logger.debug('test debug')
    logger.info('test info')
    logger.warning('test warning')
    logger.error('test error')
    logger.critical('test critical')


if __name__ == '__main__':
    test_log()
