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
    for exp in expenses:  #loops through all expenses and adds them to the corresponding category
        amount_by_category[exp.category] = amount_by_category.get(exp.category, 0.0) + exp.amount

    now = datetime.datetime.now()  #to get the current date and time
    days_in_month = calendar.monthrange(now.year, now.month)[1]
    remaining_days = days_in_month - now.day + 1  # +1 is done to ensure that the calculation includes the current day 
    
    daily_budget = 0.0
    if remaining_days > 0:
        daily_budget = remaining_budget / remaining_days  #Checks if there are any days left. If so, it calculates the Required Daily Budget by dividing the remaining_budget by the remaining_days
    
    return {
        'total_spent': total_spent,
        'remaining_budget': remaining_budget,
        'daily_budget': daily_budget,
        'remaining_days': remaining_days,
        'category_totals': amount_by_category,
        'overspent': overspent
    }

def detect_overspending(summary: Dict[str, Any]):
    if summary['overspent']:  #Checks the overspent flag. If true, it triggers an overspending alert
        print(red(f"\n🚨 OVERSPENDING ALERT! You are Rs{abs(summary['remaining_budget']):.2f} over your Rs{BUDGET:.2f} budget!"))
    elif summary['daily_budget'] < 0:  #If the user is not yet over budget but the calculated daily_budget is negative, it means they have spent too fast and must now stop spending to avoid exceeding the budget. This triggers a red WARNING
         print(red(f"\n⚠️ WARNING: Your required daily budget is negative! Need to stop spending."))
