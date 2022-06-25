from abc import ABCMeta, abstractmethod
from datetime import datetime, timedelta

from Enums import PaymentMethod
from sqlDb import Base
from sqlalchemy import Column, Integer, String, Date, Float, Boolean

class Order(metaclass=ABCMeta):
    def __init__(self, fName, lName, orderItems):
        self.customerFirstName = fName
        self.customerLastName = lName
        self.timePlaced = datetime.now()
        self.orderItems = orderItems
        self.totalCost = orderItems.getTotalCost()
        self.paid = False
        self.estimatedTimeFoodRecieved = self.timePlaced + timedelta(minutes = self.getEstimatedTime())

    #id = Column(Integer, primary_key = True)
    #fName = Column(String)
    #lName = Column(String)
    #timePlaced = Column(Date)
    #totalCost = Column(Float)
    #paid = Column(Boolean)
    #estimatedTimeFoodRecieved = Column(Date)

    #def __repr__(self):
    #    return "<Order{fname={0}, lname={}}>".format(self.fName, self.lName)

    @abstractmethod
    def getConfirmationMessage(self):
        pass
    @abstractmethod    
    def getEstimatedTime(self):
        #Assumes 10 minutes from makeline to cut and one minute to prepare each item
        return 10 + self.orderItems.getTotalNumItems()

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

        return """Customer {0} {1} Ordered at {2} 
Food will be recieved at {3}
{4}""".format(self.customerFirstName, self.customerLastName, self.timePlaced, 
        self.estimatedTimeFoodRecieved, 
        payString)



class CarryoutOrder(Order):
    def getConfirmationMessage(self):
        return "Your order will be ready for pickup in about {} minutes".format(self.getEstimatedTime()) 

    def getEstimatedTime(self):
        return super().getEstimatedTime() + 1 #One minute to find customer