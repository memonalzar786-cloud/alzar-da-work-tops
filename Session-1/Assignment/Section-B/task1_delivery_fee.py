order_value = float(input("Enter order value"))
distance = float(input("Enter order value"))

if order_value < 0 or distance <0:
    print("Error: order value and distance cannot be negetive")

else:
    if order_value >=500:
        delivery_fee = 0
    elif distance <=5:
        delivery_fee = 30
    else:
        delivery_fee = 60

final_amount = order_value+delivery_fee

print("\n----- Bill Sumrray -----")
print(f"Item Total    :₹{order_value:.2f}")
print(f"Delivery fee  :₹{delivery_fee:.2f}")
print(f"Final Amount  :₹{final_amount:.2f}")

    