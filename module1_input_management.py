import sqlite3
from typing import List, Optional, Any
from data_model import Expense, DB_FILE, CATEGORIES, green, red, yellow

def db_execute(query: str, params: tuple = ()) -> Optional[List[Expense]]:
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    try:
        cursor.execute(query, params)
        if query.strip().upper().startswith('SELECT'):
            expenses = []
            for row in cursor.fetchall():
                expenses.append(Expense(id=row[0], name=row[1], amount=row[2], category=row[3], date=row[4]))
            return expenses
        conn.commit()
        return None
    except sqlite3.Error as e:
        print(f"{red('DB Error:')} {e}")
        return None
    finally:
        conn.close()

def get_all_expenses() -> List[Expense]:
    return db_execute("SELECT id, name, amount, category, date FROM expenses ORDER BY date DESC") or []

def add_expense(expense: Expense):
    query = "INSERT INTO expenses (name, amount, category, date) VALUES (?, ?, ?, ?)"
    params = (expense.name, expense.amount, expense.category, expense.date)
    db_execute(query, params)
    print(f"{green('✅ SUCCESS:')} Added {expense.category} expense: {expense.name} (Rs.{expense.amount:.2f}).")

def get_user_expense_details():
    print(yellow("\n--- Enter New Expense ---"))
    expense_name = input("Enter description (e.g., 'Groceries', 'Rent'): ")
    while True:
        try:
            expense_amount = float(input("Enter amount spent: Rs. "))
            if expense_amount <= 0: continue
            break
        except ValueError:
            print(red("Invalid amount. Please enter a number."))
    while True:
        print("\nSelect a category:")
        for i, category_name in enumerate(CATEGORIES):
            print(f"  {i + 1}. {category_name}")
        try:
            selected_index = int(input(f"Enter category number [1 - {len(CATEGORIES)}]: ")) - 1
            if 0 <= selected_index < len(CATEGORIES):
                selected_category = CATEGORIES[selected_index]
                break
            else:
                print(red("Invalid category number."))
        except ValueError:
            print(red("Invalid input. Please enter a number."))
    expense_date = input(f"Enter date (YYYY-MM-DD) or press Enter for today: ")
    if not expense_date:
        expense_date = Expense(name='', amount=0, category='').date
    return Expense(
        name=expense_name, 
        category=selected_category, 
        amount=expense_amount,
        date=expense_date
    )

def delete_expense(expense_id: int):
    query = "DELETE FROM expenses WHERE id = ?"
    db_execute(query, (expense_id,))
    print(f"{green('✅ SUCCESS:')} Deleted expense ID {expense_id}.")

def edit_expense(expense_id: int, new_amount: float, new_category: str):
    query = "UPDATE expenses SET amount = ?, category = ? WHERE id = ?"
    db_execute(query, (new_amount, new_category, expense_id))
    print(f"{green('✅ SUCCESS:')} Updated expense ID {expense_id} to Rs.{new_amount:.2f} in {new_category}.")

def manage_expenses_menu():
    expenses = get_all_expenses()
    if not expenses:
        print(yellow("No expenses to manage."))
        return
        
    print(yellow("\n--- Current Expenses for Management ---"))
    print(f"{'ID':<4} | {'Date':<10} | {'Category':<15} | {'Amount':<10} | {'Description'}")
    print("-" * 60)
    for exp in expenses:
        print(f"{exp.id:<4} | {exp.date:<10} | {exp.category:<15} | Rs.{exp.amount:<9.2f} | {exp.name}")
        
    while True:
        try:
            choice = input(yellow("\nEnter ID to [E]dit, [D]elete, or [B]ack to Main Menu: ")).upper()
            if choice == 'B': return
            if choice in ('E', 'D'):
                exp_id = int(input("Enter the ID number to manage: "))
                if not any(e.id == exp_id for e in expenses):
                    print(red("Invalid ID."))
                    continue
                if choice == 'D':
                    confirm = input(f"Delete ID {exp_id}? (Y/N): ").upper()
                    if confirm == 'Y': delete_expense(exp_id)
                    return
                elif choice == 'E':
                    new_amount = float(input(f"Enter new amount for ID {exp_id}: "))
                    print("\nSelect a new category:")
                    for i, category_name in enumerate(CATEGORIES):
                        print(f"  {i + 1}. {category_name}")
                    cat_index = int(input(f"Enter new category number [1 - {len(CATEGORIES)}]: ")) - 1
                    new_category = CATEGORIES[cat_index]
                    edit_expense(exp_id, new_amount, new_category)
                    return
            else:
                print(red("Invalid choice."))
        except ValueError:
            print(red("Invalid input."))
        except IndexError:
             print(red("Invalid category selection."))