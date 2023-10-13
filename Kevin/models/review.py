#!/usr/bin/env python3
"""
This module contains the Review class.
"""
from base_model import BaseModel


class Review(BaseModel):
     """
     Class Review that inherits from BaseModel
     """
     def __init__(self, *args, **kwargs):
        """
        Class instantiation
        """
        super().__init__(*args, **kwargs)
        self.place_id = ""
        self.user_id = ""
        self.text = ""
