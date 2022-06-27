from Account import Account
from CompleteOrder import CompleteOrder
from Enums import Tab
from Menu import Menu
from DataGenerator import CreateDataBase
from OrderTab import OrderTypeInfo
from sqlDb import Engine
from sqlalchemy.orm import sessionmaker
import UserInterface

def main():
    Session = sessionmaker(bind=Engine)    
    session = Session()
    CreateDataBase(session)
    account = Account()
    menu = Menu(session)
    orderTab = OrderTypeInfo()

    if(UserInterface.askYesNo('Log in with a testing account')):
        account.LogIn()
        menu.useLastOrder()
        orderTab.useLastOrder(account)

    while True:
        print()
        options =  ['Account', 'Menu', 'Order']
        if(menu.hasSelectedIems() and orderTab.isCompleted()):
            options.append('Complete Order')
        tab = UserInterface.enterNumber('Choose a tab', options)
        print()
        if(tab == Tab.ACCOUNT.value):
            account.TabInterface()
        elif(tab == Tab.MENU.value):
            menu.TabInterface(account.showDesription)
        elif(tab == Tab.ORDER.value):
            orderTab.TabInterface(account)
        elif(tab == Tab.COMPLETE.value):
            finished = CompleteOrder(orderTab.CreateOrder(menu.getSelectedItems()))
            if(finished):
                break
        elif(tab == Tab.QUIT.value):
            if(UserInterface.askYesNo('Are you sure you want to quit')):
                break

main()