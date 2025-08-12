# Personal Expense Tracker
print("Expense Tracker Started")

def add_expense():
    amount = float(input("Enter expense amount: $"))
    description = input("Enter description: ")
    print(f"Added: ${amount} for {description}")

def main():
    print("1. Add expense")
    choice = input("Choose option: ")
    
    if choice == "1":
        add_expense()
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()