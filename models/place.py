#!/usr/bin/python3
"""The ``place`` module
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """The Place class inherit from ``BaseModel``
    
    Args:
        city_id(str): The city id
        user_id(str): The user id
        name(str): The name of the place
        description(str): The description of the place
        number_rooms(int): The number of rooms
        number_bathrooms(int): The number of bathrooms
        max_guest(int): The max number of guest
        price_by_night(int): The price per night
        latitude(float): The latitude of the place
        longitude(float): The longitude of the place
        amenity_ids(list): The lists of amenity ids
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
