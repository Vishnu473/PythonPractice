class FoodMenu:
    def __init__(self, food_items):
        self.food_items = food_items

    @staticmethod
    def get_category_list():
        return ['Main Course', 'Starter', 'Dessert', 'Beverage', 'Special Combo']

    def get_items_by_category(self, category):
        print("-----------------------")
        print(f"{category} Items are:",end='\n')
        found = False
        for item in self.food_items:
            if item.get_by_category(category):
                print(item)
                found = True
        if not found:
            print("No items found in this category.")

    def __str__(self):
        return "\n".join(str(item) for item in self.food_items)

class FoodItem:
    def __init__(self, name, price, category):
        if price < 0:
            raise ValueError("Price cannot be negative.")
        if category not in FoodMenu.get_category_list():
            raise ValueError(f"Invalid category: {category}")
        self.name = name
        self.price = price
        self.category = category

    def __str__(self):
        return f"{self.name} - {self.category} - ${self.price}"
    
    def __eq__(self, food_item):
        return self.name == food_item.name and self.price == food_item.price and self.category == food_item.category
        
    def __add__(self,food_item):
        if isinstance(food_item, FoodItem):
            return ComboItem('', self.price + food_item.price, "Special Combo", [self, food_item])
        raise TypeError("Can only add FoodItem to another FoodItem")

    def get_by_category(self, category):
        return self.category.lower() == category.lower()


class ComboItem(FoodItem):
    def __init__(self, name, price, category, items):
        super().__init__(name, price, category)
        self.items = items

    def __str__(self):
        item_names = ' & '.join(item.name for item in self.items)
        return f"Special Combo {item_names} - ${self.price}"
    
    

# combo1 = ComboItem("", 15.99, "Special Combo",[FoodItem("Pizza", 8.99, "Main Course"), FoodItem("Salad", 5.99, "Starter")])
# combo2 = ComboItem("", 20.99, "Special Combo", [FoodItem("Burger", 9.99, "Main Course"), FoodItem("Fries", 3.99, "Starter"), FoodItem("Soda", 2.99, "Beverage")])
# food1 = FoodItem("Biryani", 12.99, "Main Course")
# food2 = FoodItem("Spring Rolls", 4.99, "Starter")
# food3 = FoodItem("Ice Cream", 3.99, "Dessert")

# food_menu = FoodMenu([combo1, combo2, food1, food2, food3])
# print(food_menu)
# print("\nAvailable Categories:", FoodMenu.get_category_list())

# for category in FoodMenu.get_category_list():
#     food_menu.get_items_by_category(category)