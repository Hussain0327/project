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
    category = input("Enter category (food/transport/entertainment/other): ")
    
    expense = {
        "amount": amount,
        "description": description,
        "category": category,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M")
    }
    
    expenses.append(expense)
    save_expenses(expenses)
    print(f"✓ Added: ${amount} for {description}")

def view_expenses():
    expenses = load_expenses()
    if not expenses:
        print("No expenses recorded yet.")
        return
    
    total = 0
    for expense in expenses:
        print(f"${expense['amount']:.2f} - {expense['description']} ({expense['category']}) - {expense['date']}")
        total += expense['amount']
    
    print(f"\nTotal spent: ${total:.2f}")

def main():
    while True:
        print("\n--- Expense Tracker ---")
        print("1. Add expense")
        print("2. View all expenses")
        print("3. Exit")
        
        choice = input("Choose option: ")
        
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()