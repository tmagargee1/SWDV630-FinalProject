from Enums import Size, CrustType
from MenuItem import MenuItem, PizzaMenuItem, ToppingMenuItem
from sqlalchemy import create_engine

from sqlDb import Base
from sqlalchemy.orm import sessionmaker

def main():
    print('Creating Objects to store')
    menuItem1 = MenuItem("Garlic Knots", 6.99, 'Garlicy Bread')
    menuItem2 = MenuItem("Cinnamon Twists", 7.99, 'Made with CinnaMagic')
    pizza1 = PizzaMenuItem(5.99, Size.SMALL, CrustType.HAND_TOSSED)
    pizza2 = PizzaMenuItem(8.99, Size.MEDIUM, CrustType.PAN)
    topping1 = ToppingMenuItem('Pepperoni', 'Small red meat circles', False)
    topping2 = ToppingMenuItem('Premium Chicken', 'Fancy Chicken', True)

    print('Creating database')
    engine = create_engine('sqlite:///:memory:', echo = False)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)    
    session = Session()


    session.add(menuItem1)
    session.add(menuItem2)
    newMenuItem1 = session.query(MenuItem).filter_by(name='Garlic Knots').first()
    print(newMenuItem1)
    print('Was first menu Item stored correctly?: {}'.format(newMenuItem1 == menuItem1))
    print()
    print('Adding Pizza menu items')
    session.add_all({pizza1, pizza2})

    for row in session.query(PizzaMenuItem).all():
        print(row)

    print()
    print('Adding topping menu items')
    session.add_all({topping1, topping2})
    for row in session.query(ToppingMenuItem).all():
        print(row)

    print()
    print('All menu items')
    for row in session.query(MenuItem).all():
        print(row)

    print()
    print('Filter for only generic items')
    for row in session.query(MenuItem).filter_by(type= 'menu').all():
        print(row)

    print()
    print('Menu Items that cost less than $7 and are not toppings')
    for row in session.query(MenuItem).filter(MenuItem.price < 7).filter(MenuItem.type != 'menuTopping').all():
        print(row)

    

main()