

from Order import Order
import UserInterface

class DeliveryInfo():
    def __init__(self, createAddress = True, streetInfo = '123 Road rd', deliveryInstructions = ''):
        #TODO Hold other address info defaulted to store info 
        if(createAddress):
            self.streetInfo = UserInterface.GetValidString('Street Address')
            self.deliveryInstructions = UserInterface.GetValidString('Enter any special instructions', '')
        else:
            self.streetInfo = streetInfo
            self.deliveryInstructions = deliveryInstructions

    def __str__(self):
        if(self.deliveryInstructions == ''):
            return self.streetInfo
        else:
            return '{}, {}'.format(self.streetInfo, self.deliveryInstructions)

    def Edit(self):
        while(True):
            num = UserInterface.enterNumber('Which property do you want to edit',
             ['Street Address ({})'.format(self.color), 'Delivery Instructions ({})'.format(self.make)])
            if(num == 1):
                self.streetInfo = UserInterface.GetValidString('Enter New Color')
            elif(num == 2):
                self.deliveryInstructions = UserInterface.GetValidString('Enter New Make')
            else:
                break

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