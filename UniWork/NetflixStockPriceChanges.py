import pandas as pd
import numpy as np
import time
import matplotlib.pyplot as plt

# Load Netflix stock data
data = pd.read_csv(r"C:\Users\agedow001\Downloads\HistoricalData_1762773013086(HistoricalData_1762773013086).csv")

# Sort by date if available
if "Date" in data.columns:
    data["Date"] = pd.to_datetime(data["Date"])
    data = data.sort_values("Date")

# Calculate daily price change: P(N+1) - P(N)
prices = data["Close/Last"]
raw_prices = []
for price in prices:
    price = price.replace('$', '')
    number_price = float(price)
    raw_prices.append(number_price)

print(raw_prices[:5])

prices = np.array(prices)
price_change = np.diff(raw_prices)

# Test different sample sizes
sample_sizes = [10, 20, 30, 40, 50, 60, 70 , 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250]
times = []

# Measure sorting time for each n
for n in range(len(price_change)):
    sample = price_change[0 :n]
    elapsed_average = 0.0

    for m in range(5):

        start = time.perf_counter()
        np.sort(sample)
        end = time.perf_counter()

        elapsed = end - start
        elapsed_average = [elapsed]
    elapsed = sum(elapsed_average) / (len(elapsed_average))
    times.append(elapsed)
    print(f"n = {n:4d} → sort time = {elapsed:.8f} seconds")

# Plot sorting time vs n
plt.figure(figsize=(8, 5))
plt.plot(range(len(price_change)), times, marker="o", color="blue")
plt.title("Sorting Time vs Number of Price Changes (Netflix)")
plt.xlabel("Number of Data Points (n)")
plt.ylabel("Time to Sort (seconds)")
plt.grid(True)
plt.show()