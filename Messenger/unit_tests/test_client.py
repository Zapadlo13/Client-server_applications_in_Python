import unittest
import sys
import os

sys.path.append(os.path.join(os.getcwd(), '..'))
from common.variables import RESPONSE, ERROR, USER, ACCOUNT_NAME, TIME, ACTION, PRESENCE, ENCODING
from client import create_presence, process_ans
import time


class Test_Client(unittest.TestCase):
    TIME_ = time.time()
    ACCOUNT_NAME_ = 'Guest'
    ACCOUNT_NAME2 = 'Guest123456'

    test_dict_send = {
        ACTION: PRESENCE,
        TIME: TIME_,
        USER: {
            ACCOUNT_NAME: ACCOUNT_NAME_
        }
    }
    test_dict_send_user = {
        ACTION: PRESENCE,
        TIME: TIME_,
        USER: {
            ACCOUNT_NAME: ACCOUNT_NAME2
        }
    }

    RESPONSE200 = {RESPONSE: 200}
    RESPONSE400 = {RESPONSE: 400, ERROR: 'Bad Request'}


    '''create_presence'''

    def test_create_presence(self):
        '''Тест создания запроса'''
        test_send = create_presence()
        test_send[TIME] = self.TIME_

        self.assertEqual(test_send, self.test_dict_send)

    def test_create_presence_user(self):
        '''Тест создания запроса с указанеи пользователя'''
        test_send = create_presence(self.ACCOUNT_NAME2)
        test_send[TIME] = self.TIME_

        self.assertEqual(test_send, self.test_dict_send_user)

    '''process_ans'''

    def test_process_ans_200(self):
        '''Тест 200 ответа'''
        self.assertEqual(process_ans(self.RESPONSE200), '200 : OK')

    def test_process_ans_400(self):
        '''Тест 400 ответа'''
        self.assertEqual(process_ans(self.RESPONSE400),  '400 : Bad Request')

    def test_process_ans_no_response(self):
        '''Тест 400 ответа'''
        self.assertEqual(process_ans(self.RESPONSE400),  '400 : Bad Request')