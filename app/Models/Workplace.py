from peewee import *
from .Operator import Operator
from .Model import BaseModel
from .setup import settings


class WorkplaceStateException(Exception):

    def __init__(self, inputdata):
        super().__init__("Invalid state for a workplace, possible states are free and busy. Enetered state: {state}".format(state=inputdata))


class Workplace(BaseModel):

    class Meta:
        db_table = settings["workplaces_table"]

    id = AutoField()
    operator = ForeignKeyField(Operator)
    __state = "busy"


    def setstate(self, state):
        if not (state == "busy" or state == "free"):
            raise WorkplaceStateException(state)
        self.__state = state

    
    def getstate(self):
        return self.__state

    
    def __str__(self):
        return "Workplace №{id}{operator} ({state})".format(id=self.id, operator=(", operator: {name} {surname}".format(name=self.operator.name, surname=self.operator.surname) if self.operator != None else " (No operator)"), state=self.getstate())
    

if __name__ == '__main__':
    Workplace(
        operator=1
    ).save()