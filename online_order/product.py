from config import get_connection
from mysql.connector import Error

class ProductDB:
    def add_product(self, product_name, price, stock):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO products (product_name, price, stock) VALUES (%s, %s, %s)",
                (product_name, price, stock)
            )
            conn.commit()
            print(f"Product '{product_name}' added.")
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            conn.close()
