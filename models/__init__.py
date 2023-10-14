#!/usr/bin/python3
"""
Create a unique FileStorage instance for AirBnB.
"""
from models.engine import file_storage

storage = FileStorage()
storage.reload()
