# Compound Interest Calculator (annual compounding)

import math

def compound_yearly(principal: float, annual_rate: float, years: int):
    """
    Calculate end-of-year balances with annual compounding.
    principal: starting amount (must be > 0)
    annual_rate: decimal rate per year (e.g., 0.05 for 5%)
    years: number of years (>= 1)
    Returns a list of floats, one per year.
    """
    if principal <= 0:
        raise ValueError("Principal must be greater than 0.")
    if years < 1:
        raise ValueError("Years must be at least 1.")
    balance = principal
    balances = []
    for _ in range(years):
        balance *= (1 + annual_rate)
        balances.append(balance)
    return balances

def years_to_double(principal: float, annual_rate: float):
    """
    Return the number of whole years needed for the principal to at least double,
    assuming annual compounding at annual_rate. Returns None if impossible
    (e.g., non-positive rate).
    """
    if principal <= 0:
        raise ValueError("Principal must be greater than 0.")
    if annual_rate <= 0:
        return None
    # Use logarithmic solution and round up to whole years
    years_needed = math.log(2) / math.log(1 + annual_rate)
    return math.ceil(years_needed)

def get_positive_float(prompt):
    while True:
        try:
            val = float(input(prompt))
            if val > 0:
                return val
            print("Please enter a number greater than 0.")
        except ValueError:
            print("Please enter a valid number.")

def get_nonnegative_float(prompt):
    while True:
        try:
            val = float(input(prompt))
            if val >= 0:
                return val
            print("Please enter a number 0 or greater.")
        except ValueError:
            print("Please enter a valid number.")

def get_int_at_least(prompt, minimum):
    while True:
        try:
            val = int(input(prompt))
            if val >= minimum:
                return val
            print(f"Please enter an integer >= {minimum}.")
        except ValueError:
            print("Please enter a valid integer.")

def main():
    print("Compound Interest Calculator (annual compounding)")
    principal = get_positive_float("Enter starting savings amount: ")
    rate_percent = get_nonnegative_float("Enter annual interest rate (%) e.g., 5 for 5%: ")
    years = get_int_at_least("Enter number of years: ", 1)

    rate = rate_percent / 100.0

    # Print balances for each year
    balances = compound_yearly(principal, rate, years)
    for i, bal in enumerate(balances, start=1):
        print(f"Year {i}: {bal:,.2f}")

    # Print years to double
    double_years = years_to_double(principal, rate)
    if double_years is None:
        print("At this interest rate, the savings will not double.")
    else:
        print(f"It will take about {double_years} year(s) for the savings to double.")

if __name__ == "__main__":
    main()
    