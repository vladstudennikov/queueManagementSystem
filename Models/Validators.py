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
    

validationsetup = {
        "name": NameValidator,
        "surname": NameValidator,
        "email": EmailValidator,
        "id": IDValidator
    }
    

class ValuesValidator:

    def validate(self, **args):
        d = dict()

        for i in args:
            if i in validationsetup:
                tmp = validationsetup[i]
                d[i] = tmp.validate(self, args[i])
        
        return d


if __name__ == '__main__':
    v = ValuesValidator()
    print(v.validate(
        name="1",
        surname="Test",
        id=1
    ))