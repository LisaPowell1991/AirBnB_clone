#!/usr/bin/env python3
"""
Module for User class
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    Class User that inherits from BaseModel
    """
    def __init__(self, *args, **kwargs):
       """
       Instantiation of User Class
       """
       super().__init__(*args, **kwargs)
       self.email = ""
       self.password = ""
       self.first_name = ""
       self.last_name = ""