from config import get_connection
from mysql.connector import Error
from datetime import date

class OrderDB:
    def place_order(self, customer_id, items):  # items = [(product_id, quantity)]
        try:
            conn = get_connection()
            cursor = conn.cursor()
            conn.start_transaction()

            total = 0.0
            for product_id, quantity in items:
                cursor.execute("SELECT price, stock FROM products WHERE product_id = %s", (product_id,))
                result = cursor.fetchone()
                if not result:
                    raise Exception(f"Product ID {product_id} not found.")
                price, stock = result
                if stock < quantity:
                    raise Exception(f"Insufficient stock for product ID {product_id}.")
                total += price * quantity

            cursor.execute(
                "INSERT INTO orders (customer_id, order_date, total_amount) VALUES (%s, %s, %s)",
                (customer_id, date.today(), total)
            )
            order_id = cursor.lastrowid

            for product_id, quantity in items:
                cursor.execute("SELECT price FROM products WHERE product_id = %s", (product_id,))
                price = cursor.fetchone()[0]
                cursor.execute(
                    "INSERT INTO order_items (order_id, product_id, quantity, item_price) VALUES (%s, %s, %s, %s)",
                    (order_id, product_id, quantity, price)
                )
                cursor.execute(
                    "UPDATE products SET stock = stock - %s WHERE product_id = %s",
                    (quantity, product_id)
                )

            conn.commit()
            print(f"Order {order_id} placed successfully. Total: ₹{total:.2f}")
        except Exception as e:
            conn.rollback()
            print(f"Order failed: {e}")
        finally:
            cursor.close()
            conn.close()

    def generate_invoice(self, order_id):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("""
                SELECT o.order_id, o.order_date, o.total_amount, c.name, c.email
                FROM orders o
                JOIN customers c ON o.customer_id = c.customer_id
                WHERE o.order_id = %s
            """, (order_id,))
            order = cursor.fetchone()
            print(f"Invoice for Order #{order[0]} - Date: {order[1]} - Total: ₹{order[2]:.2f}")
            print(f"Customer: {order[3]} ({order[4]})")

            cursor.execute("""
                SELECT p.product_name, oi.quantity, oi.item_price
                FROM order_items oi
                JOIN products p ON oi.product_id = p.product_id
                WHERE oi.order_id = %s
            """, (order_id,))
            for item in cursor.fetchall():
                print(f"{item[0]} × {item[1]} @ ₹{item[2]:.2f}")
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            conn.close()

    def order_history(self, customer_id):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("""
                SELECT order_id, order_date, total_amount
                FROM orders
                WHERE customer_id = %s
                ORDER BY order_date DESC
            """, (customer_id,))
            for row in cursor.fetchall():
                print(f"Order #{row[0]} - Date: {row[1]} - Total: ₹{row[2]:.2f}")
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            conn.close()

    def sales_report(self, start_date, end_date):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("""
                SELECT order_date, SUM(total_amount)
                FROM orders
                WHERE order_date BETWEEN %s AND %s
                GROUP BY order_date
                ORDER BY order_date
            """, (start_date, end_date))
            for row in cursor.fetchall():
                print(f"{row[0]} → ₹{row[1]:.2f}")
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            conn.close()
