from sqlalchemy import create_engine
from Account import Account
from Enums import Size, CrustType, Tab
from MenuItem import MenuItem, PizzaMenuItem, ToppingMenuItem
from DataGenerator import CreateDataBase

from sqlDb import Base, Engine
from sqlalchemy.orm import sessionmaker
import UserInterface

def main():
    #CreateDataBase()
    account = Account()
    account.LogIn()

    while True:
        tab = 3#UserInterface.enterNumber('Go to Menu, Order, or Account tab', ['Menu', 'Order', 'Account'])
        if(tab == Tab.MENU.value):
            pass
        elif(tab == Tab.ORDER.value):
            pass
        elif(tab == Tab.ACCOUNT.value):
            account.TabInterface()
        elif(tab == Tab.QUIT.value):
            if(UserInterface.askYesNo('Are you sure you want to quit')):
                break



    """ Session = sessionmaker(bind=Engine)    
    session = Session()
    print("here")
    for row in session.query(PizzaMenuItem).all():
        print(row.id)
        print(row) """

main()