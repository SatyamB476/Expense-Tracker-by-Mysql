import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt

class FinanceManager:
    def __init__(self):
        # Step A: Connect to your live MySQL Server
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="satyam391", # Use your Workbench password
            database="fin_track_db"
        )
        self.cursor = self.conn.cursor()

    def add_expense(self, amount, category_name, description):
        """Finds category ID and inserts a new expense into MySQL."""
        self.cursor.execute("SELECT id FROM categories WHERE name = %s", (category_name,))
        result = self.cursor.fetchone()
        
        if result:
            category_id = result[0]
            query = "INSERT INTO expenses (amount, category_id, description) VALUES (%s, %s, %s)"
            self.cursor.execute(query, (amount, category_id, description))
            self.conn.commit()
            return True
        return False

    def get_expenses_df(self):
        """Fetches data using SQL JOIN and returns a Pandas DataFrame for analysis."""
        query = """
            SELECT e.amount, c.name as category, e.description, e.date_created as date 
            FROM expenses e 
            JOIN categories c ON e.category_id = c.id
        """
        # This fulfills your resume skill in Data Handling & SQL [cite: 15]
        return pd.read_sql_query(query, self.conn)

    def generate_report(self):
        """Uses Matplotlib to visualize MySQL data trends."""
        df = self.get_expenses_df()
        if df.empty:
            print("\n>>> No data in MySQL. Add expenses first!")
            return

        summary = df.groupby('category')['amount'].sum()

        plt.figure(figsize=(10, 7))
        colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0']
        
        summary.plot(
            kind='pie', 
            autopct='%1.1f%%', 
            startangle=140, 
            colors=colors,
            wedgeprops={'edgecolor': 'white', 'linewidth': 2}
        )

        plt.title('MySQL Data: Spending Distribution', fontsize=16)
        plt.ylabel('')
        plt.show()

    def close_connection(self):
        if self.conn.is_connected():
            self.cursor.close()
            self.conn.close()