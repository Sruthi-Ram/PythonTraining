cart_items = []

def add_item(name, price):
    cart_items.append({'name': name, 'price': price})

def remove_item(name):
    global cart_items
    cart_items = [item for item in cart_items if item['name'] != name]

def calculate_total():
    return sum(item['price'] for item in cart_items)
