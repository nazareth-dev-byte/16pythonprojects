"""# Currency converter: converts an amount between currencies.
# Rates are stored in the RATES dictionary.
# Each value is how many units of that currency equal 1 US dollar.
# Rates are fixed (typed in by hand) and go stale over time.
# Rates typed in on: 2026-10-20 (placeholders from ~5 Aug 2026, verify)

RATES = {
    "USD": 1,
    "NGN": 1362.48,
    "EUR": 0.8666,
    "GBP": 0.7430,
}


def convert(amount, from_code, to_code):
    dollars = amount / RATES[from_code]
    result = dollars * RATES[to_code]
    return round(result, 2)


def ask_amount():
    while True:
        try:
            value = float(input("Enter the amount: "))
        except ValueError:
            print("Only digits allowed.")
            continue
        if value <= 0:
            print("Amount must be above 0.")
            continue
        return value

def ask_currency(prompt):





#print(convert(3, "NGN", "USD"))


"""