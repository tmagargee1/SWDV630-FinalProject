from sqlalchemy import null
from Account import Account
from CarsideOrder import CarsideInfo, CarsideOrder
from DeliveryOrder import DeliveryInfo, DeliveryOrder
from Enums import OrderType
from Order import CarryoutOrder
import UserInterface


class OrderTypeInfo():
    def __init__(self):
        self.orderType = None
        self.account = Account()
        self.orderName = ''
        self.carsideInfo = None
        self.deliveryInfo = None
        pass

    def useLastOrder(self, account):
        self.orderName = account.name
        self.orderType = OrderType.CARRYOUT

    def TabInterface(self, account):
        self.account = account
        options = [ot for ot in OrderType]
        if(self.orderName == ''):
            self.editOrderName()
        options.append('Edit Order Name ({})'.format(self.orderName))
        while(True):
            if(self.orderType != None):
                print("Currently {} is selected".format(self.orderType))
            choice = UserInterface.enterNumber('What type of order', options)
            if(choice == -1):
                break
            else:
                if(choice == OrderType.CARRYOUT.value):
                    self.orderType = OrderType.CARRYOUT
                elif(choice == OrderType.CARSIDE.value):
                    self.editCarsideInfo()
                elif(choice == OrderType.DELIVERY.value):
                    self.editDeliveryInfo()
                else:
                    self.editOrderName()
                    options[choice-1] = 'Edit Order Name ({})'.format(self.orderName)
            print()
                    

    def editOrderName(self):
        if(not self.account.guest):
            if(self.orderName == ''):
                self.orderName = self.account.name
        elif(self.orderName != ''):
            print('Current name for order is {}'.format(self.orderName))
            if(UserInterface.askYesNo('Change order name')):
                self.orderName = UserInterface.GetValidString('Enter new name')
        else:
            self.orderName = UserInterface.GetValidString('Enter name for order')

    def editCarsideInfo(self):
        if(self.carsideInfo == None):
            if(self.account.guest):
                self.carsideInfo = CarsideInfo()
            else:
                if(len(self.account.carsideInfo) != 0):
                    options = list(map(str, self.account.carsideInfo)) + ['New Car']
                    choice = UserInterface.enterNumber('Choose car from your account or add one', options)
                    if(choice == len(options)):
                        car = CarsideInfo()
                        self.account.carsideInfo.append(car)
                        self.carsideInfo = car
                    elif(choice > 0):
                        choice -= 1
                        self.carsideInfo = options[choice]
                    else:
                        return 
                self.orderType = OrderType.CARSIDE
        else:
            print('Current car for order is {}'.format(self.carsideInfo))
            if(UserInterface.askYesNo('Change car')):
                self.carsideInfo = None
                self.orderType = None
                self.editCarsideInfo()

    def editDeliveryInfo(self):
        if(self.deliveryInfo == None):
            if(self.account.guest):
                self.deliveryInfo = DeliveryInfo()
            else:
                if(len(self.account.deliveryInfo) != 0):
                    options = list(map(str, self.account.deliveryInfo)) + ['New Address']
                    choice = UserInterface.enterNumber('Choose address from your account or add one', options)
                    if(choice == len(options)):
                        car = DeliveryInfo()
                        self.account.deliveryInfo.append(car)
                        self.deliveryInfo = car
                    elif(choice > 0):
                        choice -= 1
                        self.deliveryInfo = options[choice]
                    else:
                        return 
        else:
            print('Current address for order is {}'.format(self.deliveryInfo))
            if(UserInterface.askYesNo('Change Address')):
                self.deliveryInfo = None
                self.orderType = None
                self.editDeliveryInfo()
                return
        self.orderType = OrderType.DELIVERY
    
    def isCompleted(self):
        return self.orderType != None

    def CreateOrder(self, selectedItems):
        if(self.orderType == None):
            return False
        elif(self.orderType == OrderType.CARRYOUT):
            return CarryoutOrder(self.orderName, selectedItems)
        elif(self.orderType == OrderType.CARSIDE):
            return CarsideOrder(self.orderName, selectedItems, self.carsideInfo)
        elif(self.orderType == OrderType.DELIVERY):
            return DeliveryOrder(self.orderName, selectedItems, self.deliveryInfo)