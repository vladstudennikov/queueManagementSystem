from .Customer import Customer
from .Models import Workplace


class InvalidDatatypeException(Exception):

    def __init__(self, text):
        return super().__init__(text)
    

class WorkplaceWasNotFoundException(Exception):

    def __init__(self):
        return super().__init__("Workplace was not found in list")


class QueueService():

    def __init__(self):
        self.__customerList = list()
        self.__workplaces = dict()

        for i in list(Workplace.select()):
            self.__workplaces[i] = None

        
    def __attachCustomerToWorkplace(self, customer: Customer) -> int:
                                  
        for i in self.__workplaces:
            if self.__workplaces[i] is None and i.getstate() != "busy":
                self.__workplaces[i] = customer
                return i.id
        return -1


    def addCustomer(self, id: int) -> str:

        if type(id) is not int:
            raise InvalidDatatypeException("User id should be integer value")

        c = Customer(id)

        if c in self.__customerList or c in self.__workplaces.values():
            raise Exception("This customer is already in the queue")

        a = self.__attachCustomerToWorkplace(c)

        if a != -1:
            return f"User was attached to a workplace {a}"
        
        self.__customerList.append(c)
        return "User was added to queue"


    def getWorkplaces(self) -> dict:
        return self.__workplaces
    

    def getListOfCustomers(self) -> list:
        return self.__customerList
    

    def changeWorkplaceState(self, workplaceid: int, state: str) -> str:
        if type(workplaceid) is not int:
            raise InvalidDatatypeException("Workplace id should be integer number")
        
        if state.lower() != "busy" and state.lower() != "free":
            raise InvalidDatatypeException("Possible states of workplace: free or busy")
        
        for i in self.__workplaces:
            if i.id == workplaceid:
                if i.getstate() == state:
                    return f"State is already {state}"

                if i.getstate() == "busy" and state == "free":
                    
                    if self.__workplaces[i] == None and len(self.__customerList) > 0:
                        self.__workplaces[i] = self.__customerList[0]
                        self.__customerList.pop(0)
                        i.setstate(state)
                        return "State was changed and client was assigned"

                    if self.__workplaces[i] != None:
                        self.__workplaces[i] = None
                        print(len(self.__customerList))
                        if len(self.__customerList) > 0:
                            self.__workplaces[i] = self.__customerList[0]
                            self.__customerList.pop(0)
                        i.setstate(state)
                        return "State was changed and client was assigned"
                
                i.setstate(state)
                return "state was changed"
        
        raise WorkplaceWasNotFoundException()


if __name__ == "__main__":
    q = QueueService()
    q.addCustomer(1)
    q.addCustomer(2)
    q.addCustomer(3)
    q.addCustomer(4)
    q.addCustomer(5)
    print("Guys are free and were added new customers")
    for k, v in q.getWorkplaces().items():
        print(f"{k} - {v}")
    for i in q.getListOfCustomers():
        print(i)

    print(q.changeWorkplaceState(1, "free"))
    print("\nWas changed state of operator 1 to busy")
    for k, v in q.getWorkplaces().items():
        print(f"{k} - {v}")
    for i in q.getListOfCustomers():
        print(i)

    print(q.changeWorkplaceState(1, "free"))
    print("\nWas changed state and now we are ready to serve new customers")
    for k, v in q.getWorkplaces().items():
        print(f"{k} - {v}")
    for i in q.getListOfCustomers():
        print(i)

    q.changeWorkplaceState(2, "free")
    for k, v in q.getWorkplaces().items():
        print(f"{k} - {v}")
    for i in q.getListOfCustomers():
        print(i)

    print()
    for k, v in q.getWorkplaces().items():
        print(f"{k} - {v}")
    for i in q.getListOfCustomers():
        print(i)

    q.changeWorkplaceState(2, "free")
    print()
    for k, v in q.getWorkplaces().items():
        print(f"{k} - {v}")
    for i in q.getListOfCustomers():
        print(i)