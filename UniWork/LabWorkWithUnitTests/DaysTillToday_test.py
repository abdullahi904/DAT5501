from datetime import date, datetime
import unittest

# ----- code under test -----
def parse_date(s):
    s = s.strip()
    formats = [
        "%Y-%m-%d",  # 2024-11-20
        "%d/%m/%Y",  # 20/11/2024
        "%m/%d/%Y",  # 11/20/2024
        "%d-%m-%Y",  # 20-11-2024
        "%Y/%m/%d",  # 2024/11/20
    ]
    for fmt in formats:
        try:
            return datetime.strptime(s, fmt).date()
        except ValueError:
            continue
    raise ValueError("Unrecognized date format")

def main():
    while True:
        user_input = input("Enter a past date (e.g., YYYY-MM-DD or DD/MM/YYYY): ")
        try:
            input_date = parse_date(user_input)
            break
        except ValueError:
            print("Invalid date. Try formats like YYYY-MM-DD, DD/MM/YYYY, or MM/DD/YYYY.")
    
    today = date.today()
    delta_days = (today - input_date).days

    if delta_days > 0:
        print(f"It has been {delta_days} day(s) since {input_date.isoformat()}.")
    elif delta_days == 0:
        print("That date is today!")
    else:
        print(f"That date is in the future by {-delta_days} day(s).")

# ----- unit tests (simple, like the image) -----
class my_unit_tests(unittest.TestCase):
    def test_parse_date(self):
        # test valid formats
        self.assertEqual(parse_date("2024-11-20"), date(2024, 11, 20))
        self.assertEqual(parse_date("20/11/2024"), date(2024, 11, 20))
        self.assertEqual(parse_date("11/20/2024"), date(2024, 11, 20))
        self.assertEqual(parse_date("20-11-2024"), date(2024, 11, 20))
        self.assertEqual(parse_date("2024/11/20"), date(2024, 11, 20))
        self.assertEqual(parse_date(" 2024-11-20 "), date(2024, 11, 20))  # leading/trailing spaces

        # test invalid inputs
        with self.assertRaises(ValueError):
            parse_date("not a date")
        with self.assertRaises(ValueError):
            parse_date("")
        with self.assertRaises(ValueError):
            parse_date("2024.11.20")

# run the tests
if __name__ == "__main__":
    unittest.main()