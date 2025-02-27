from enum import Enum

class OrderStatus(Enum):
    PENDING = 1
    ASSIGNED = 2
    DELIVERED = 3



class Customer:
    def __init__(self, name, email, phone):
        self.__name = name
        self.__email = email
        self.__phone = phone

    
    def get_name(self):
        return self.__name

    def get_email(self):
        return self.__email

    def get_phone(self):
        return self.__phone

    
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


class Admin:
    def __init__(self, admin_id):
        self.__admin_id = admin_id

    
    def get_admin_id(self):
        return self.__admin_id

    
    def set_admin_id(self, admin_id):
        self.__admin_id = admin_id

    def assign_delivery(self):
        """Assigns an order to a delivery staff"""
        pass

    def generate_delivery_note(self):
        """Generates a delivery note for an order"""
        pass

    def manage_orders(self):
        """Manages order updates, cancellations, or modifications"""
        pass

class DeliveryStaff:
    def __init__(self, staff_id, location):
        self.__staff_id = staff_id
        self.__location = location

    def get_staff_id(self):
        return self.__staff_id

    def get_location(self):
        return self.__location

    def set_staff_id(self, staff_id):
        self.__staff_id = staff_id

    def set_location(self, location):
        self.__location = location

    def update_delivery_status(self):
        """Updates the status of a delivery"""
        pass

    def complete_delivery(self):
        """Marks an order as delivered"""
        pass

class Order:
    def __init__(self, order_id, items, total_amount, status):
        self.__order_id = order_id
        self.__items = items  
        self.__total_amount = total_amount
        self.__status = status

    def get_order_id(self):
        return self.__order_id

    def get_items(self):
        return self.__items

    def get_total_amount(self):
        return self.__total_amount

    def get_status(self):
        return self.__status

    def set_order_id(self, order_id):
        self.__order_id = order_id

    def set_items(self, items):
        self.__items = items

    def set_total_amount(self, total_amount):
        self.__total_amount = total_amount

    def set_status(self, status):
        if isinstance(status, OrderStatus):
            self.__status = status
        else:
            raise ValueError("Invalid status. Use OrderStatus Enum.")

    def calculate_total(self):
        """Calculates the total amount of the order"""
        pass

    def get_order_details(self):
        """Retrieves details of the order"""
        pass


class DeliveryNote:
    def __init__(self, note_id, order_id, recipient_name, address):
        self.__note_id = note_id
        self.__order_id = order_id
        self.__recipient_name = recipient_name
        self.__address = address

    
    def get_note_id(self):
        return self.__note_id

    def get_order_id(self):
        return self.__order_id

    def get_recipient_name(self):
        return self.__recipient_name

    def get_address(self):
        return self.__address

    
    def set_note_id(self, note_id):
        self.__note_id = note_id

    def set_order_id(self, order_id):
        self.__order_id = order_id

    def set_recipient_name(self, recipient_name):
        self.__recipient_name = recipient_name

    def set_address(self, address):
        self.__address = address

    def generate_note(self):
        """Generates a delivery note with order details"""
        pass