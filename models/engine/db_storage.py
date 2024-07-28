#!/usr/bin/python3
"""This module defines a class to manage database storage for hbnb clone"""

from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity


class DBStorage:
    """This class manages storage of hbnb models in a MySQL database"""
    __engine = None
    __session = None

    def __init__(self):
        """Instantiates a new DBStorage object"""
        user = getenv('HBNB_MYSQL_USER')
        pwd = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        db = getenv('HBNB_MYSQL_DB')
        env = getenv('HBNB_ENV')

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(user, pwd, host, db),
                                      pool_pre_ping=True)

        if env == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Queries the current database session for all objects of the
        given class name"""
        obj_dict = {}
        if cls:
            objs = self.__session.query(cls).all()
            for obj in objs:
                key = obj.__class__.__name__ + '.' + obj.id
                obj_dict[key] = obj

        else:
            classes = [State, City, User, Place, Review, Amenity]
            for cls in classes:
                objs = self.__session.query(cls).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    obj_dict[key] = obj

        return obj_dict

    def new(self, obj):
        """Add an object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes to the database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete an object from the current database session"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """create all tables in the database and current database session"""
        Base.metadata.create_all(self.__engine)
        sess = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess)
        self.__session = Session()

    def close(self):
        """Closes the current database session"""
        self.__session.remove()
