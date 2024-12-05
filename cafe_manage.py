# Define the menu with Indian foods
menu = {
    1: ("Samosa", 30),
    2: ("Paneer Tikka", 150),
    3: ("Chole Bhature", 120),
    4: ("Aloo Paratha", 80),
    5: ("Masala Dosa", 100),
    6: ("Butter Chicken", 250),
    7: ("Biryani", 180),
    8: ("Pav Bhaji", 90),
    9: ("Chaat", 50),
    10: ("Lassi", 60)
}

# Display the menu
print("\nMenu:")
for key, (item, price) in menu.items():
    print(f"{key}. {item} - Rs{price:.2f}")

# Initialize an empty order list
order = []

# Take order from user
while True:
    choice = int(input("\nEnter item number to order (0 to finish): "))
    if choice == 0:
        break
    if choice in menu:
        quantity = int(input("Enter quantity: "))
        order.append((menu[choice], quantity))
    else:
        print("Invalid choice, try again.")

# Show order summary and calculate total
total = 0
print("\nYour Order:")
for (item, price), quantity in order:
    print(f"{item} x {quantity} - Rs{price * quantity:.2f}")
    total += price * quantity

print(f"\nTotal: Rs{total:.2f}")
print("\nThank you for visiting!")
