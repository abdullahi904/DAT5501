def get_days_in_month():
    while True:
        try:
            n = int(input("How many days in the month (28-31): "))
            if 28 <= n <= 31:
                return n
            print("Please enter a number between 28 and 31.")
        except ValueError:
            print("Please enter a valid integer.")

def get_start_day():
    day_map = {
        "monday": 1, "mon": 1, "1": 1,
        "tuesday": 2, "tue": 2, "tues": 2, "2": 2,
        "wednesday": 3, "wed": 3, "weds": 3, "3": 3,
        "thursday": 4, "thu": 4, "thurs": 4, "4": 4,
        "friday": 5, "fri": 5, "5": 5,
        "saturday": 6, "sat": 6, "6": 6,
        "sunday": 7, "sun": 7, "7": 7
    }
    while True:
        s = input("What is the starting day of the week (Mon-Sun or 1-7): ").strip().lower()
        if s in day_map:
            return day_map[s]
        print("Please enter a day name (Mon, Tue, Wed, Thu, Fri, Sat, Sun) or a number 1-7 (Mon=1 ... Sun=7).")

def print_calendar(days_in_month, start_day):
    print("Mo Tu We Th Fr Sa Su")
    print("   " * (start_day - 1), end="")
    for day in range(1, days_in_month + 1):
        print(f"{day:2} ", end="")
        if (start_day - 1 + day) % 7 == 0:
            print()
    print()

def main():
    days = get_days_in_month()
    start_day = get_start_day()
    print_calendar(days, start_day)

if __name__ == "__main__":
    main()