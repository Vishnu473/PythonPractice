from datetime import datetime
import random
from FoodItem import FoodMenu
from FoodItem import FoodItem, ComboItem
from Cart import Cart
from User import User, PremiumUser, CorporateUser
from Order import Order
from Payment import WalletPayment, UPIPayment, CashOnDeliveryPayment
from Order import OrderLogger
from Delivery import HumanRider, AutoBot

def admin_flow(menu: FoodMenu):
    print("\n--- Admin Panel ---")
    while True:
        choice = input("1. Add Food Item\n2. Add Combo Item\n3. View Menu\n4. Exit Admin\nChoose: ")

        if choice == "1":
            while True:
                name = input("Enter food name: ")
                price = float(input("Enter price: "))
                category = input("Enter category (Main Course, Starter, Dessert, Beverage): ")
                if category not in FoodMenu.get_category_list():
                    print("Invalid category. Please try again.")
                    continue
                else:
                    item = FoodItem(name, price,category)
                    break
            
            menu.add_item(item)

        elif choice == "2":
            while True:
                combo_name = input("Enter combo name: ").strip()
                try:
                    num = int(input("How many items in the combo? "))
                except ValueError:
                    print("Invalid number. Please enter an integer.")
                    continue

                items = []
                for i in range(num):
                    print(f"\nEnter details for item {i+1}:")
                    name = input("  Item name: ").strip()
                    try:
                        price = float(input("  Item price: "))
                    except ValueError:
                        print("  Invalid price. Skipping this item.")
                        continue

                    category = input("  Item category (Main Course, Starter, Dessert, Beverage): ").strip()
                    if category not in FoodMenu.get_category_list():
                        print("Invalid category. Skipping this item.")
                        continue

                    items.append(FoodItem(name, price, category))

                if not items:
                    print("No items added to combo.")
                    break

                total_price = sum(item.price for item in items)
                combo = ComboItem(combo_name, total_price, "Special Combo", items)
                menu.add_item(combo)
                print(f"Combo item '{combo_name}' added successfully.")
                break

        elif choice == "3":
            if not menu.food_items:
                print("Menu is empty. Please add items first.")
                continue
            print("\nAvailable Menu:")
            print(f"{'Item Name':<25} {'Category':<15} {'Price':>8}")
            print("-" * 50)
            for item in menu.get_items():
                print(f"{item.name:<25} {item.category:<15} ₹{item.price:>6.2f}")
            print("-" * 50)
        
        elif choice == "4":
            break

        else:
            print("Invalid option.")

def user_flow(menu: FoodMenu):
    print("\n--- Welcome to FoodieFleet ---")

# -------------------------------------------- User Registration --------------------------------
    name = input("Enter your name: ")
    try:
        wallet_balance = float(input("Enter your initial wallet balance: ₹"))
    except ValueError:
        print("Invalid wallet balance. Setting to ₹0.00. You can add money later while placing an order.")
        wallet_balance = 0.0
    mobile = input("Enter a valid 10-digit mobile number: ")
    while not User.validate_mobile_number(mobile):
        mobile = input("Enter a valid 10-digit mobile number: ")

    user_type = input("Are you a Premium User or Corporate User? (Enter 'Premium' or 'Corporate', or press Enter for Regular User): ").strip().lower()
    no_of_orders = int(input("Enter number of orders placed so far (for discount eligibility): "))

    if user_type == "premium":
        user = PremiumUser(name, mobile, wallet_balance,no_of_orders)
    elif user_type == "corporate":
        while True:
            company = input("Enter your corporate company name: ").strip()
            user_wallet_id = input("Enter your corporate user wallet ID: ").strip()

            if company in CorporateUser.corporate_list and user_wallet_id[0:3] == company.upper()[0:3]:
                user = CorporateUser(name, mobile, wallet_balance,no_of_orders,company, user_wallet_id)
            else:
                print("Invalid company or wallet ID. Please try again.")
                continue
            break
    else:
        user = User(name, mobile, wallet_balance,no_of_orders)
    
    print(f"Welcome {user.name}! Your wallet balance is ₹{user.wallet_balance:.2f}")
    
# -------------------------------------------- User Order & Cart Flow --------------------------------

    cart = Cart()

    while True:
        print("\n1. View Menu\n2. Add to Cart\n3. View Cart\n4. Place Order\n5. View Wallet\n6. Exit User\n")
        choice = input("Choose an option: ")

        # ------------------- Viewing the menu -------------------

        if choice == "1":
            try:
                if(len(menu.food_items) == 0):
                    raise ValueError("Menu is empty. Please add items first.")
                else:
                    for i, item in enumerate(menu.get_items(), 1):
                        print(f"{i}. {item}")
            except ValueError as e:
                print(e)
                continue

        # ------------------- Add items to the cart -------------------

        elif choice == "2":
            menu_items = menu.get_items()
            if not menu_items:
                print("Currently, No items available in Menu.")
                continue
            else:
                for i, item in enumerate(menu_items, 1):
                    print(f"{i}. {item}")
                idx = int(input("Enter item number: ")) - 1
                qty = int(input("Enter quantity: "))
                print("---------------------")
                for item in menu_items:
                    print(item)
                print("---------------------")
                if 0 <= idx < len(menu_items):
                    cart.add_item(menu_items[idx], qty)
                else:
                    print("Invalid item.")

        # ------------------- View Cart -------------------

        elif choice == "3":
            cart.view_cart()

        # ------------------ Placing an order ------------------

        elif choice == "4":
            if not cart.items:
                print("Cart is empty. Add items first.")
                continue

            delivery_address = input("Enter delivery address: ")
            order_id = generate_order_id()
            time_stamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            # ------------------ Payment Method Selection ------------------
            
            print("Choose payment method:\n1. Wallet\n2. UPI\n3. Cash on Delivery")
            pm = input("Enter choice: ")
            payment_method = None
            if pm == "1":
                payment = WalletPayment(user)
                payment_method = "wallet"
            elif pm == "2":
                payment = UPIPayment(user)
                payment_method = "upi"
            elif pm == "3":
                payment = CashOnDeliveryPayment(user)
                payment_method = "cod"
            else:
                print("Invalid payment method.")
                continue
            
            # --------------- Delivery Type Selection ----------------

            if payment_method == "cod":
                delivery_type = "delivery"
            else:
                delivery_type = input("Enter delivery type (delivery/takeaway): ").strip().lower()

                if delivery_type not in ['delivery', 'takeaway']:
                    print("Invalid delivery type. Defaulting to 'Delivery'.")
                    delivery_type = 'delivery'

            
            
            # ----------------- Creating Order ----------------

            order = Order(user,order_id, list(cart.items.keys()),time_stamp, delivery_address,payment_method,delivery_type)

            total = order.calculate_total()

            # ----------------- Processing Payment and delivery ----------------

            try:
                if payment_method == "wallet":
                    if payment.process_payment(total):
                        try:
                            user.place_order_from_wallet(total,order.discount )
                            print(order.print_invoice())
                            OrderLogger.log_order(order)
                            if delivery_type == 'takeaway':
                                print(f"Please collect your order from the restaurant by showing invoice.")
                            else:
                                print(handle_delivery(order))
                        except ValueError as e:
                            print(f"Error placing order at using wallet: {e}")
                            continue
                    else:
                        print("Insufficient wallet balance. Please add money to your wallet.")
                        amount = float(input("Enter amount to add to wallet: ₹"))
                        user.add_money(amount)
                        continue
                elif payment_method == "upi" or payment_method == "cod":
                    print(order.print_invoice())
                    OrderLogger.log_order(order)
                    if delivery_type == 'takeaway':
                        print(f"Please collect your order from the restaurant by showing invoice.")
                    else:
                        print(handle_delivery(order))
                    
                else:
                    print("Payment Failed.")

            except Exception as e:
                print(f"An error occurred while processing the payment using {payment_method}: {e}")
                continue
            finally:
                cart.items.clear()
        
        elif choice == "5":
            print(f"Your current wallet balance is: ₹{user.wallet_balance:.2f}")
            add_money = input("Do you want to add money to your wallet? (yes/no): ").strip().lower()
            if add_money == "yes":
                try:
                    amount = float(input("Enter amount to add to wallet: ₹"))
                    print(user.add_money(amount))
                except ValueError as e:
                    print(f"Invalid amount: {e}")
            else:
                continue

        elif choice == "6":
            break
        else:
            print("Invalid choice.")


def handle_delivery(order):
    try:
        delivery_type = random.choice(["Human", "Bot"])
        delivery_id = f"DEL{random.randint(1000, 9999)}"

        if delivery_type == "Human":
            agents = {"Ravi":101, "Anjali":102, "Suresh":103, "Meena":104, "Raj":105}
            name = random.choice(list(agents.keys()))
            agent_id = f"AGENT-{agents[name]}"
            rider = HumanRider(name, agent_id, order, delivery_type, delivery_id)
            return rider.deliver_order(order)

        else:
            bot_id = f"BOT-{random.randint(101, 105)}"
            bot = AutoBot(order, delivery_type, delivery_id, bot_id)
            return bot.deliver_order(order)
    except Exception as e:
        return f"Error in delivery process: {e}"

def generate_order_id():
    now = datetime.now()
    return f"ORD{now.strftime('%Y%m%d%H%M%S%f')}"

def main():
    menu = FoodMenu([])
    while True:
        print("\n🛒 Main Menu\n1. Admin Login\n2. User Order Flow\n3. Exit Program")
        flow = input("Choose: ")

        if flow == "1":
            admin_flow(menu)
        elif flow == "2":
            user_flow(menu)
        elif flow == "3":
            print("Exiting. Visit Again!")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
