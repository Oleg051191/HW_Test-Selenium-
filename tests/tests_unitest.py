import unittest
from selenium import webdriver
from unittest import mock
from main import *
from API_Yandex import Yandex, user_yandex
from Chrome.Selenium import authorization

class TestLibrary(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('Тесты класса запущены !')

    @classmethod
    def tearDownClass(cls):
        print('Тесты класса завершены !')

    def setUp(self):
        print('RUN Test !')

    def tearDown(self):
        print('END Test !')

    def test_check_document_existance(self):
        self.assertEqual(check_document_existance(user_doc_number='10006'), True)

    def test_get_doc_owner_name_eq(self):
        with unittest.mock.patch('builtins.input', return_value='10006'):
            self.assertEqual(get_doc_owner_name(), 'Аристарх Павлов')

    def test_get_doc_owner_name_not_eq(self):
        with unittest.mock.patch('builtins.input', return_value='10006'):
            self.assertNotEqual(get_doc_owner_name(), 'Геннадий Покемонов')


    def test_get_all_doc_owners_names(self):
        print('Name_test:', self.id())
        self.assertIsInstance(get_all_doc_owners_names(), list, 'This is SET !')

    def test_l_get_all_doc_owners_names(self):
        self.assertEqual(l_get_all_doc_owners_names(), 3, "Length of set = 3")

    def test_is_none_get_all_doc_owners_names(self):
        self.assertIsNotNone(get_all_doc_owners_names())

    def test_remove_doc_from_shelf(self):
        self.assertNotIn(remove_doc_from_shelf('11-2'), [])

    def test_add_new_shelf(self):
        with unittest.mock.patch('builtins.input', return_value='4'):
            self.assertTrue(add_new_shelf())

    def test_append_doc_to_shelf(self):
        print('Name_test:', self.id())
        self.assertIn(append_doc_to_shelf('3344', '2'), directories.values())

    def test_delete_doc(self):
        with unittest.mock.patch('builtins.input', return_value='10006'):
            self.assertTrue(delete_doc())

    def test_get_doc_shelf(self):
        with unittest.mock.patch('builtins.input', return_value='11-2'):
            self.assertEqual(get_doc_shelf(), '1')

    def test_move_doc_to_shelf(self):
        with unittest.mock.patch('builtins.input', return_value='11-2'):
            with unittest.mock.patch('builtins.input', return_value='3'):
                self.assertEqual(move_doc_to_shelf(), '3')

    def test_create_folder(self):
        self.assertEqual(user_yandex.create_folder('New_folder'), 201, 'This folder was create early !')

    @unittest.skip
    def test_was_create(self):
        self.assertEqual(user_yandex.create_folder('New_folder'), 409)

    def test_authorization_selenium(self):
        self.assertTrue(authorization(), 'https://passport.yandex.ru/profile')

