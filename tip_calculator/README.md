Tip Calculator

A command-line tip calculator in Python. Enter a bill, a tip percentage and the number of people. It prints a receipt with the tip, the total and the amount per person.

Features
Input validation: letters and out-of-range values are rejected and re-asked
Tip from 0 to 100%
Whole-number check for people
Per-person amount shown only when splitting between 2 or more people
Calculate again without restarting
Requirements
Python 3.8 or later
No external packages
How to run
python tipcalculator.py
Example
**********WELCOME TO THE TIP CALCULATOR**********
Bill: 100
Tip %: 10
people: 2
**********RECEIPT**********
Total bill ********** ₦100.00
Tip 10.0% ********** ₦10.00
Total ********** ₦110.00
Per person (2 people) ********** ₦55.00
Calculate another(y/n)?: n
Goodbye!
Notes
The bill must be above 0. A tip of 0 is allowed.
Change the currency symbol in the CURRENCY constant.