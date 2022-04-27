import unittest
import sys
import os

sys.path.append(os.path.join(os.getcwd(), '..'))
from common.variables import RESPONSE, ERROR, USER, ACCOUNT_NAME, TIME, ACTION, PRESENCE, ENCODING
from server import process_client_message,process_message

import time


class Test_Server(unittest.TestCase):

    err_dict = {
        RESPONSE: 400,
        ERROR: 'Bad Request'
    }
    ok_dict = {RESPONSE: 200}

    TIME = time.time()
    ACCOUNT_NAME =  'Guest'
    WRONG_ACCOUNT_NAME = 'Guest123456'

    """process_client_message"""

    def test_wrong_action(self):
        """Ошибка если токого действия нету"""
        self.assertEqual(process_client_message(
            {ACTION: 'MSG', TIME: self.TIME, USER: {ACCOUNT_NAME: self.ACCOUNT_NAME}}), self.err_dict)
        self.assertEqual(process_client_message(
            {ACTION: 'Presence', TIME: self.TIME, USER: {ACCOUNT_NAME: self.ACCOUNT_NAME}}), self.err_dict)

    def test_no_action(self):
        """Ошибка если нет действия"""
        self.assertEqual(process_client_message(
            {TIME: self.TIME, USER: {ACCOUNT_NAME: self.ACCOUNT_NAME}}), self.err_dict)

    def test_no_time(self):
        """Ошибка если нет времени"""
        self.assertEqual(process_client_message(
            {ACTION: PRESENCE, USER: {ACCOUNT_NAME: self.ACCOUNT_NAME}}), self.err_dict)

    def test_no_user(self):
        """Ошибка если нет пользователя"""
        self.assertEqual(process_client_message(
            {ACTION: PRESENCE, TIME: self.TIME }), self.err_dict)

    def test_wrong_user(self):
        """Ошибка если нет пользователя"""
        self.assertEqual(process_client_message(
            {ACTION: PRESENCE, TIME: self.TIME, USER: {ACCOUNT_NAME: self.WRONG_ACCOUNT_NAME}}), self.err_dict)

    def test_ok_check(self):
        """Корректный запрос"""
        self.assertEqual(process_client_message(
            {ACTION: PRESENCE, TIME:self.TIME, USER: {ACCOUNT_NAME: self.ACCOUNT_NAME}}), self.ok_dict)


if __name__ == '__main__':
    unittest.main()
