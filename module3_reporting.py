import datetime
from typing import Dict, Any, List
from data_model import Expense, BUDGET, green, red, yellow  #Imports the BUDGET value and the color functions

def display_report(summary: Dict[str, Any]):
    total_spent = summary['total_spent']  #Pulls the necessary key values (total spent, remaining budget, daily budget, remaining days) out of the input summary dictionary
    remaining_budget = summary['remaining_budget']
    daily_budget = summary['daily_budget']
    remaining_days = summary['remaining_days']

    print(yellow("\n" + "-"*40))
    print(yellow(f"💰 MONTHLY BUDGET REPORT ({datetime.date.today().strftime('%b %Y')})"))
    print(yellow("-"*40))
    
    print(f"💵 Total Budget: Rs.{BUDGET:.2f}")
    print(f"💸 Total Spent: Rs.{total_spent:.2f}")

    if summary['overspent']:
        budget_status = red(f"❌ Budget Remaining: Rs.{remaining_budget:.2f} (OVER BUDGET)")
    else:
        budget_status = green(f"✅ Budget Remaining: Rs.{remaining_budget:.2f}")
    print(budget_status)

    if remaining_days > 0 and daily_budget > 0:
        daily_status = green(f"👉 Daily Budget (Days Left: {remaining_days}): Rs.{daily_budget:.2f}")
    elif remaining_days > 0 and daily_budget <= 0:
        daily_status = red(f"🛑 Required Daily Budget: Rs.{daily_budget:.2f} (Need to save!)")
    else:
        daily_status = "✨ End of month! All budgeting complete."
    print(daily_status)
    
    print("-" * 40)

def display_analytics(summary: Dict[str, Any]):
    category_totals = summary['category_totals']
    total_spent = summary['total_spent']
    
    print(yellow("\n📈 WHERE DID THE MONEY GO?"))
    
    if not category_totals:
        print("No expenses recorded yet.")
        return
        
#Takes the category totals and sorts them from largest spending amount to smallest (descending order).
    sorted_categories = sorted(category_totals.items(), key=lambda item: item[1], reverse=True)

    for category, amount in sorted_categories:
        percentage = (amount / total_spent) * 100 if total_spent > 0 else 0
        bar_length = int(percentage // 5)
        bar = "█" * bar_length  #each block █ represents 5% of the total spent
        print(f"  {category:<10} | Rs.{amount:7.2f} ({percentage:4.1f}%) {yellow(bar)}")
        
def generate_monthly_report(expenses: List[Expense], summary: Dict[str, Any]):
    display_report(summary)  #Simply calls the two main display functions in sequence to build the final report shown to the user.
    print("\n" + "-"*40)
    display_analytics(summary)
