import re
import datetime  

print("💄welcome to gloss & glam shop💄\n\n")
today_date = datetime.datetime.now().strftime("%d.%m.%Y")  
available_days = "monday,tuesday,wednesday,thursday,friday"  
visit_day = input(" please Enter the day you want to visit: ").lower()
if re.search(visit_day, available_days):
    print("\n👍 The shop is open today. You can visit the store.")
if not re.search(visit_day, available_days):
    print("\n👎 The shop is closed today, but you can shop through online.")
else:
    print("invalid day")   
print("📆 Today’s date is:", today_date)
items = [(" matte lipstick", 500), ("liquid lipstick",410), ("satin lipstic", 600), ("creamy lipstick", 400)]
cart = []
def valid_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("❌ Invalid input! Please enter a number.")
def show_items():
    print("\n💄Available lipsticks:")
    for i, (name, price) in enumerate(items, 1):
        print(f"{i}. {name} - {price}")
def add_to_cart():
    show_items()
    choice = valid_input("Enter item number: ") -1
    print(f"your have entered {choice}")
    if choice < 0 or choice >= len(items):
        print("❌ Invalid choice!")
    else:
        qty = valid_input("Enter quantity: ")
        print(f"You have entered {qty}")
        cart.append((items[choice][0], items[choice][1], qty))
        print(f"✅ {qty} {items[choice][0]}(s) added!")# View cart items  
def view_cart():
    print("\n🛍️ Your Cart:")
    if not cart:
        print("Cart is empty!")
        return
    total = sum(price * qty for _, price, qty in cart)
    for i, (name, price, qty) in enumerate(cart, 1):
        print(f"{i}. {name} - {price} x {qty} = {price * qty}")
    print(f"💰 Total: {total}")
def checkout():
    if not cart:
        print("🛑 Your cart is empty!")
        return  
    total = sum(price * qty for _, price, qty in cart)
    tax = total * 0.08
    grand_total = total + tax
    print(f"\n🧾 Total: {total} + Tax ({tax:.2f}) = {grand_total:.2f}")
    with open("bill.txt", "w") as f:
        f.write(f"Total: {total}\nTax: {tax:.2f}\nGrand Total: {grand_total:.2f}")
    print("✅ Bill has been saved!")
while True:
    choice = input("\n1️⃣ Add Item 2️⃣ View Cart 3️⃣ Checkout 4️⃣ Exit: ")
    if choice == "1":
        add_to_cart()
    elif choice == "2":
        view_cart()
    elif choice == "3":
        checkout()
    elif choice == "4":
        print("👋 THANK YOU! VISIT AGAIN!")
        break
    else:
        print("❌ Invalid choice!")