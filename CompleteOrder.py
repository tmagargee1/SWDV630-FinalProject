from HelperFunctions import moneyString
from Order import Order
import UserInterface


def CompleteOrder(order : Order):
    print('Selected Items cost a total of {}'.format(moneyString(order.totalCost)))
    for item in order.orderItems:
        print('{}: {}'.format(moneyString(item.getPrice()), item.getInfoString()))

    print()
    print('Order Type info')
    print(order.getOrderInfoMessage())
    print()

    if(UserInterface.askYesNo('Place Order')):
        print(order.getConfirmationMessage())
        return True
    return False

    


