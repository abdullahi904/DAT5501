import numpy as np
import matplotlib.pyplot as plt
months = np.array([1, 2, 3, 4, 5, 6])
sales = np.array([100, 120, 140, 160, 180, 200])
# Calculate the line of best fit
plt.scatter(months, sales, color='blue', label='Sales Data')
coefficients = np.polyfit(months, sales, 1)  # 1 means linear
slope, intercept = coefficients
best_fit_line = slope * months + intercept
plt.plot(months, best_fit_line, color='red', label='Best Fit Line')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.title('Monthly Sales with Best Fit Line')
plt.legend()
plt.show()
