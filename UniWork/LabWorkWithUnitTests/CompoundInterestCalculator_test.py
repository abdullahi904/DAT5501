import unittest

from CompoundInterestCalculator import compound_yearly, years_to_double

class my_unit_tests(unittest.TestCase):
    def test_compound_yearly_basic(self):
        # one year at 5%
        self.assertAlmostEqual(compound_yearly(1000.0, 0.05, 1)[0], 1050.0, places=9)
        # zero rate over multiple years
        result = compound_yearly(500.0, 0.0, 3)
        self.assertEqual(len(result), 3)
        self.assertAlmostEqual(result[-1], 500.0, places=9)

    def test_compound_yearly_errors(self):
        with self.assertRaises(ValueError):
            compound_yearly(0.0, 0.05, 2)
        with self.assertRaises(ValueError):
            compound_yearly(1000.0, 0.05, 0)

    def test_years_to_double(self):
        self.assertEqual(years_to_double(1000.0, 0.05), 15)  # ~14.21 -> ceil 15
        self.assertEqual(years_to_double(1000.0, 0.10), 8)   # ~7.27 -> ceil 8

    def test_years_to_double_nonpositive_rate(self):
        self.assertIsNone(years_to_double(1000.0, 0.0))
        self.assertIsNone(years_to_double(1000.0, -0.01))

    def test_years_to_double_error_principal(self):
        with self.assertRaises(ValueError):
            years_to_double(0.0, 0.05)

if __name__ == "__main__":
    unittest.main()