from LoginController import LoginController
from QueueServices import QueueService
from ModelsLogic import PeeweeModelAdder
from Monitor import Monitor
from Admin import Admin
from Operator import Operator
from Workplace import Workplace
from Customer import Customer

class BusinessLogic():

    users = {
            "operator": Operator,
            "admin": Admin,
            "monitor": Monitor,
            "workplace": Workplace
        }

    def __init__(self):
        self.logins = LoginController()
        self.queue = QueueService()
        self.crud = PeeweeModelAdder()
        """TODO: add class for deleting control"""

        self.customerid = 1


    def getUserByLogin(self, login: str, password: str): 
        return self.logins.getUser(login, password)
        

    def add(self, usertype: str, **args):
        if usertype not in self.users.keys():
            raise Exception("User was not found, usertypes: " + self.users.keys())
        
        self.queue.add(self.users[usertype], **args)

    
    def getUser(self, usertype: str, id: int):
        if usertype not in self.users.keys():
            raise Exception("User was not found, usertypes: " + self.users.keys())
        
        userlist = list(self.users[usertype].select())
        for i in userlist:
            if i.id == id:
                return i
            
        raise Exception("User with this id was not found")

    
    """def delete(self, ...) - TODO"""


    def addCustomer(self):
        self.queue.addCustomer(self.customerid)
        self.customerid += 1

    
    def getWorkplaces(self):
        return self.queue.getWorkplaces()
    

    def getCustomers(self):
        return self.queue.getListOfCustomers()


    def changeWorkplaceState(self, workplace: int, state):
        self.queue.changeWorkplaceState(workplace, state)


    def getWorkplaceOperator(self, workplaceid: int):
        if type(workplaceid) is not int:
            raise Exception("Invalid datatype")
        
        workplaces = self.queue.getWorkplaces()
        workplace = None
        for i in workplaces:
            if i.id == workplaceid:
                workplace = i
        return workplace.operator
    

    def getWorkplaceById(self, workplaceid: int):
        workplaces = self.queue.getWorkplaces()
        workplace = None
        for i in workplaces:
            if i.id == workplaceid:
                workplace = i
        return workplace


