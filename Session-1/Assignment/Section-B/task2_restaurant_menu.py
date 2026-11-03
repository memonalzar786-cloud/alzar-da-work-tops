menu = {
    "Pizza": {"price": 250, "category": "Fast Food"},
    "Burger": {"price": 120, "category": "Fast Food"},
    "Pasta": {"price": 180, "category": "Italian"},
    "Dosa": {"price": 80, "category": "South Indian"},
    "Sandwich": {"price": 100, "category": "Fast Food"},
    "Idli": {"price": 60, "category": "South Indian"}
}

def view_menu():
    print(f"----- RESTAURANT MENU -----")
    print("No.   Dish       Price    Caegory")

    for number, (dish,detail) in enumerate(menu.items(), start=1):
        print(
            f"{number}. {dish:<12} ₹{details["price"]:<9}"
            f"{delails["category"]}"
        )

def filter_category():
    category = input("Enter category:  ").strip()

    print(f"\n---- {category} MENU ----")
    found = False

    for dish,details in menu.items():
        if details["category"].lower() == category.lower():
            print(f"{dish} - ₹{details}['price']")
            found = True

    if not found:
        print("category not found")

def search_dish():
    dish_name = input("Enter your dish name").strip()

    if dish_name.lower() in [dish.lower() for dishin in menu]:
       for dish, details in menu.items():
           if dish.lower() == dish_name.lower():
               print(f"{dish} price: ₹{details['price']}")
               return

    print("Dish not found")

while True:
    print("\n===== RESTARURANT MENU MANAGER =====")
    print("1. View All menu")
    print("2. Filter by category")
    print("3. Search Dish")
    print("0. Exit")
                  
    choice = input("Enter your choice")

    if choice == "1":
        view_menu()

    elif choice == "2":
        filter_category()

    elif choice == "3":
        search_dish()

    elif choice == "0":
        print("Than you! program closed")
        break 
    else:
        print("Invalid choice: please try again.")

     
