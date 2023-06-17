from peewee import *
from setup import settings
from abc import ABC, abstractmethod, ABCMeta


db = SqliteDatabase(settings["db_link"])


class AbstractModel(ABC):
    __metaclass__ = ABCMeta

    @abstractmethod
    def save(self): pass

    @abstractmethod
    def delete(self): pass

    @abstractmethod
    def get(self): pass

    @abstractmethod
    def update(self): pass


class InsertDataException(Exception):

    def __init__(self):
        return super().__init__("Something went wrong in process of adding data")


class MetaClass(type(Model), type(AbstractModel)): pass


class BaseModel(Model, AbstractModel, metaclass=MetaClass):

    class Meta:
        database = db

    