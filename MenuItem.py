from Enums import CrustType, Size
from sqlDb import Base
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Enum, Boolean

class MenuItem(Base):
    next_id = 1

    def __init__(self, name, price, description):
        self.name = name
        self.price = price
        self.description = description

        self.id = MenuItem.next_id
        MenuItem.next_id += 1
    
    __tablename__ = 'menu'

    id = Column(Integer, primary_key = True)
    name = Column(String)
    price = Column(Float)
    description = Column(String)
    type = Column(String)

    __mapper_args__ = {
        "polymorphic_identity": "menu",
        "polymorphic_on": type,
    }

    def __repr__(self):
        return "<MenuItem(name={}, price={}, description={})>".format(self.name, self.price, self.description)



class PizzaMenuItem(MenuItem):
    def __init__(self, price, size, crust):
        name = '{} Pizza'.format(size)
        description = 'Cheese pizza with {} crust'.format(crust)

        super().__init__(name, price, description)
        self.size = size
        self.crust = crust

    __tablename__ = 'menuPizza'

    id = Column(Integer, ForeignKey("menu.id"), primary_key = True)
    size = Column(Enum(Size))
    crust = Column(Enum(CrustType))

    __mapper_args__ = {
        "polymorphic_identity": "menuPizza",
    }

    def __repr__(self):
        return "<PizzaMenuItem(name={}, price={}, description={}, size = {}, crust = {})>".format(
            self.name, self.price, self.description, self.size, self.crust)

class ToppingMenuItem(MenuItem):
    def __init__(self, name, description, isPremium):
        super().__init__(name, 0, description)
        self.isPremium = isPremium
        #Want to display lowest price by default
        self.updatePrice(size = Size.SMALL)

    __tablename__ = 'menuTopping'

    id = Column(Integer, ForeignKey("menu.id"), primary_key = True)
    isPremium = Column(Boolean)

    __mapper_args__ = {
        "polymorphic_identity": "menuTopping",
    }

    def updatePrice(self, size):
        if(self.isPremium):
            premiumPriceArray = [1.5, 2, 2.5, 3]
            self.price = premiumPriceArray[size.value]
        else:
            regularPriceArray = [1, 1.5, 2, 2.25]
            self.price = regularPriceArray[size.value]
    
    def __repr__(self):
        return "<ToppingMenuItem(name={}, price={}, description={}, isPremium = {})>".format(
            self.name, self.price, self.description, self.isPremium)


