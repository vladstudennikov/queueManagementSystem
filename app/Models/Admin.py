from peewee import *
from .Model import BaseModel
from .setup import settings


class Admin(BaseModel):

    class Meta:
        db_table = settings["admins_table"]

    id = AutoField()
    name = CharField()
    surname = CharField()
    email = CharField()


    def __str__(self):
        return "Admin #{id} ({name} {surname}{email})".format(id=self.id, name=self.name, surname=self.surname, email=(", email: {email}".format(email=self.email) ) if self.email != None else "") 
 

if __name__ == '__main__':
    a = Admin()
    print(list(a.select()))

    Admin(
        name="Test"
    ).save()

