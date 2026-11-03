


import csv
import os



class Rider:

    def __init__(self, rider_id, name, status="Available",
                 total_deliveries=0):

        self.rider_id = rider_id
        self.name = name
        self.status = status
        self.total_deliveries = total_deliveries


    def assign_order(self, order_id):

        if self.status == "Available":
            self.status = "On Delivery"
            print(f"Order {order_id} assigned to {self.name}")

        else:
            print(f"{self.name} is already on delivery.")

    
    def complete_delivery(self):

        if self.status == "On Delivery":
            self.total_deliveries += 1
            self.status = "Available"
            print(f"Delivery completed by {self.name}")

        else:
            print(f"{self.name} has no active delivery.")

    def display_info(self):

        print("\n----- RIDER INFORMATION -----")
        print(f"Rider ID: {self.rider_id}")
        print(f"Name: {self.name}")
        print(f"Status: {self.status}")
        print(f"Total Deliveries: {self.total_deliveries}")



def load_riders():

    riders = []

    if os.path.exists("riders.csv"):

        with open("riders.csv", "r", newline="") as file:

            reader = csv.DictReader(file)

            for row in reader:

                rider = Rider(
                    row["rider_id"],
                    row["name"],
                    row["status"],
                    int(row["total_deliveries"])
                )

                riders.append(rider)

    else:
        riders = [
            Rider("R101", "Amit"),
            Rider("R102", "Rahul"),
            Rider("R103", "Jay")
        ]

    return riders


def save_riders(riders):

    with open("riders.csv", "w", newline="") as file:

        fieldnames = [
            "rider_id",
            "name",
            "status",
            "total_deliveries"
        ]

        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()

        for rider in riders:

            writer.writerow({
                "rider_id": rider.rider_id,
                "name": rider.name,
                "status": rider.status,
                "total_deliveries": rider.total_deliveries
            })



riders = load_riders()

while True:

    print("\n===== DELIVERY RIDER SYSTEM =====")
    print("1. Display All Riders")
    print("2. Assign Order")
    print("3. Complete Delivery")
    print("0. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        for rider in riders:
            rider.display_info()

    elif choice == "2":

        rider_id = input("Enter Rider ID: ")
        order_id = input("Enter Order ID: ")

        found = False

        for rider in riders:

            if rider.rider_id == rider_id:
                rider.assign_order(order_id)
                found = True
                break

        if not found:
            print("Rider not found.")

    elif choice == "3":

        rider_id = input("Enter Rider ID: ")

        found = False

        for rider in riders:

            if rider.rider_id == rider_id:
                rider.complete_delivery()
                found = True
                break

        if not found:
            print("Rider not found.")

    elif choice == "0":

        save_riders(riders)

        print("Rider data saved successfully!")
        print("Program closed.")
        break

    else:
        print("Invalid choice. Try again.")
