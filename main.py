from database import initialize_db
from manager import FinanceManager
from tabulate import tabulate # External library for professional tables
import os

def clear_screen():
    # Clears the terminal to keep the UI clean
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    initialize_db()
    fm = FinanceManager()
    
    while True:
        # clear_screen() # Uncomment if you want a super clean look
        print("\n" + "╔" + "═"*38 + "╗")
        print("║   FINTRACK: MYSQL ANALYTICS SYSTEM   ║")
        print("╚" + "═"*38 + "╝")
        print("  1. ➕ Add New Expense")
        print("  2. 📋 View Transaction History")
        print("  3. 📊 Generate Visual Analytics")
        print("  4. ❌ Exit System")
        print("═"*40)
        
        choice = input("Select an option (1-4): ")
        
        if choice == '1':
            try:
                print("\n--- NEW ENTRY ---")
                amt = float(input("Enter Amount (INR): "))
                print("Options: Food, Rent, Transport, Leisure, Bills")
                cat = input("Enter Category Name: ").capitalize()
                desc = input("Note/Description: ")
                
                if fm.add_expense(amt, cat, desc):
                    print("\n✅ DATA COMMITTED TO MYSQL SUCCESSFULLY!")
                else:
                    print("\n⚠️  ERROR: CATEGORY NOT RECOGNIZED.")
            except ValueError:
                print("\n⚠️  VALIDATION ERROR: Please enter a numeric value.")

        elif choice == '2':
            print("\n" + "═"*60)
            print("                SQL TRANSACTION LOG")
            print("═"*60)
            df = fm.get_expenses_df()
            if df.empty:
                print("No data found in MySQL server.")
            else:
                # Use tabulate for a professional table look
                print(tabulate(df, headers='keys', tablefmt='psql', showindex=False))
            input("\nPress Enter to return to menu...")

        elif choice == '3':
            print("\nLaunching Matplotlib Analytics Engine...")
            fm.generate_report()

        elif choice == '4':
            fm.close_connection()
            print("\nConnection Closed. Project Session Ended. Goodbye!")
            break

if __name__ == "__main__":
    main()