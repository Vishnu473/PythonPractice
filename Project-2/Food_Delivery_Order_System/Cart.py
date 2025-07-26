from FoodItem import FoodItem, ComboItem

class Cart:

    def __init__(self):
        self.items = {}

    def add_item(self, item, quantity):
        if not isinstance(item, (FoodItem, ComboItem)):
            raise TypeError("Only FoodItem or ComboItem can be added.")

        if item in self.items:
            self.items[item] += quantity
        else:
            self.items[item] = quantity

    def remove_item(self, item):
        if item in self.items:
            del self.items[item]
        else:
            raise ValueError("Item not found in the cart.")

    def view_cart(self):
        if not self.items:
            return "Cart is empty."

        print("\nCart Summary:")
        total = 0
        for item, qty in self.items.items():
            print(f"{item} | Qty: {qty} | Subtotal: ${item.price * qty:.2f}")
            total += item.price * qty
        print(f"Total: ${total:.2f}")

    def clear_cart(self):
        self.items.clear()