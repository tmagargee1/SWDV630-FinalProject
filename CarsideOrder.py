from Order import Order
import UserInterface

class CarsideInfo():
    def __init__(self, createCar = True, color = '', make = '', model = ''):
        if(createCar):
            self.color = UserInterface.GetValidString('Enter color').capitalize()
            self.make = UserInterface.GetValidString('Enter make').capitalize()
            self.model = UserInterface.GetValidString('Enter model').capitalize()
        else:
            self.color = color
            self.make = make
            self.model = model

    def __str__(self):
        return '{} {} {}'.format(self.color, self.make, self.model)

    def EditCar(self):
        while(True):
            num = UserInterface.enterNumber('Which property do you want to edit',
             ['Color ({})'.format(self.color), 'Make ({})'.format(self.make), 'Model ({})'.format(self.model)])
            if(num == 1):
                self.color = UserInterface.GetValidString('Enter New Color')
            elif(num == 2):
                self.make = UserInterface.GetValidString('Enter New Make')
            elif(num == 3):
                self.model =UserInterface.GetValidString('Enter New Model')
            else:
                break
        
    
class CarsideOrder(Order):
    
    def __init__(self, name, orderItems, carsideInfo):
        super().__init__(name, orderItems)
        self.carInfo = carsideInfo
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
        return super().__str__() + "\nCarry to car: {} {}".format(self.carInfo, carrierString)

    def getOrderInfoMessage(self):
        return 'Carside\n' + super().getOrderInfoMessage() + '\nCar: {}'.format(self.carInfo)