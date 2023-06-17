from peewee import *
from LoginData import OperatorloginData, AdminLoginData, MonitorLoginData
from setup import settings


class LoginController:
    def __init__(self):
        self.operators = list(OperatorloginData.select())
        self.admins = list(AdminLoginData.select())
        self.monitors = list(MonitorLoginData.select())

    
    def getUser(self, login, password):
        for i in range(len(self.operators)):
            if self.operators[i].login == login and self.operators[i].password == password:
                return self.operators[i].operator
            
        for i in range(len(self.admins)):
            if self.admins[i].login == login and self.admins[i].password == password:
                return self.admins[i].admin
            
        for i in range(len(self.monitors)):
            if self.monitors[i].login == login and self.monitors[i].password == password:
                return self.monitors[i].monitor
        
        raise Exception("User was not found")
            

if __name__ == '__main__':
    l = LoginController()
    print(l.getUser("oper2", "oper2"))