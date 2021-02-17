#!/usr/bin/python3
import os
import models
import unittest
from models.user import User
from time import sleep

class TestUser_instantiation(unittest.TestCase):
    """Unittests for instance of user class"""

    def test_no_args_instantiates(self):
        self.assertEqual(User, type(User()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(User(), models.storage.all().value())

    def test_id_is_public(self):
        self.assertEqual(datetime, type(User().created_at))

    def test_update_at_is_public_datetime(self):
        self.assertEqual(datetime, type(User().update_at))

    def test_email_is_public(self):
        self.assertEqual(str, type(User.email))

    def test_password_is_public(self):
        self.assertEqual(str, type(User.email))

    def test_first_name_is_public(self):
        self.assertEqual(str, type(User.first_name))

    def test_last_name_is_public(self):
        self.assertEqual(str, type(User.last_name))

    def test_two_users_not_same_id(self):
        ud1 = User()
        ud2 = User()
        self.assertNotEqual(ud1.id, ud2.id)
