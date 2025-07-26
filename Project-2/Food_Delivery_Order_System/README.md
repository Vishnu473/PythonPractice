**FoodieFleet – A Food Delivery Order System**

*Problem Statement*:

Design and implement a simplified food delivery order management system using Python, where customers can place orders, and delivery agents (human or bots) fulfill them. This system demonstrates object-oriented programming principles and file handling techniques.

1. User Module

    class User

        Attributes: name, mobile, wallet_balance

        Use @property, getter/setter to protect wallet_balance

        Method: place_order()

    class PremiumUser(User)

        Inherits from User

        Overrides place_order() to apply discount

        Multi-level inheritance: (ex: User -> PremiumUser -> CorporateUser if needed)

        <!-- @classmethod:

        User.from_csv(cls, csv_line: str) → Creates user from file line -->

        @staticmethod:

        validate_mobile(mobile: str) → Returns True if mobile number is valid

2. Food Item Module

    class FoodItem

        Attributes: name, price, category (starter/main/dessert)

        Magic methods:

        __str__() → Printable format

        __eq__() → Compare if two food items are same

        __add__() → Combine two items to return a ComboItem

    class ComboItem(FoodItem)

        Inherits from FoodItem

        Combines names/prices of two items

        Override __str__() to indicate combo

3. Order Module

    class Order

        Attributes: order_id, user, items, total_amount, timestamp

        Method: calculate_total(), __str__()

    File I/O:

        OrderLogger.log_order(order: Order) → Appends to orders.txt

        OrderLogger.read_orders() → Reads and displays past orders

4. Delivery System Module

    Abstract Base Class:
        
    class DeliveryAgent(ABC)

        Method (abstract):
        deliver_order(order: Order)

    class Person

        Attributes: name, agent_id

    class HumanRider(Person, DeliveryAgent)

        Implements deliver_order()

        Use super() to initialize base

    class AutoBot(DeliveryAgent)

        Attributes: bot_id

        Implements deliver_order()

5. Payment Module:

    Abstract Base Class:
    
    class PaymentMode(ABC)

        Method (abstract): process_payment(amount: float) -> bool


    class Wallet(PaymentMode)

        Deducts amount from user's wallet

        Fails if insufficient funds

    class UPI(PaymentMode)

        Prints message simulating payment

    class CashOnDelivery(PaymentMode)

        Always returns True (pay on delivery)