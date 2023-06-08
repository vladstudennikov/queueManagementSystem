from abc import ABC, abstractmethod
import re


class ValidatorModel(ABC):
    @abstractmethod
    def validate(self, value) -> bool: pass


class EmailValidator(ValidatorModel):

    def validate(self, email: str) -> bool:
        emailregex = "^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-z]{2,6}$"

        if re.fullmatch(pattern=emailregex, string=email):
            return True
        return False
    

class NameValidator(ValidatorModel):

    def validate(self, name: str) -> bool:
        nameregex = "[A-Z][a-z]+"

        if re.fullmatch(pattern=nameregex, string=name):
            return True
        return False
    

class IDValidator(ValidatorModel):

    def validate(self, id: int) -> bool:
        return type(id) is int