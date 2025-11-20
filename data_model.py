import sqlite3
import datetime

DB_FILE = 'expenses.db'
BUDGET = 2000.00
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

    def __repr__(self):
        return f"Expense(ID={self.id}, Name='{self.name}', Amount=Rs.{self.amount:.2f}, Category='{self.category}', Date='{self.date}')"

def green(text: str) -> str:
    return f"\033[92m{text}\033[0m"

def red(text: str) -> str:
    return f"\033[91m{text}\033[0m"

def yellow(text: str) -> str:
    return f"\033[93m{text}\033[0m"

def setup_db():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            amount REAL NOT NULL,
            category TEXT NOT NULL,
            date TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

setup_db()