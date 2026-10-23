Expense Tracker

A command-line expense tracker in Python. Add expenses, view them, filter by category, see totals, and delete entries. Data is saved to a JSON file, so it is still there the next time you run it.

Features
Add an expense with amount, category and description (the date is set automatically)
View all expenses, or only one category
Totals per category and overall
Spending for the current month
Delete an expense with confirmation
Input validation: bad input is rejected and asked again, never a crash
Corrupted or missing data file starts a fresh list
Requirements
Python 3.12 or later
No external packages
How to run
python tracker.py
Example
**********EXPENSE TRACKER**********
1: Add an expense.
2: View all expenses.
...
Select one: 2
**********ALL EXPENSES**********
1 | 2026-10-23 | Transport | Bike ride | ₦500.00
How data is stored

Each expense is a dictionary with four keys: amount, category, description and date. All expenses are kept in one list and saved to expenses.json, which is created on the first save and is not tracked by git.

Notes
Categories come from a fixed list, so typos can't create new ones.
Change the currency symbol in the CURRENCY constant.