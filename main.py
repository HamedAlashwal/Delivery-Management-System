from enum import Enum

class OrderStatus(Enum):
    PENDING = "Pending"
    ASSIGNED = "Assigned"
    DELIVERED = "Delivered"



class Customer:
    def __init__(self, name, email, phone):
        self.__name = name
        self.__email = email
        self.__phone = phone

    # Getters
    def get_name(self):
        return self.__name

    def get_email(self):
        return self.__email

    def get_phone(self):
        return self.__phone

    # Setters
    def set_name(self, name):
        self.__name = name

    def set_email(self, email):
        self.__email = email

    def set_phone(self, phone):
        self.__phone = phone

    def place_order(self):
        """Allows the customer to place an order"""
        pass

    def track_order(self):
        """Allows the customer to track their order"""
        pass