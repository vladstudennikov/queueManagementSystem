from peewee import IntegrityError
from Model import AbstractModel
from Monitor import Monitor
from Admin import Admin
from Operator import Operator
from Workplace import Workplace
from Customer import Customer
from abc import ABC, abstractmethod
import Validators as v


class ModelAdder(ABC):

    @abstractmethod
    def add(self): pass


class ModelsRemover(ABC):

    @abstractmethod
    def delete(self): pass


class InvalidFieldsException(Exception):

    def __init__(self, user: object):
        listOfFields = user.__dict__.keys()
        res = "User that you want to add do not exist in database\nList of fields:\n"

        for i in listOfFields:
            if not i.startswith("__") and not i.startswith("_"):
                res += i + '\n'

        return super().__init__(res)


class InvalidClassException(Exception):

    def __init__(self):
        return super().__init__("User you want to add cannot be added: it was not found in the database or program cannot work with this class because class is not an instance of AbstractModel")


class IncorrectDataException(Exception):
    
    def __init__(self, d: dict):
        tmp = None
        for i in d:
            if d[i] == False:
                tmp = i
        return super().__init__(f"Invalid data for adding. Problem with {tmp}.")


class PeeweeModelAdder(ModelAdder):

    def add(self, user, **args):
        try:
            if not issubclass(user, AbstractModel):
                raise InvalidClassException()
            
            validator = v.ValuesValidator()
            d = validator.validate(**args)
            
            if False in d.values():
                raise IncorrectDataException(d)

            user(**args).save()
        except IntegrityError:
            raise InvalidFieldsException(user)
        

"""class PeeweeModelsRemover(ModelsRemover): - todo"""


if __name__ == '__main__':
    m = PeeweeModelAdder()
    m.add(
        Admin,
        name="1",
        surname="Test"
    )