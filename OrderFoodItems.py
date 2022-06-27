
import copy
from HelperFunctions import moneyString
from sqlDb import Base


class OrderItem():
    def __init__(self, menuItem, quantity = 1):
        self.menuItem = menuItem
        self.quantity = quantity

    def getPrice(self):
        return self.menuItem.price * self.quantity

    def getInfoString(self, showDescription = False):
        des = ' ({})'.format(self.menuItem.description) if showDescription else ''
        return '{}: {}{}'.format(self.quantity, self.menuItem.name, des)

    def __str__(self):
        return '{}\n    Costs: {}'.format(self.getInfoString(), moneyString(self.getPrice()))

    def clone(self):
        return copy.deepcopy(self)

class PizzaOrderItem(OrderItem):
    def __init__(self, menuItem, quantity = 1):
        super().__init__(menuItem, quantity)
        self.toppings = []

    def addTopping(self, topping):
        topping.updatePrice(self.menuItem.size)
        self.toppings.append(topping)
    
    def removeTopping(self, topping):
        self.toppings.remove(topping)

    def getPrice(self):
        toppingPrice = 0
        for topping in self.toppings:
            toppingPrice += topping.price
        
        toppingPrice = toppingPrice * self.quantity
        return super().getPrice() + toppingPrice

    def getInfoString(self, showDescription = False):
        if len(self.toppings) > 0:
            toppingString = 'Topped with '
            for topping in self.toppings:
                toppingString += topping.name + ', '
            toppingString = toppingString[:-2] #Remove last comma
        else:
            toppingString = ''

        return '{}: {} {}'.format(self.quantity, self.menuItem, toppingString)

    def __str__(self):
        priceString = 'Costs: {}'.format(moneyString(self.getPrice()))
        return '{}\n    {}'.format(self.getInfoString(), priceString)

class OrderFoodIterator:
    def __init__(self, items):
        self.indx = -1
        self.items = items

    def has_next(self):
        return self.indx < len(self.items) - 1

    def next(self):
        self.indx += 1
        item = self.items[self.indx]
        return item

    def has_prev(self):
        return self.indx > 0

    def prev(self):
        self.indx -= 1
        item = self.items[self.indx]
        return item

    def curr(self):
        item = self.items[self.indx]
        return item

    def remove(self):
        item = self.items.pop(self.indx)
        #If removing last item in list then go to new last item
        if(self.indx == len(self.items)):
            self.indx -= 1
        return item

class OrderFoodInfo:
    def __init__(self):
        self.items = []
    
    def add(self, item):
        self.items.append(item)

    def iterator(self):
        return OrderFoodIterator(self.items)

    def getTotalCost(self):
        iterator = self.iterator()
        totalCost = 0
        while iterator.has_next():
            item = iterator.next()
            totalCost += item.getPrice()
        return totalCost

    def getTotalNumItems(self):
        iterator = self.iterator()
        count = 0
        while iterator.has_next():
            item = iterator.next()
            count += item.quantity
        return count

    def clone(self):
        return copy.deepcopy(self)