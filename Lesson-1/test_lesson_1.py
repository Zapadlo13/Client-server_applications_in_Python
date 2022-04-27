import filecmp
import os
import unittest
from task_1 import encode_list
from task_2 import str_type_len
from task_3 import get_byte_type
from task_4 import encode_byte, decode_byte

from task_6 import createfile, getencoding, encoding_convert


class Test_Lesson1(unittest.TestCase):
    filename_task6 = 'test_file6.txt'
    filename_task6_convert = 'test_file6_convert.txt'

    def test_task1(self):
        lst = ['разработка', 'сокет', 'декоратор']
        lst_result = ['\\u0440\\u0430\\u0437\\u0440\\u0430\\u0431\\u043e\\u0442\\u043a\\u0430',
                      '\\u0441\\u043e\\u043a\\u0435\\u0442',
                      '\\u0434\\u0435\\u043a\\u043e\\u0440\\u0430\\u0442\\u043e\\u0440']
        lst_uni = encode_list(lst)
        self.assertEqual(lst_uni, lst_result)

    def test_task2(self):
        self.assertEqual(str_type_len(b'class'), f"Слово:b'class' тип:<class 'bytes'> длинна:5")

    def test_task3_byte(self):
        self.assertEqual(get_byte_type('attribute'), b'attribute')

    def test_task3_no_byte(self):
        self.assertEqual(get_byte_type('класс'), 'класс нельзя записать в байтовом виде')

    def test_task4_encode(self):
        self.assertEqual(encode_byte('разработка'),
                         b'\xd1\x80\xd0\xb0\xd0\xb7\xd1\x80\xd0\xb0\xd0\xb1\xd0\xbe\xd1\x82\xd0\xba\xd0\xb0')

    def test_task4_decode(self):
        self.assertEqual(
            decode_byte(b'\xd1\x80\xd0\xb0\xd0\xb7\xd1\x80\xd0\xb0\xd0\xb1\xd0\xbe\xd1\x82\xd0\xba\xd0\xb0'),
            'разработка')

    def test_task6_createfile(self):
        '''сравнение файлов'''
        lst = ['сетевое программирование', 'сокет', 'декоратор']

        createfile(self.filename_task6, lst)
        self.assertTrue(filecmp.cmp(self.filename_task6, 'test_file_task_6.txt', shallow=False))

    def test_task6_getencoding(self):
        lst = ['сетевое программирование', 'сокет', 'декоратор']

        createfile(self.filename_task6, lst)
        self.assertEqual(getencoding(self.filename_task6), 'windows-1251')

    def test_task6_encoding_convert(self):
        lst = ['сетевое программирование', 'сокет', 'декоратор']

        createfile(self.filename_task6_convert, lst)
        encoding = getencoding(self.filename_task6_convert)
        encoding_convert(self.filename_task6_convert, encoding)

        self.assertTrue(filecmp.cmp(self.filename_task6_convert, 'test_file_utf8.txt', shallow=False))

    def tearDown(self):
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), self.filename_task6)
        if (os.path.isfile(path)):
            os.remove(path)

        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), self.filename_task6_convert)
        if (os.path.isfile(path)):
            os.remove(path)
