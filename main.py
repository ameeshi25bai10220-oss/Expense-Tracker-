from data_model import DB_FILE, green, red, yellow
import module1_input_management as m1
import module2_data_processing as m2
import module3_reporting as m3


def print_main_menu():
    print(green("💸 EXPENSE TRACKER - MAIN MENU"))
    print("-" * 40)  #to make it look clean
    print("1. Add New Expense")
    print("2. View Summary & Analytics")
    print("3. Manage/Edit/Delete Expenses")
    print("4. Exit")
    print("-" * 40)

def main():
    print(green(f"🚀 Starting Expense Tracker..."))
    
    while True:
        print_main_menu()
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            new_expense = m1.get_user_expense_details()
            if new_expense:
                m1.add_expense(new_expense)
                          
        elif choice == '2':
            expenses = m1.get_all_expenses()
            summary = m2.calculate_summary(expenses)
            
            m3.generate_monthly_report(expenses, summary)
            m2.detect_overspending(summary)
            
        elif choice == '3':
            m1.manage_expenses_menu()

        elif choice == '4':
            print(yellow("👋 Thank you for tracking your expenses."))
            break
            
        else:
            print(red("Invalid choice. Please select 1, 2, 3, or 4."))

if __name__ == "__main__":
    main()
