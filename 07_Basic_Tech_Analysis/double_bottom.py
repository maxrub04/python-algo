import scipy.signal as signal
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dates = pd.date_range(start="2023-01-01", periods=50, freq="D")
prices = np.random.normal(loc=35000, scale=500, size=50)
df = pd.DataFrame({"Date": dates, "Price": prices})
df.set_index("Date", inplace=True)


# Extract price values from the "Price" column as a numpy array
prices_array = df["Price"].values

# Invert the price values to find minimums by searching for maximums
inverted_prices = -prices_array
# Find local minimums using scipy.signal.find_peaks
# distance=5 specifies minimum distance between minimums
peaks, _ = signal.find_peaks(inverted_prices, distance=5)



plt.figure(figsize=(10, 5))
plt.plot(df.index, prices_array, label="Price", marker="o")
plt.plot(df.index[peaks], prices_array[peaks], "rv", label="Local Minimials")
plt.title("double bottom")
plt.xlabel("Date")
plt.ylabel("Price (USD)")
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()