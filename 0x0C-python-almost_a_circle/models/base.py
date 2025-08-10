#!/usr/bin/python3
class Base:
    __nb_objects = 0
    def __init__(self, id=None):
        if id:
            self.id = id
        else:
            self.id = Base.__nb_objects + 1
            Base.__nb_objects += 1
