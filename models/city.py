#!/usr/bin/python3
"""
City Class from Models Module
"""

from models.base_models import BaseModel


class City(BaseModel):
    """City class handles all application cities"""

    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """instatiates a new city"""
        super().__init__(self, *args, **kwargs)
