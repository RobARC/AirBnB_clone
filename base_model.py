#!/usr/bin/python3
"""module class BaseModel"""
from uuid import uuid4
import datetime 
import models


class BaseModel:
    """Class BaseModel"""

    def __init__(self, *args, **kwargs):
        """ method to initialize instance of class BaseModel"""
        
        if kwargs is not None and len(kwargs) is not 0:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                else:
                    if key == 'update_at' or key == 'created_at':
                        time = datetime.datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                        setattr(self, key, time)
                       
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.datetime.now()
            self.update_at = datetime.datetime.now()
            models.storage.new(self)

    def save(self):
        """ updates the public instance attribute updated_at
        with the current datetime"""
        self.update_at = datetime.datetime.now()
        models.storage.save()


    def to_dict(self):
        """returns a dictionary containing all keys/values of
        __dict__ of the instance"""
        new = {}
        mydict = self.__dict__
        for key in mydict:
            if key is 'created_at' or key is 'update_at':
                mydict[key] = datetime.datetime.now()
                new[key] = mydict[key].isoformat()
            else:
                new[key] = mydict[key]
        new['__class__'] = self.__class__.__name__
        return new

    def __str__(self):
        """ should print: [<class name>] (<self.id>) <self.__dict__>"""
        clsname = type(self).__name__
        return "[{}] ({}) ({})".format(clsname, self.id, self.__dict__)
