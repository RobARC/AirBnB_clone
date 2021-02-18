#!/user/bin/python3
"""
Unit Test for Review Class
"""
import unittest
from datetime import datetime
from models.review import Review
import json


class TestReviewDocs(unittest.TestCase):
    """Class for testing BaseModel docs"""

    @classmethod
    def setUpClass(cls):
        print('\n\n.................................')
        print('..... Testing Documentation .....')
        print('.......   Review  Class   .......')
        print('.................................\n\n')

    def test_doc_file(self):
        """... documentation for the file"""
        expected = 'Review class handles all application reviews'
        actual = Review.__doc__
        self.assertEqual(expected, actual)

    def test_doc_class(self):
        """... documentation for the class"""
        expected = 'Review class handles all application reviews'
        actual = Review.__doc__
        self.assertEqual(expected, actual)
