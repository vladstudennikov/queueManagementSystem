class Customer:
    
    def __init__(self, id):
        self.id = id


    """def getCustomerId(self):
        return self.__id"""


    def __str__(self):
        return f"Customer №{self.id}"
    

    def __eq__(self, obj):
        if isinstance(obj, Customer):
            return self.id == obj.id
        return False