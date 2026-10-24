import passwordgenerator

print(passwordgenerator.generate_password(9, ["uppercase", "lowercase", "digits", "punctuations"]))


"""test = []
add_expense(test, 2500, "Food", "Lunch")
add_expense(test, 800, "Transport", "Bus")

show_expenses(test)
show_expenses([])
"""

"""test = []
add_expense(test, 2500, "Food", "Lunch")
add_expense(test, 800, "Transport", "Bus")
add_expense(test, 1500, "Food", "Dinner")

print(total_spent(test))                 # 4800
print(totals_by_category(test))          # {'Food': 4000, 'Transport': 800}
print(len(filter_by_category(test, "Food")))  # 2
delete_expense(test, 0)
print(len(test))                         # 2

print(total_spent([]))                   # 0
print(totals_by_category([]))            # {}
print(filter_by_category([], "Food"))    # []"""

"""# Test 1: save, then load back
data = []
add_expense(data, 2500, "Food", "Lunch")
add_expense(data, 800, "Transport", "Bus")
save_expenses(data)
print(load_expenses())        # expect both expenses, not []

# Test 2: file missing
import os
os.remove(EXPENSES_FILE)
print(load_expenses())        # expect []

# Test 3: damaged file
with open(EXPENSES_FILE, "w") as f:
    f.write("hello")
print(load_expenses())        # expect []

# Test 4: valid JSON, but not a list
with open(EXPENSES_FILE, "w") as f:
    f.write('{"a": 1}')
print(load_expenses())        # expect []"""