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
    HAND_TOSSED = 0
    THIN = 1
    BROOKLYN = 2
    GLUTEN_FREE = 3
    PAN = 4

    def __str__(self):
        return enumNameFormatter(self.name)

class OrderType(Enum):
    CARRYOUT = 0
    CARSIDE = 1
    DELIVERY = 2

    def __str__(self):
        return enumNameFormatter(self.name)

class Tab(Enum):
    QUIT = -1
    MENU = 1
    ORDER = 2
    ACCOUNT = 3

    def __str__(self):
        return enumNameFormatter(self.name)
