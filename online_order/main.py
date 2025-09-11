from customer import CustomerDB
from product import ProductDB
from order import OrderDB

customer_db = CustomerDB()
product_db = ProductDB()
order_db = OrderDB()

# Add customer
customer_db.add_customer("Bob", "bob@example.com")

# Add products
product_db.add_product("Laptop", 50000.0, 10)
product_db.add_product("Mouse", 500.0, 50)

# Place order: Bob orders 2 Laptops and 1 Mouse
order_db.place_order(1, [(1, 2), (2, 1)])

# Generate invoice
order_db.generate_invoice(1)

# View Bob's order history
order_db.order_history(1)

# Sales report for today
order_db.sales_report("2025-09-11", "2025-09-11")
