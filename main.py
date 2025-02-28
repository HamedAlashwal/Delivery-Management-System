from enum import Enum

class OrderStatus(Enum):
    PENDING = 1
    ASSIGNED = 2
    DELIVERED = 3



class Customer:
    def __init__(self, name, email, phone, address):
        """Initializes a Customer with personal details."""
        self.__name = name
        self.__email = email
        self.__phone = phone
        self.__address = address

    def get_name(self):
        return self.__name

    def get_email(self):
        return self.__email

    def get_phone(self):
        return self.__phone
    
    def get_address(self):
        return self.__address

    def set_name(self, name):
        self.__name = name

    def set_email(self, email):
        self.__email = email

    def set_phone(self, phone):
        self.__phone = phone
    
    def set_address(self, address):
        self.__address = address

    def place_order(self):
        """Allows the customer to place an order."""
        pass

    def track_order(self):
        """Allows the customer to track their order."""
        pass


class Admin:
    def __init__(self, admin_id):
        """Initializes an Admin with a unique ID."""
        self.__admin_id = admin_id

    def get_admin_id(self):
        return self.__admin_id

    def set_admin_id(self, admin_id):
        self.__admin_id = admin_id

    def assign_delivery(self):
        """Assigns an order to a delivery staff."""
        pass

    def generate_delivery_note(self):
        """Generates a delivery note for an order."""
        pass

    def manage_orders(self):
        """Manages order updates, cancellations, or modifications."""
        pass

class DeliveryStaff:
    def __init__(self, staff_id, location):
        """Initializes Delivery Staff with an ID and location."""
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
        """Updates the status of a delivery."""
        pass

    def complete_delivery(self):
        """Marks an order as delivered."""
        pass

class Order:
    def __init__(self, order_id, items, status):
        """Initializes an Order with items and status."""
        self.__order_id = order_id
        self.__items = items  
        self.__total_amount = 0 
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

    def set_status(self, status):
        self.__status = status

    def get_order_details(self):
        """Retrieves details of the order"""
        pass
    
    def calculate_total(self):
        """Calculates the total amount of the order."""
        total = 0
        for item in self.__items:
            total_price = item[2] * item[3]
            total = total + total_price
        self.__total_amount = total

class DeliveryNote:
    def __init__(self, note_id, order, customer, delivery_date, delivery_method, package_weight):
        """Initializes a Delivery Note with all necessary details."""
        self.__note_id = note_id
        self.__order = order
        self.__customer = customer
        self.__delivery_date = delivery_date
        self.__delivery_method = delivery_method
        self.__package_weight = package_weight
    
    def get_note_id(self):
        return self.__note_id

    def get_order(self):
        return self.__order

    def get_customer(self):
        return self.__customer

    def get_delivery_date(self):
        return self.__delivery_date

    def get_delivery_method(self):
        return self.__delivery_method

    def get_package_weight(self):
        return self.__package_weight

    def display_note(self):
        """Displays the delivery note details."""
        print("=" * 50)
        print("            DELIVERY NOTE")
        print("=" * 50)
        print("\nThank you for using our delivery service! Please print your delivery receipt and present it upon receiving your items.")
        
        print("\nRecipient Details:")
        print("Name:-", self.__customer.get_name())
        print("Contact:-", self.__customer.get_email())
        print("Delivery Address:-", self.__customer.get_address())

        print("\nDelivery Information:")
        print("Order Number:-", self.__order.get_order_id())
        print("Reference Number:-", self.__note_id)
        print("Delivery Date:-", self.__delivery_date)
        print("Delivery Method:-", self.__delivery_method)
        print("Package Dimensions:")
        print("Total Weight:-", str(self.__package_weight), " kg")

        print("\nSummary of Items Delivered:")
        print("%-10s %-25s %-10s %-16s %-15s" % ("Item Code", "Description", "Quantity", "Unit Price (AED)", "Total Price (AED)"))
        print("-" * 75)

        subtotal = 0

        items = self.__order.get_items()
        for item in items:
            item_code = item[0]
            description = item[1]
            quantity = item[2]
            unit_price = item[3]
            total_price = quantity * unit_price
            subtotal = subtotal + total_price

            print("%-10s %-25s %-10d %-16.2f %-15.2f" % (item_code, description, quantity, unit_price, total_price))


        taxes_fees = subtotal * 0.05
        total = subtotal + taxes_fees

        print("\nSubtotal:- AED %.2f" % subtotal)
        print("Taxes and Fees:- AED %.2f" % taxes_fees)
        print("\nTotal Charges:- AED %.2f" % total)
        print("=" * 50)
        
        

customer = Customer("Sarah Johnson", "sarah.johnson@example.com", "+971 50 123 4567", "45 Knowledge Avenue, Dubai, UAE")

items = [
    ("ITM001", "Wireless Keyboard", 1, 100.00),
    ("ITM002", "Wireless Mouse & Pad Set", 1, 75.00),
    ("ITM003", "Laptop Cooling Pad", 1, 120.00),
    ("ITM004", "Camera Lock", 3, 15.00)
]

order = Order("DEL123456789", items, OrderStatus.DELIVERED)
order.calculate_total()

delivery_note = DeliveryNote("DN-2025-001", order, customer, "January 25, 2025", "Courier", 7)

delivery_note.display_note()
