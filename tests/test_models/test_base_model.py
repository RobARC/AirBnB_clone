#!/usr/bin/pyhton3
"""
Unit Test for BaseModel Class
"""
from models.base_model import BaseModel
import unittest
import datetime
import models
import json
from models.engine.file_storage import FileStorage
import os

BaseModel = models.base_model.BaseModel

class TestBaseModelDocs(unittest.TestCase):
    """Class for testtin BaseModel docs"""

    @classmethod
    def setUpClass(cls):
        print('\n\n.............................')
        print('..... Testing Documentation .....')
        print('.....  For BaseModel Class  .....')
        print('.............................\n\n')

    def test_doc_class(self):
        """...documentation for de class"""
        expected = 'Class BaseModel'
        actual = BaseModel.__doc__
        self.assertEqual(expected, actual)

    def test_doc_file(self):
        """... documentation for the file"""
        expected = 'module class BaseModel'
        actual = models.base_model.__doc__
        self.assertEqual(expected, actual)

    def test_doc_init(self):
        """... documentation for init function"""
        expected = ' method to initialize instance of class BaseModel'
        actual = BaseModel.__init__.__doc__
        self.assertEqual(expected, actual)

    def test_doc_save(self):
        """... documentation for save function"""
        expected =  'attribute updated_at with the current datetime'
        actual = BaseModel.save.__doc__
        self.assertEqual(expected, actual)

    def test_doc_to_dict(self):
        """... documentation for to_json function"""
        expected = 'returns a dictionary containing all keys/values of __dict__'
        actual = BaseModel.to_dict.__doc__
        self.assertEqual(expected, actual)

    def test_doc_str(self):
        """... documentation for to str function"""
        expected = 'should print: [<class name>] (<self.id>) <self.__dict__>'
        actual = BaseModel.__str__.__doc__
        self.assertEqual(expected, actual)

class TestBaseModelInstances(unittest.TestCase):
    """testing for class instances"""

    @classmethod
    def setUpClass(cls):
        print('\n\n.................................')
        print('....... Testing Functions .......')
        print('.....  For BaseModel Class  .....')
        print('.................................\n\n')
    
    def setUp(self):
        """initializes new BaseModel instance for testing"""
        self.model = BaseModel()

    def test_instantiation(self):
        """... checks if BaseModel is properly instantiated"""
        self.assertIsInstance(self.model, BaseModel)
    
    def test_to_string(self):
        """... checks if BaseModel is properly casted to string"""
        my_str = str(self.model)
        my_list = ['BaseModel', 'id', 'created_at']
        actual = 0
        for sub_str in my_list:
            if sub_str in my_str:
                actual += 1
        self.assertTrue(3 == actual)

    def test_instantiation_no_updated(self):
        """... should not have updated attribute"""
        my_str = str(self.model)
        actual = 0
        if 'updated_at' in my_str:
            actual += 1
        self.assertTrue(0 == actual)

    def test_dict_class(self):
        """... to_dict should include class key with value BaseModel"""
        my_model_dict = self.model.to_dict()
        actual = None
        if my_model_dict['__class__']:
            actual = my_model_dict['__class__']
        expected = 'BaseModel'
        self.assertEqual(expected, actual)

    def test_name_attribute(self):
        """... add name attribute"""
        self.model.name = "Holberton"
        actual = self.model.name
        expected = "Holberton"
        self.assertEqual(expected, actual)

    def test_number_attribute(self):
        """... add number attribute"""
        self.model.number = 98
        actual = self.model.number
        self.assertTrue(98 == actual)

if __name__ == '__main__':
    unittest.main

    





