#!/usr/bin/pyhton3
"""
Unit Test for amenity file
"""

import unittest
from models.amenity import Amenity
import models
import json

class TestAmenityDocs(unittest.TestCase):
    """Class testing for Amenity"""

    @classmethod
    def setUpClass(cls):
        print('\n\n.............................')
        print('..... Testing Documentation .....')
        print('.....  For  Amenity Class  .....')
        print('.............................\n\n')

    def test_doc_class(self):
        """...documentation for de class"""
        expected = '\nAmenity Class from Models Module\n'
        actual = models.amenity.__doc__
        self.assertEqual(expected, actual)

    def test_doc_class(self):
        """... documentation for the class"""
        expected = 'Amenity class handles all application amenities'
        actual = Amenity.__doc__
        self.assertEqual(expected, actual)
