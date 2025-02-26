from enum import Enum

class OrderStatus(Enum):
    PENDING = "Pending"
    ASSIGNED = "Assigned"
    DELIVERED = "Delivered"