#!/usr/bin/env python3
"""
Module that implements the Place class
"""
from base_model import BaseModel


class Place(BaseModel):
    """
    Class Place that inherits from BaseModel
    """
    def __init__(self, *args, **kwargs):
       """
       Class instantiation
       """
       super().__init__(*args, **kwargs)
       self.name = ""
       self.city_id = ""
       self.user_id = ""
       self.description = ""
       self.number_rooms = ""
       self.number_bathrooms = ""
       self.max_guest = 0
       self.price_by_night = 0
       self.latitude = 0.0
       self.longitude = 0.0
       self.amenity_ids = []
