from abc import ABCMeta, abstractmethod
from datetime import datetime, timedelta

from Enums import PaymentMethod

class Order(metaclass=ABCMeta):
    def __init__(self, name, orderItems):
        self.customerName = name
        self.timePlaced = datetime.now()
        self.orderItems = orderItems
        self.totalCost = sum(oi.getPrice() for oi in orderItems)
        self.paid = False
        self.estimatedTimeFoodRecieved = self.timePlaced + timedelta(minutes = self.getEstimatedTime())

    @abstractmethod
    def getConfirmationMessage(self):
        pass
    @abstractmethod    
    def getEstimatedTime(self):
        #Assumes 10 minutes from makeline to cut and one minute to prepare each item
        return 10 + len(self.orderItems)

    @abstractmethod
    def getOrderInfoMessage(self):
        return 'Name: {}'.format(self.customerName)

    def processPayment(self, paymentMethod):
        if(paymentMethod == PaymentMethod.CASH):
            #Process Cash Payment
            print("Cash processed")
        elif(paymentMethod == PaymentMethod.GIFT_CERTIFICATE):
            #Process Gift Card
            print("Gift card processed")
        elif(paymentMethod == PaymentMethod.CARD):
            #Process Card
            print("Credit/debit card processed")
        else:
            raise Exception("Invalid Payment type")

        self.paid = True

    def __str__(self):
        payString = 'Paid' if self.paid else 'Unpaid'
        payString =  payString + ' Total: ${:,.2f}'.format(self.totalCost)

        return """Customer {0} Ordered at {2} 
Food will be recieved at {3}
{4}""".format(self.customerName, self.timePlaced, 
        self.estimatedTimeFoodRecieved, 
        payString)


class CarryoutOrder(Order):
    def getConfirmationMessage(self):
        return "Your order will be ready for pickup in about {} minutes".format(self.getEstimatedTime()) 

    def getEstimatedTime(self):
        return super().getEstimatedTime() + 1 #One minute to find customer

    def getOrderInfoMessage(self):
        return 'Carryout\n' + super().getOrderInfoMessage()