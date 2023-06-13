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

    def getUser(self): 
        return self.logins.getUser()
        

    def add(self, user: str, **args):
        users = {
            "operator": Operator,
            "admin": Admin,
            "monitor": Monitor,
            "workplace": Workplace
        }
        
        if user not in users.keys():
            raise Exception("User was not found, usertypes: " + users.keys())
        
        self.queue.add(users[user], **args)

    
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
        if type(id) is not int:
            raise Exception("Invalid datatype exception")
        
        self.queue.addCustomer(self.customerid)
        self.customerid += 1

    
    def getWorkplaces(self):
        return self.queue.getWorkplaces()
    

    def getCustomers(self):
        return self.queue.getListOfCustomers()


    def changeWorkplaceState(self, workplace: int, state):
        self.queue.changeWorkplaceState(workplace, state)


