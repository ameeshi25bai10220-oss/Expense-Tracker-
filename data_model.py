import sqlite3
import datetime

DB_FILE = 'expenses.db'  #defines the filename for the SQLite db, also used in Module1
BUDGET = 2000.00  #set a budget limit
CATEGORIES = [
    "🍔 Food",
    "🏠 Home",
    "💼 Work",
    "✈️ Travel",
    "💡 Bills",
    "🎉 Fun",
    "✨ Misc",
]

class Expense:
    def __init__(self, name: str, amount: float, category: str, date: str = None, id: int = None):
        self.id = id
        self.name = name
        self.amount = amount
        self.category = category
        self.date = date if date else datetime.date.today().isoformat()

    def __repr__(self):  #Defines how the object should be printed when debugging or inspected (e.g., Expense(ID=1, Name='Rent'
        return f"Expense(ID={self.id}, Name='{self.name}', Amount=Rs.{self.amount:.2f}, Category='{self.category}', Date='{self.date}')"
#Color Utility: Returns the input text wrapped in ANSI escape codes that make the text appear green, red or yellow in the terminal.
def green(text: str) -> str:
    return f"\033[92m{text}\033[0m"

def red(text: str) -> str:
    return f"\033[91m{text}\033[0m"

def yellow(text: str) -> str:
    return f"\033[93m{text}\033[0m"

def setup_db():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor() #Connects to the database file. If the file doesn't exist, SQLite automatically creates it.
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            amount REAL NOT NULL,
            category TEXT NOT NULL,
            date TEXT NOT NULL
        )
    """)
    conn.commit()  #Saves the table creation structure to the database file.
    conn.close()

setup_db()  #executes i.e. Calls the function immediately when the file is loaded, ensuring the database table is prepared before any other module tries to read or write data.
