from CarsideOrder import CarsideOrder
from DeliveryOrder import DeliveryOrder
from Enums import OrderType
from Order import CarryoutOrder, Order

class OrderFactory:
    @classmethod
    def create(cls, orderType, *args):
        if orderType == OrderType.CARRYOUT:
            return CarryoutOrder(*args)
        elif orderType == OrderType.CARSIDE:
            return CarsideOrder(*args)
        elif orderType == OrderType.DELIVERY:
            return DeliveryOrder(*args)

