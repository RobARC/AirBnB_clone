#!/usr/bin/python3
"""
Unit Test for State Class
"""
import unittest
from datetime import datetime
from models.state import State
import json

class TestStateDocs(unittest.TestCase):
    """Class for testing State docs"""

    @classmethod
    def setUpClass(cls):
        print('\n\n.................................')
        print('..... Testing Documentation .....')
        print('........   State Class   ........')
        print('.................................\n\n')

    def test_doc_file(self):
        """... documentation for the file"""
        expected = 'State class handles all application states' 
        actual = State.__doc__
        self.assertEqual(expected, actual)

    def test_doc_class(self):
        """... documentation for the class"""
        expected = 'State class handles all application states'
        actual = State.__doc__
        self.assertEqual(expected, actual)
