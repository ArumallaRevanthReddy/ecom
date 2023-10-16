from enum import Enum

class OrderStatus(Enum):
    ORDERED = 1
    INTRANSIT = 2
    DELIVERED = 3

    @classmethod
    def order_status(cls):
        return [(item.value, item.name) for item in cls]