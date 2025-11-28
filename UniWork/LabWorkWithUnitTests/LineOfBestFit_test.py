import unittest
import numpy as np

# Prevent plot windows during import
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.show = lambda: None  # no-op

from LineOfBestFit import months, sales, coefficients, slope, intercept, best_fit_line

class my_unit_tests(unittest.TestCase):
    def test_coefficients(self):
        # Expect a perfect linear fit: sales = 20 * month + 80
        self.assertAlmostEqual(slope, 20.0, places=7)
        self.assertAlmostEqual(intercept, 80.0, places=7)
        self.assertEqual(len(coefficients), 2)
        self.assertAlmostEqual(coefficients[0], 20.0, places=7)
        self.assertAlmostEqual(coefficients[1], 80.0, places=7)

    def test_best_fit_line_matches_sales(self):
        # Since data is perfectly linear, best fit line should equal sales
        self.assertTrue(np.allclose(best_fit_line, sales))

    def test_shapes(self):
        self.assertEqual(months.shape, sales.shape)
        self.assertEqual(best_fit_line.shape, months.shape)

if __name__ == "__main__":
    unittest.main()