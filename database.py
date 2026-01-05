import mysql.connector
from mysql.connector import Error

def initialize_db():
    conn = None # Initialize as None to avoid UnboundLocalError
    try:
        # Step A: Connect to MySQL Server
        # IMPORTANT: Replace 'root123' with your ACTUAL MySQL password
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="satyam391" 
        )
        
        if conn.is_connected():
            cursor = conn.cursor()
            
            # Step B: Create and Use Database
            cursor.execute("CREATE DATABASE IF NOT EXISTS fin_track_db")
            cursor.execute("USE fin_track_db")
            print("Database 'fin_track_db' is ready.")

            # Step C: Categories Table (Normalization) [cite: 15]
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS categories (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(50) NOT NULL UNIQUE
                )
            ''')

            # Step D: Expenses Table with Foreign Key [cite: 15, 16]
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS expenses (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    amount DECIMAL(10, 2) NOT NULL,
                    category_id INT,
                    description TEXT,
                    date_created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (category_id) REFERENCES categories(id)
                )
            ''')

            # Step E: Insert default categories
            default_cats = [('Food',), ('Rent',), ('Transport',), ('Leisure',), ('Bills',)]
            cursor.executemany('INSERT IGNORE INTO categories (name) VALUES (%s)', default_cats)

            conn.commit()
            print("MySQL Tables initialized successfully!")

    except Error as e:
        print(f"Error while connecting to MySQL: {e}")
        print("\nTIP: Make sure your MySQL password is correct and the service is running.")

    finally:
        if conn and conn.is_connected():
            cursor.close()
            conn.close()
            print("MySQL connection closed.")

if __name__ == "__main__":
    initialize_db()