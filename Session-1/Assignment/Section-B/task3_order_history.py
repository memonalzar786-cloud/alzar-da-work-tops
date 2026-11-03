import json

file_name = "oders.json"

def load_orders():
    try:
        with open(file_name, "r") as file:
            orders = json.load(file)
            return orders

    except FileNotFoundError:
        return[]

def save_orders(orders):
    with open(file_name, "w") as file:
        json.dump(orders, file, indent=4)

def add_orders():
    try:
        customer_name = input("Enter your name")

        items_input = input("Enter your item(Comma separated):")
        items = [item.strip() for item in items_input.split(",")]

        total_amount = float(input("Enter order status:"))
        order_status = input("Enter your status")

        if not customer_name.strip():
            print("Error: customer cannot be negative")
            return

        if total_amount <0:
            print("Error: amount cannot be negative")
            return

        if not items_input.strip():
            print("Error: food items cannot be negative")
            return

        new_order = {
            "customer_name" :customer_name,
            "Items" : items,
            "Total amoint" : total_amount,
            "order_status": order_status
        }

        orders = load_orders()
        orders.append(new_order)

        save_orders(orders)
        print("order saved successfuly")

    except ValueError:
        print("Error: please enter a valid numeric amount")

def view_orders():
    orders = load_orders()

    if not orders:
        print("No order history found")
        return

    print("\n------ORDER HISTORT-----")

    for number, order in enumerate(orders, start=1):
        print(f"\nOrder No: {number}")
        print(f"Customer Name: {order['customer_name']}")
        print(f"Food Items: {', '.json(order['items'])}")
        print(f"Total amount: ₹{order['total_amount']:.2f}")
        print(f"Order Status: {order['order_status']}")

while True:
    print("\n===== ORDER HISTORY SYSTEM =====")
    print("1. Add new order")
    print("2. View order")
    print("0. Exit")

    choice = input("Enter your choice")

    if choice == "1":
        add_orders()

    elif choice == "2":
        view_orders()

    elif choice == "0":
        print("Program Closed")
        break


    else:
        print("Invalid choice. Try again")






