#!/usr/bin/env python3
"""
Module that implements City Class
"""
from base_model import BaseModel


class City(BaseModel):
    """
    City class that inherits from BaseModel
    """
    def __init__(self, *args, **kwargs):
       """
       Instantiation of City class
       """
       super().__init__(*args, **kwargs)
       self.state_id = ""
       self.name = ""
