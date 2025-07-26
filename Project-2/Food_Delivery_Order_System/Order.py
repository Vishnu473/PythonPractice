
class Order:

    def __init__(self, user,order_id, items,time_stamp,address,payment_method,delivery_type):
        self.user = user
        self.order_id = order_id
        self.items = items
        self.time_stamp = time_stamp
        self.address = address
        self.payment_method = payment_method
        self.delivery_type = delivery_type

    def calculate_total(self):
        return sum(item.price for item in self.items)
    
    def generate_invoice(self):
        discount = self.user.calculate_discount()
        total_amount = self.calculate_total()
        order_amount = total_amount - (total_amount * discount / 100) if discount > 0 else total_amount

        invoice = f"Order ID: {self.order_id}\n"
        invoice += f"User: {self.user.name}\n"
        invoice += f"Time: {self.time_stamp}\n"
        invoice += "Items:\n"
        for item in self.items:
            invoice += str(item)
        invoice += f"\nTotal Amount: ${total_amount:.2f}\n"
        invoice += f"Order Amount after Discount: ${order_amount:.2f}\n"
        return invoice
    
    def print_invoice(self):
        discount = self.user.calculate_discount()
        total_amount = self.calculate_total()
        order_amount = total_amount - (total_amount * discount / 100) if discount > 0 else total_amount

        order_invoice = f"Order ID: {self.order_id}" + "\n"
        order_invoice += f"Order booked by {self.user.name} at {self.time_stamp}. The ordered items are: " + "\n"
        order_invoice += "----------------------------------" + "\n"
        for item in self.items:
            order_invoice += str(item)
        order_invoice += "\n" + "----------------------------------"
        order_invoice += "\n"+f"Total Order amount for {len(self.items)} items - ${self.calculate_total()} /-"
        order_invoice += "\n" + f"Discount applied: {discount}%"
        order_invoice += "\n" + f"Final Order amount after discount: ${order_amount:.2f} /-"
        order_invoice += "\n" + "----------------------------------"
        order_invoice += "\n" + f"Payment Method opted: {self.payment_method}"
        order_invoice += "\n" + "----------------------------------"
        if self.delivery_type.lower() == 'takeaway':
            order_invoice += "\n" + "Delivery opted: takeaway! \n Contact user at: " + self.user.mobile_number
        else:
            order_invoice += "\n"+f"Order to be delivered at {self.address} by our delivery agent soon."+"\n"+f"Contact user at: {self.user.mobile_number}."
        order_invoice += "\n" + "----------------------------------"
        order_invoice += "\n" + "Thank you for ordering with us! We hope you enjoy your meal!"
        return order_invoice

class OrderLogger:
    @staticmethod
    def log_order(order):
        with open("orders.txt", "a") as file:
            file.write(str(order) + "\n\n")
        print("Order logged successfully.")
    
    @staticmethod
    def read_orders():
        try:
            with open("orders.txt", "r") as file:
                return file.read()
        except FileNotFoundError:
            return "No orders found."
