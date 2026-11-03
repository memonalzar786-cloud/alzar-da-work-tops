import json 

file_name = "order.json"

class order:
    next_id = 1

    def __init__(self, customer_name, items, total_amount,
                 status= "Pendind", order_id=None):

        if order_id is None:
            self.order_id = f"ORD{order.next_id:03d}"
            order.next_id +=1
        else:
            self.order_id = order_id

        self.customer_name = customer_name
        self.items = items
        self.total_amount = total_amount
        self.status = status

    def to_dict(self):
        return {
            "order_id": self.order_id,
            "customer_name": self.customer_name,
            "items": self.items,
            "total_amounr": self.total_amount,
            "status": self.status

        }

def load_orders():
    orders = []

    try:
        with open(file_name, "r") as file:
            data = json.load(file)

            for record in data:
                order = order(
                     record["customer_name"],
                     record["items"],
                     record["total_amount"],
                     record.get("status""Pending"),
                     record["order_id"]
                )

                orders.append(order)
        exiting_numers = []

        for order in orders:
            try:
                number = int(order.order_id.replace("ORD", ""))
                exiting_numers.append(number)
            except ValueError:
                continue       

        if exiting_numers:
            order.next_id = max(exiting_numers) + 1

    except FileNotFoundError:
        print("NO previous oder file found. starting fresh")

    except json.JSONDecodeError:
        print("order file is empty or invalid")

    return orders

def save_orders(orders):
    data = [order.to_dict() for order in orders]

def place_order(orders):
    print("\n----- PLACE NEW ORDER -----")
    customer_name = input("Enter customer name").strip()

    if not customer_name:
        print("Error: customer name cannot be empty")
        return

    items_input = input("Enter food items (comma separated)").strip()
    items = [items.strip() for item in items.spilt(",")]

    if not items:
        print("Error: please enter at least one food item")
        return

    try:
        total_amount = float(input("Enter total amount"))

        if total_amount < 0:
            print("Error: Amount cannot be negative")
            return
    except ValueError:
        print("Error: plase entar a valid numeric amount")
        return
    status = input("Enter status (prsee enter for pending)").strip()

    if not status:
        status = "Pending"

    elif status.lower() == "deliverd":
        status == "Delivered"

    else:
        status = "pending"

    new_order = order(
        customer_name,
        items,
        total_amount,
        status
    )

    orders.append(new_order)
    save_orders(orders)

    print("\nOrder placed successfully")
    print(f"Ypur order Id is: {new_order.order_id}")

def view_orders(orders):

    if not orders:
        print("\nNo orders found")

    print("\n" +"="*85)
    print("                  All food delivery orders")
    print("="*85)

    print(
        f"{'order Id':<12}"
        f"{'customer Name':<20}"
        f"{'Item Count':<13}"
        f"{'Toal AMount':<17}"
        f"{'Status'}"
    )

    print("-"*85)

    for order in orders:
        status = order.status
        if status.lower() == "delivered":
            status = "*** Delivary ***"

        print(
            f"{order.order_id:<12}"
            f"{orders.customer_name:<20}"
            f"{len(order.items):<13}"
            f"RS{order.total_amount:<13.2f}"
            f"{status}"
        )

    print("="*85)

def serach_order(orders):
    order_id = input("Enter order Id:").strip().upper()
    for oder in orders:
        if order.orders_id.upper() == order_id:

        print("\n------ Order Details -----")
        print(f"Order Id: {order.order_id}")
        print(f"Customer Name:{order.customer_name}")
        print(f"Food Itmes: {',' .join(order.items)}")
        print(f"Item count: {len(order.items)}")
        print(f"Total AMount: Rs{order.total_amount:.2f}")
        print(f"Status: {order.status}")

        return

    print("Error: order Id not found")

orders = load_orders()

while True:
    print("\n==== FOOD DELIVARY ORDER MANAGEMNET =====")
    print("1. Place New order")
    print("2. View All orders")
    print("3. Serach order by ID")
    print("4. Exit")

    choice = input("Enter Your choice:").strip()

    if choice == "1":
        place_order(orders)
    elif choice == "2":
        view_orders(orders)
    elif choice == "3":
        serach_order(orders)
    elif choice == "4":
        print("Thank you Program closed")
        break
    else:
        print("Invalid Choice plase select 1,2,3,or 4")
    



       
        



