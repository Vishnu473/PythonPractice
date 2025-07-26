from abc import abstractmethod, ABC

class Payment(ABC):
    @abstractmethod
    def process_payment(self, amount) -> bool:
        pass

class WalletPayment(Payment):
    def __init__(self, user):
        self.user = user

    def process_payment(self, amount) -> bool:
        if amount <= self.user.wallet_balance:
            self.user.place_order(amount)
            return True
        return False
    
class UPIPayment(Payment):
    def __init__(self,user):
        self.user = user

    def process_payment(self, amount):
        print(f"Payment of {amount} successful by {self.user.name}.")
        return True
    
class CashOnDeliveryPayment(Payment):
    def __init__(self, user):
        self.user = user

    def process_payment(self, amount):
        print(f"Payment of {amount} will be collected from {self.user.name} upon delivery.")
        return True