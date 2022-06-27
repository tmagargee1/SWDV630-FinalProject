from enum import Enum

def enumNameFormatter(name):
    return name.title().replace("_", " ")

class PaymentMethod(Enum):
    CASH = 0
    GIFT_CERTIFICATE = 1
    CARD = 2
    
    def __str__(self):
        return enumNameFormatter(self.name)

class Size(Enum):
    SMALL = 0
    MEDIUM = 1
    LARGE = 2
    EXTRA_LARGE = 3

    def __str__(self):
        return enumNameFormatter(self.name)

class CrustType(Enum):
    HAND_TOSSED = 1
    THIN = 2
    BROOKLYN = 3
    GLUTEN_FREE = 4
    PAN = 5

    def __str__(self):
        return enumNameFormatter(self.name)

class OrderType(Enum):
    CARRYOUT = 1
    CARSIDE = 2
    DELIVERY = 3

    def __str__(self):
        return enumNameFormatter(self.name)

class Tab(Enum):
    QUIT = -1
    ACCOUNT = 1
    MENU = 2
    ORDER = 3
    COMPLETE = 4

    def __str__(self):
        return enumNameFormatter(self.name)
