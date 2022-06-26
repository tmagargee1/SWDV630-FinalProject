from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Enums import CrustType, Size

from MenuItem import MenuItem, PizzaMenuItem, ToppingMenuItem
from sqlDb import Base, Engine

def CreateDataBase():
    print('Creating Objects to store')
    #Non pizza
    nonPizzaArray = {
        MenuItem("Garlic Knots", 6.99, 'Garlicy Bread'),
        MenuItem("Cinnamon Twists", 7.99, 'Made with CinnaMagic'),
        MenuItem("Lava Cakes", 5.99, 'The perfect dessert')
    }

    #Pizzas
    pizzaArray = {
        #Normal
        PizzaMenuItem(5.99, Size.SMALL, CrustType.HAND_TOSSED),
        PizzaMenuItem(7.99, Size.MEDIUM, CrustType.HAND_TOSSED),
        PizzaMenuItem(9.99, Size.LARGE, CrustType.HAND_TOSSED),
        PizzaMenuItem(11.99, Size.EXTRA_LARGE, CrustType.HAND_TOSSED),
        #Special
        PizzaMenuItem(7.99, Size.SMALL, CrustType.GLUTEN_FREE),
        PizzaMenuItem(8.99, Size.MEDIUM, CrustType.PAN),
        PizzaMenuItem(7.99, Size.MEDIUM, CrustType.THIN),
        PizzaMenuItem(9.99, Size.LARGE, CrustType.THIN),
        PizzaMenuItem(8.99, Size.LARGE, CrustType.BROOKLYN),
        PizzaMenuItem(10.99, Size.EXTRA_LARGE, CrustType.BROOKLYN)
    }

    #Toppings
    toppingArray = {
        ToppingMenuItem('Pepperoni', 'Small red meat circles', False),
        ToppingMenuItem('Bacon', 'Greasy Goodness', False),
        ToppingMenuItem('Italian Sausage', 'Slightly spicy', False),
        ToppingMenuItem('Pinapple', 'Yellow fruit', False),
        ToppingMenuItem('Mushrooms', 'Edible fungus', False),
        #Premium
        ToppingMenuItem('Premium Chicken', 'Fancy chicken', True),
        ToppingMenuItem('Philly Steak', 'Shreaded beef', True),
        ToppingMenuItem('Ham', 'Good with pinapple', True)
    }


    print('Creating database')
    Base.metadata.create_all(Engine)

    Session = sessionmaker(bind=Engine)    
    session = Session()

    #Add
    session.add_all(nonPizzaArray)
    session.add_all(pizzaArray)
    session.add_all(toppingArray)
    

