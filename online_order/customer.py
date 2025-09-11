from config import get_connection
from mysql.connector import Error

class CustomerDB:
    def add_customer(self, name, email):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO customers (name, email) VALUES (%s, %s)",
                (name, email)
            )
            conn.commit()
            print(f"Customer '{name}' added.")
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            conn.close()
