#!/usr/bin/python3
"""
User Class from Models Module
"""

from models.base_model import BaseModel


class User(BaseModel):
    """User Class handles all application users"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """instance a new user"""
        super().__init__(self, *args, **kwargs)
