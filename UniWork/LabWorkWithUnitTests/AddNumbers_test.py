import unittest

from AddNumbers import add

class my_unit_tests(unittest.TestCase):
    def test_add_negative(self):
        self.assertEqual(add(-1, 5), 4)

    def test_add_floats(self):
        self.assertEqual(add(2.5, 3.1), 5.6)

if __name__ == "__main__":
    unittest.main()