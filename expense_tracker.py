import json
from datetime import datetime

EXPENSE_FILE = "expenses.json"

def load_expenses():
    try:
        with open(EXPENSE_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_expenses(expenses):
    with open(EXPENSE_FILE, 'w') as file:
        json.dump(expenses, file, indent=2)

def add_expense():
    expenses = load_expenses()
    
    amount = float(input("Enter expense amount: $"))
    description = input("Enter description: ")
    category = input("Enter category (food/transport/entertainment/other): ").lower()
    
    expense = {
        "amount": amount,
        "description": description,
        "category": category,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M")
    }
    
    expenses.append(expense)
    save_expenses(expenses)
    print(f"✓ Added: ${amount} for {description}")

def view_all_expenses():
    expenses = load_expenses()
    if not expenses:
        print("No expenses recorded yet.")
        return
    
    display_expenses(expenses, "All Expenses")

def view_by_category():
    expenses = load_expenses()
    if not expenses:
        print("No expenses recorded yet.")
        return
    
    category = input("Enter category to filter by: ").lower()
    filtered = [exp for exp in expenses if exp['category'] == category]
    
    if not filtered:
        print(f"No expenses found for category: {category}")
        return
    
    display_expenses(filtered, f"Expenses for: {category.title()}")

def display_expenses(expenses, title):
    print(f"\n--- {title} ---")
    total = 0
    for expense in expenses:
        print(f"${expense['amount']:.2f} - {expense['description']} ({expense['category']}) - {expense['date']}")
        total += expense['amount']
    
    print(f"\nTotal: ${total:.2f}")

def show_summary():
    expenses = load_expenses()
    if not expenses:
        print("No expenses recorded yet.")
        return
    
    categories = {}
    for expense in expenses:
        cat = expense['category']
        categories[cat] = categories.get(cat, 0) + expense['amount']
    
    print("\n--- Spending Summary ---")
    total = 0
    for category, amount in categories.items():
        print(f"{category.title()}: ${amount:.2f}")
        total += amount
    
    print(f"\nGrand Total: ${total:.2f}")

def main():
    while True:
        print("\n--- Expense Tracker ---")
        print("1. Add expense")
        print("2. View all expenses")
        print("3. View by category")
        print("4. Spending summary")
        print("5. Exit")
        
        choice = input("Choose option: ")
        
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_all_expenses()
        elif choice == "3":
            view_by_category()
        elif choice == "4":
            show_summary()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()