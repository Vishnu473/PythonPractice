from random import randint

class User: #discount of 1-3% is applied if min. order are greater than 50

    def __init__(self,name,mobile_number,wallet_balance, min_orders=50):
        self.name = name
        self.mobile_number = mobile_number
        self.__wallet_balance = wallet_balance
        self.min_orders = min_orders

    @property
    def wallet_balance(self):
        return self.__wallet_balance

    def add_money(self, amount):
        if amount < 0:
            raise ValueError("Cannot add negative amount to wallet")
        self.__wallet_balance += amount
        return f"Money added successfully! New balance: {self.wallet_balance}"


    @staticmethod
    def validate_mobile_number(mobile_number):
        try:
            if  len(mobile_number) == 10 and mobile_number.isdigit():
                return True
        except ValueError:
            print("Invalid mobile number. It should be a 10-digit number.")
            return False


    def place_order_from_wallet(self,order_amount,discount=None):
        try:
            if order_amount < 0:
                    raise ValueError("Order amount cannot be negative")
            if order_amount > self.wallet_balance:
                raise ValueError("Insufficient wallet balance to place the order. Add money into wallet")
            
            if discount is None:
                discount = self.calculate_discount()
            
            final_amount = order_amount - (order_amount * discount / 100)
            self.__wallet_balance -= final_amount
        
            if discount > 0:
                return f"Order placed successfully with a discount of {discount}%! Final amount paid: ₹{final_amount:.2f}"
            return f"Order placed successfully! Amount paid: ₹{final_amount:.2f}"
        except ValueError as e:
            return f"Error placing order: {e}"
    
    def place_order(self,order_amount,discount=None):
        try:
            if order_amount < 0:
                    raise ValueError("Order amount cannot be negative")
            if discount is None:
                discount = self.calculate_discount()
            final_amount = order_amount - (order_amount * discount / 100)
            if discount > 0:
                return f"Order placed successfully with a discount of {discount}%! Final amount to be paid: ₹{final_amount:.2f}"
            return f"Order placed successfully! Amount to be paid: ₹{final_amount:.2f}"
        except ValueError as e:
            return f"Error placing order: {e}"
        
    def discount_eligibility(self):
        if self.min_orders > 50:
            return True
        return False
    
    def calculate_discount(self):
        if self.discount_eligibility():
            return randint(1,4)
        return 0

    
class PremiumUser(User): #Guaranteed discount upto 10% from 3% if min_order > 10 else 1% - 3%

    def __init__(self, name, mobile_number, wallet_balance,min_orders=10):
        super().__init__(name,mobile_number,wallet_balance,min_orders)

    def calculate_discount(self):
        return randint(5,10) if self.min_orders > 10 else randint(1,3)

    def place_order(self, order_amount):
        discount = self.calculate_discount()
        final_order_amount = order_amount - (order_amount * discount / 100)
        return super().place_order(final_order_amount,discount)
    

class CorporateUser(PremiumUser): #Guaranteed discount from 10 to 15% if a user is a corporateUser

    corporate_list = ['Google', 'Amazon', 'TCS', 'Microsoft', 'Tesla']

    def __init__(self, name, mobile_number, wallet_balance,min_orders,company,user_wallet_id):
        super().__init__(name,mobile_number,wallet_balance,min_orders)
        self.company = company
        self.user_wallet_id = user_wallet_id
    
    def calculate_discount(self):
        if self.company in CorporateUser.corporate_list and self.user_wallet_id[0:3] == self.company.upper()[0:3]:
            return randint(10,15)
        return super().calculate_discount() 
    
    def place_order(self,order_amount):
        discount = self.calculate_discount()
        final_order_amount = order_amount - (order_amount * discount / 100)
        return super().place_order(final_order_amount,discount)

    