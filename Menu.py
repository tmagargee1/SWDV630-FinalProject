from sqlalchemy import false, true
from Enums import CrustType, Size
from HelperFunctions import moneyString
from MenuItem import MenuItem, PizzaMenuItem, ToppingMenuItem
from OrderFoodItems import OrderItem, PizzaOrderItem
import UserInterface

class Menu():
    def __init__(self, session):
        self.selectedNonPizzas = []
        self.nonPizzaChoices = []

        self.selectedPizzas = []   
        self.session = session

    def useLastOrder(self):
        #TODO list past orders to accounts to fill in default orders
        #For now hardcoded testing code
        pizza = PizzaOrderItem(self.session.query(PizzaMenuItem).get(6))
        pizza.addTopping(self.session.query(ToppingMenuItem).get(15))
        self.selectedPizzas = [pizza]

        self.selectedNonPizzas = [OrderItem(self.session.query(MenuItem).get(1), 2)]
        self.nonPizzaChoices = [0]

    def TabInterface(self, showDescription):
        self.showDescription = showDescription
        while(True):
            options = ['Create a Pizza', 'Select Non Pizza Item']
            if(self.hasSelectedIems()):
                options.append('View Selected Items')
            num = UserInterface.enterNumber('Select an option', options)
            print()
            if(num == 1):
                self.createPizza()
            elif(num == 2):
                self.orderNonPizza()
            elif(num == 3):
                self.viewSelectedItems()
            else:
                break
            print()
    
    def createPizza(self):
        options = []
        idNums = []
        pizzaId = 0
        firstTime = True
        while(True):
            if(firstTime):
                firstTime = False
            else:
                if(UserInterface.askYesNo("Leave pizza tab")):
                    break
            if(UserInterface.askYesNo("Select Pizza From List (to see all prices)")):
                for row in self.session.query(PizzaMenuItem).all():
                    idNums.append(row.id)
                    options.append('{} {} {} Crust'.format(moneyString(row.price), row.size, row.crust))
                choice = UserInterface.enterNumber('Select a pizza', options)
                if(choice == -1):
                    continue
                else:
                    pizzaId = idNums[choice-1]
            else:
                options = [c for c in CrustType]
                crustChoice = UserInterface.enterNumber('Select a crust', options)
                if(crustChoice == -1):
                    continue
                else:
                    options = []
                    possibleOptions = self.session.query(PizzaMenuItem).filter_by(crust= CrustType(crustChoice))
                    idNums = []
                    for row in possibleOptions.all():
                        idNums.append(row.id)
                        options.append('{} {}'.format(moneyString(row.price), row.size))
                sizeChoice = UserInterface.enterNumber('Select a size', options)
                if(sizeChoice == -1):
                    continue
                else:
                    pizzaId = idNums[sizeChoice-1]
            pizza = PizzaOrderItem(self.session.query(PizzaMenuItem).get(pizzaId))
            if(UserInterface.askYesNo("Add Toppings")):
                self.addToppings(pizza)
            print('Selected Pizza:')
            print(pizza)
            pizza.quantity = UserInterface.GetValidNumber('How many do you want?')
            self.selectedPizzas.append(pizza)
            print('Pizza successfully added to selected items!')
              
    def addToppings(self, pizza):
        toppingOptions = []
        toppingIds = []
        for row in self.session.query(ToppingMenuItem).all():
            price = row.getPrice(pizza.menuItem.size)
            toppingString = '{} Add {}'.format(moneyString(price), row.name)
            if(self.showDescription):
                toppingString += ' :{}'.format(row.description)
            toppingOptions.append(toppingString)
            toppingIds.append(row.id)

        choices = []
        while(True):
            print(pizza)
            choice = UserInterface.enterNumber('Select a topping', toppingOptions)
            if(choice == -1):
                break
            else:
                choice -= 1
                topping = self.session.query(ToppingMenuItem).filter_by(id= toppingIds[choice]).first()
                if(choice in self.nonPizzaChoices):
                    pizza.removeTopping(topping)
                    choices.remove(choice)
                    toppingOptions[choice] = toppingOptions[choice].replace('Remove', 'Add')
                else:
                    pizza.addTopping(topping)
                    choices.append(choice)
                    toppingOptions[choice] = toppingOptions[choice].replace('Add', 'Remove')
        return pizza           
 
    def orderNonPizza(self):
        options = []
        idNums = []        
        chosenId = 0
        for row in self.session.query(MenuItem).filter_by(type= 'menu').all():
            price = row.price
            info = '{} {}'.format(moneyString(price), row.name)
            if(self.showDescription):
                info += ': {}'.format(row.description)
            options.append(info)
            idNums.append(row.id)
        while(True):
            choice = UserInterface.enterNumber('Select an item', options)
            if(choice == -1):
                break
            else:
                choice -= 1
                if(choice in self.nonPizzaChoices):
                    quantity = UserInterface.GetValidNumber('How many do you want? (Enter 0 for none)', 0)
                    options[choice] = options[choice][0:options[choice].find('(')]
                    choiceIndex = self.nonPizzaChoices.index(choice)
                    if(quantity == 0):
                        del self.selectedNonPizzas[choiceIndex]
                        self.nonPizzaChoices.remove(choice)
                    else:
                        item = self.selectedNonPizzas[choiceIndex]
                        item.menuItem.quantity = quantity
                        options[choice] = options[choice] + ' ({} Ordered)'.format(item.menuItem.quantity)
                else:
                    chosenId = idNums[choice]
                    item = OrderItem(self.session.query(MenuItem).filter_by(id= chosenId).first())
                    item.menuItem.quantity = UserInterface.GetValidNumber('How many do you want?')
                    self.nonPizzaChoices.append(choice)
                    self.selectedNonPizzas.append(item)
                    options[choice] = options[choice] + ' ({} Ordered)'.format(item.menuItem.quantity)
            
    def viewSelectedItems(self):
        if(self.selectedPizzas):
            print('Pizzas')
            for item in self.selectedPizzas:
                print(self.getViewItemString(item))
            print()
        if(self.selectedNonPizzas):
            print('Non Pizza Items')
            for item in self.selectedNonPizzas:
                print(self.getViewItemString(item))
            print()
        if(not UserInterface.askYesNo("Would you like to edit your items")):
            return
        
        while(True):
            print()
            options = []
            for item in self.selectedPizzas:
                options.append(self.getViewItemString(item))
            for item in self.selectedNonPizzas:
                options.append(self.getViewItemString(item))
            if(options == []):
                break
            choice = UserInterface.enterNumber('Edit an Item', options) 

            if(choice == -1):
                break
            else:
                quantity = UserInterface.GetValidNumber('Change number (enter 0 to remove from order)', 0)
                choice -= 1
                if(choice < len(self.selectedPizzas)):
                    #TODO allow user to edit toppings on this screen
                    pizza = self.selectedPizzas[choice]
                    if(quantity == 0):
                        del self.selectedPizzas[choice]
                    else:
                        pizza.quantity = quantity
                else:
                    item = self.selectedNonPizzas[choice]
                    if(quantity == 0):
                        del self.selectedNonPizzas[choice]
                    else:
                        item.quantity = quantity
                
    def getViewItemString(self, item):
        return '{} {}'.format(moneyString(item.getPrice()), item.getInfoString(self.showDescription))

    def hasSelectedIems(self):
        return bool(self.selectedNonPizzas or self.selectedPizzas) 

    def getSelectedItems(self):
        return self.selectedPizzas + self.selectedNonPizzas