
from Order import Order


class CarsideOrder(Order):
    
    def __init__(self, fName, lName, orderItems, carMake, carColor):
        super().__init__(fName, lName, orderItems)
        self.carMake = carMake
        self.carColor = carColor
        self.carrier = "None"

    def getConfirmationMessage(self):
        return "We will carry the order to your car in about {} minutes".format(self.getEstimatedTime()) 

    def assignCarrier(self):
        #Get next Insider available 
        self.carrier = "Katie" #Update in future

    def getEstimatedTime(self):
        #Carside orders are given 2 minutes for a dominos member to deliver
        return super().getEstimatedTime() + 2

    def __str__(self):
        if(self.carrier != "None"):
            carrierString = "\n{0} is delivering the order".format(self.carrier)
        else:
            carrierString = ""
        return super().__str__() + "\nCarry to car: {0} {1} {2}".format(self.carColor, self.carMake, carrierString)

