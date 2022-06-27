from sqlalchemy import false, true
from CarsideOrder import CarsideInfo
from DeliveryOrder import DeliveryInfo
import UserInterface

class Account():
    
    def __init__(self):
        self.guest = True
        self.name = ''
        self.showDesription = False
        self.carsideInfo = []
        self.deliveryInfo = []


    def LogIn(self):
        print("Logging in user")
        self.guest = False
        self.showDesription = False
        self.name = 'Tim'
        self.carsideInfo = [CarsideInfo(False, 'Blue', 'Honda', 'Civic'), CarsideInfo(False, 'White', 'Checy', 'Prism')]
        self.deliveryInfo = [DeliveryInfo(False)]

    def TabInterface(self):
        if(self.guest):
            print("No accounts found")
            if(UserInterface.askYesNo('Would you like to create an account')):
                self.createAccount()
            else:
                print('Sending back to home page')
        else:
            self.editAccount()

    def createAccount(self):   
        self.enterBasicInfo()     
        self.guest = False
        if(UserInterface.askYesNo('Do you want to add order info now')):
            while(True):
                num = UserInterface.enterNumber('Which order type?', ['Carside', 'Delivery'])
                if(num == 1):
                    self.enterCarsideInfo()
                elif(num == 2):
                    self.enterDeliveryInfo()
                else:
                    break
                print()


    def editAccount(self):
        self.showAccountInfo()
        while(True):
            num = UserInterface.enterNumber('Would you like to edit your account?', ['Delete Account', 'Edit Basic Info', 'Edit Cars', 'Edit Addresses'])
            if(num == 1):
                self.__init__()
                break
            elif(num == 2):
                self.enterBasicInfo()
            elif(num == 3):
                self.enterCarsideInfo()
            elif(num == 4):
                self.enterDeliveryInfo()
            else:
                break

    def showAccountInfo(self):
        print('Basic Info')
        print('\tName: {}'.format(self.name))
        print('\tShow Discriptions: {}'.format(self.showDesription))
        if(self.carsideInfo == []):
            print('No cars added')
        else:
            print('Cars')
            for car in self.carsideInfo:
                print('\t{}'.format(car))
        if(self.deliveryInfo == []):
            print('No Addresses')
        else:
            print('Addresses')
            for addr in self.deliveryInfo:
                print('\t{}'.format(addr))

        
    def enterBasicInfo(self):
        if(self.guest):
            print('Collecting Basic info')
            self.name = UserInterface.GetValidString('Enter Name')
            self.showDesription = UserInterface.askYesNo('Would you like the description of items to be shown')
            return #Remove if user should immeditiately be able to edit

        while(True):
            options = ['Edit Name ({})'.format(self.name)]
            if(self.showDesription):
                options.append('Stop showing descriptions')
            else:
                options.append('Show descriptions')
            num = UserInterface.enterNumber('Select an option', options)
            if(num == 1):
                self.name = UserInterface.GetValidString('Enter new name')
            elif(num == 2):
                self.showDesription = not self.showDesription
            else:
                return

    def enterCarsideInfo(self):
        if(self.carsideInfo == []):
            print('Please add a car')
            self.carsideInfo.append(CarsideInfo())
        
        while(True):
            options = ['New Car'] + list(map(str, self.carsideInfo))
            num = UserInterface.enterNumber('Add a new car or edit an existing one', options)
            if(num == 1):
                self.carsideInfo.append(CarsideInfo())
            elif(num > 1):
                num -= 2
                if(UserInterface.askYesNo('Do you want to delete this car')):
                    del self.carsideInfo[num]
                    print('Deleted Car')
                else:
                    self.carsideInfo[num].EditCar()
            else:
                break

    def enterDeliveryInfo(self):
        if(self.deliveryInfo == []):
            print('Please add an address')
            self.deliveryInfo.append(DeliveryInfo())
        
        while(True):
            options = ['New Address'] + list(map(str, self.carsideInfo))
            num = UserInterface.enterNumber('Add a new address or edit an existing one', options)
            if(num == 1):
                self.carsideInfo.append(CarsideInfo())
            elif(num > 1):
                num -= 2
                if(UserInterface.askYesNo('Do you want to delete this address')):
                    del self.deliveryInfo[num]
                    print('Deleted address')
                else:
                    self.deliveryInfo[num].Edit()
            else:
                break

