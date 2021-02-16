#!/usr/bin/python
"""
State Class from Models Module
"""


class State(BaseModel):
    """State class handles all application states"""

    name = ""

    def __init__(self, *args, **kwargs):
        """instantiates a new state"""
        super().__init__(self, *args, **kwargs)
