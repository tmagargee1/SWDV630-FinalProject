

from Order import Order


class DeliveryOrder(Order):
    
    def __init__(self, fName, lName, orderItems, address):
        super().__init__(fName, lName, orderItems)
        self.address = address
        self.driver = "None"

    def getConfirmationMessage(self):
        return "Our driver will arrive with your order in about {} minutes".format(self.getEstimatedTime()) 

    def assignDriver(self):
        #Get next driver available 
        self.driver = "Tim" #Update in future

    def getEstimatedTime(self):
        return super().getEstimatedTime() + self.getTimeToAddress()

    def getTimeToAddress(self):
        #Find how long of a drive self.address is from store
        return 10

    def __str__(self):
        if(self.driver != "None"):
            driverString = "\n{0} is delivering the order".format(self.driver)
        else:
            driverString = ""
        return super().__str__() + "\nDeliver to {0} {1}".format(self.address, driverString)