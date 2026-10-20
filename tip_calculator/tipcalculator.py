#It takes three inputs: the bill, the tip percentage and the number of people
#The formulas are:
#Tip = bill * percent / 100
#Total = bill + tip
#Per person = total / people


CURRENCY = "₦"

def ask_number(prompt, minimum, maximum) -> float:
    while True:
        try:
            value = float(input(prompt))
        except ValueError:
            print("Enter a number")
            continue
        if value < minimum or value > maximum:
            print(f"Enter a value from {minimum} to {maximum}.")
            continue

        return value

def calculate(bill, tip_percent, people):
    tip = bill * tip_percent / 100
    total = bill + tip
    per_person = total / people
    return round(tip, 2), round(total, 2 ), round(per_person, 2)

def show_result(bill, tip_percent, people, tip, total, per_person):
    print("**********RECEIPT**********")
    print(f"Total bill ********** {CURRENCY}{bill:.2f}")
    print(f"Tip {tip_percent}% ********** {CURRENCY}{tip:.2f}")
    print(f"Total ********** {CURRENCY}{total:.2f}")
    if people > 1:
        print(f"Per person ({people} people) ********** {CURRENCY}{per_person:.2f}")


"""print(calculate(100, 10, 2))
print(calculate(33.33, 0, 3))
print(show_result(100, 10, 2, 10, 500, 5))
"""
def main():
    print("**********WELCOME TO THE TIP CALCULATOR**********")
    while True:
        bill = ask_number("Bill: ", 0.01, 1_000_000)
        tip_percent = ask_number("Tip %: ", 0, 100)
        while True:
            people = ask_number("people: ", 1, 100)
            if people == int(people):
                people = int(people)
                break
            print("People must be a whole number.")

        tip, total, per_person = calculate(bill, tip_percent, people)
        show_result(bill, tip_percent, people, tip, total, per_person)

        redo = input("Calculate another(y/n)?: ").lower()
        if redo != "y":
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()

#print(ask_number("Test: ", 0, 100))

