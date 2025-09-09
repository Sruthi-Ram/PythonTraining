from ecommerce import cart, payment

while True:
    action = input("Choose action (add/remove/checkout): ").strip().lower()
    
    if action == "add":
        name = input("Enter item name: ")
        price = float(input("Enter item price: "))
        cart.add_item(name, price)
    elif action == "remove":
        name = input("Enter item name to remove: ")
        cart.remove_item(name)
    elif action == "checkout":
        total = cart.calculate_total()
        print("Total amount:", total)
        success = payment.process_payment(total)
        if success:
            print("Payment successful")
        else:
            print("Payment failed")
        break
    else:
        print("Invalid action")
