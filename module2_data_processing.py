import calendar
import datetime
from typing import List, Dict, Union, Any
from data_model import Expense, BUDGET, green, red

def calculate_summary(expenses: List[Expense]) -> Dict[str, Any]:
    if not expenses:
        return {
            'total_spent': 0.0,
            'remaining_budget': BUDGET,
            'daily_budget': BUDGET / 30,
            'category_totals': {},
            'overspent': False
        }

    total_spent = sum(exp.amount for exp in expenses)
    remaining_budget = BUDGET - total_spent
    overspent = remaining_budget < 0

    amount_by_category: Dict[str, float] = {}
    for exp in expenses:
        amount_by_category[exp.category] = amount_by_category.get(exp.category, 0.0) + exp.amount

    now = datetime.datetime.now()
    days_in_month = calendar.monthrange(now.year, now.month)[1]
    remaining_days = days_in_month - now.day + 1
    
    daily_budget = 0.0
    if remaining_days > 0:
        daily_budget = remaining_budget / remaining_days
    
    return {
        'total_spent': total_spent,
        'remaining_budget': remaining_budget,
        'daily_budget': daily_budget,
        'remaining_days': remaining_days,
        'category_totals': amount_by_category,
        'overspent': overspent
    }

def detect_overspending(summary: Dict[str, Any]):
    if summary['overspent']:
        print(red(f"\n🚨 OVERSPENDING ALERT! You are Rs{abs(summary['remaining_budget']):.2f} over your Rs{BUDGET:.2f} budget!"))
    elif summary['daily_budget'] < 0:
         print(red(f"\n⚠️ WARNING: Your required daily budget is negative! Need to stop spending."))