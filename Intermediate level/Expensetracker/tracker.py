
# Expense tracker: records and summarises daily spending.
# Each expense is a dictionary with four keys:
#   "amount" (number), "category" (text),
#   "description" (text), "date" (text, e.g. "2026-10-21")
# All expenses are kept in one list.
# The list is saved to expenses.json


import json
from datetime import date

EXPENSES_FILE = "expenses.json"
CURRENCY = "₦"
CATEGORIES = ["Food", "Transport", "Bills", "Entertainment", "Other"]


def add_expense(expenses, amount, category, description):
    expense = {"amount": amount,
              "category": category,
              "description":description,
              "date": (date.today().isoformat()),
               }
    expenses.append(expense)
def delete_expense(expenses, index):
    expenses.pop(index)


def total_spent(expenses):
    total = 0
    if not expenses:
        return 0
    for item in expenses:
        total += item["amount"]
    return total


def totals_by_category(expenses):
    total = {}
    for item in expenses:
        category = item["category"]
        amount = item["amount"]
        total[category] = total.get(category, 0) + amount
    return total


def filter_by_category(expenses, category):
    pile = []
    for item in expenses:
        if category == item["category"]:
            pile.append(item)
    return pile


def  save_expenses(expenses):
    file_path = EXPENSES_FILE
    with open(file = file_path, mode = "w") as file:
        json.dump(expenses, file)


def load_expenses():
    try:
        file_path = EXPENSES_FILE
        with open(file=file_path, mode="r") as file:
            explist = json.load(file)
            if not isinstance(explist, list):
                return []
        return explist
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []


def ask_amount():
    while True:
        amount = input("Please enter the amount: ").strip()
        try:
            amount = float(amount)
        except ValueError:
            print("Error: Invalid input! Please enter a valid  number (e.g., 500, 1500).")
            continue
        if amount <= 0:
            print("Input must be greater than 0")
            continue
        return amount


def ask_description():
    while True:
        description = input("Please enter the description: ").strip()
        if not description:
            print("Description cannot be empty, please input a valid description!")
            continue
        return description



def choose_category():
    for number, name in enumerate(CATEGORIES, start = 1):
        print(f"{number}. {name}")
    while True:
        try:
            choice = int(input("Please choose a category: "))
        except ValueError:
            print("Error: Invalid input! Please enter a valid whole number")
            continue
        if not (1 <= choice <= len(CATEGORIES)):
            print("That number is not part of the options.")
            continue
        return CATEGORIES[choice - 1]



def ask_index(expenses):
    if not expenses:
        print("Expenses cannot be empty.")
        return None
    try:
        index = input("Please enter the expense number to delete: ")
        index = int(index)
        if index > len(expenses):
            print("Value cannot exceed number of available expenses.")
            return None
        if index < 1:
            print("Number must be 1 or more.")
            return None
    except ValueError:
        print("Error: Invalid input! Please enter a valid whole number.")
        return None
    return index - 1


def show_expenses(expenses):
    if not expenses:
        print("No expenses recorded yet")
        return
    for number, expense in enumerate(expenses, start = 1):
        print(f"{number} | {expense["date"]} | {expense["category"]} | {expense["description"]} | {CURRENCY}{expense["amount"]:,.2f}")




def show_totals(expenses):
    if not expenses:
        print("No expenses recorded yet")
        return
    totals = totals_by_category(expenses)
    for category, amount in totals.items():
        print(f"{category}: {CURRENCY}{amount:,.2f}")
    print(f"Total: {CURRENCY}{total_spent(expenses):,.2f}")



def spending_this_month(expenses):
    today_month = date.today().isoformat()[:7]
    total = 0
    for expense in expenses:
        if expense["date"][:7] == today_month:
            total += expense["amount"]
    return total

def main():
    expenses = load_expenses()
    while True:
        menu = {1:"Add an expense.",
                2:"View all expenses.",
                3:"View expenses by category.",
                4:"See totals per category.",
                5:"Delete an expense",
                6:"View expense for the month",
                0:"Quit."}
        print("**********EXPENSE TRACKER**********")
        for key, value in menu.items():
            print(f"{key}: {value}")
        print("************************************")
        choice2 = input("Select one: ")

        if choice2 == "1":
            amount = ask_amount()
            category = choose_category()
            description = ask_description()
            add_expense(expenses, amount, category, description)
            save_expenses(expenses)
            print("Expense added!")

        elif choice2 == "2":
            print("**********ALL EXPENSES**********")
            show_expenses(expenses)
            print("************************************")

        elif choice2 == "3":
            category = choose_category()
            print(f"**********{category.upper()} EXPENSES**********")
            category_specs = filter_by_category(expenses, category)
            show_expenses(category_specs)
            print("************************************")

        elif choice2 == "4":
            print("**********TOTALS**********")
            show_totals(expenses)
            print("**************************")

        elif choice2 == "5":
            if not expenses:
                print("No expenses recorded yet")
                continue
            print("**********ALL EXPENSES**********")
            show_expenses(expenses)
            print("************************************")
            index = ask_index(expenses)
            if index is None:
                continue
            confirmation = input("Are you sure?(y/n): ")
            if confirmation == "y":
                delete_expense(expenses, index)
                save_expenses(expenses)
                print("Expense deleted.")
            else:
                print("Expense not deleted")


        elif choice2 == "6":
            stm = spending_this_month(expenses)
            print(f"This month: {CURRENCY}{stm:,.2f}")

        elif choice2 == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice(select on of the available options).")
            continue

if __name__ == "__main__":
    main()



