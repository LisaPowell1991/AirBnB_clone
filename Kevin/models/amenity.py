#!/usr/bin/env python3
"""
Module that implements the Amenity class
"""
from base_model import BaseModel


class Amenity(BaseModel):
    """
    Amenity class that inherits from BaseModel
    """
    def __init__(self, *args, **kwargs):
       """
       Instantiation of Amenity class
       """
       super().__init__(*args, **kwargs)
       self.name = ""
