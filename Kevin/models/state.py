#!/usr/bin/env python3
"""
Module that implements State class
"""
from base_model import BaseModel


class State(BaseModel):
    """
    State class that inherits from BaseModel
    """
    def __init__(self, *args, **kwargs):
       """
       Instantiation of State class
       """
       super().__init__(*args, **kwargs)
       self.name = ""
