import scipy.signal as signal
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Create test data
dates = pd.date_range(start="2023-01-01", periods=50, freq="D")
prices = np.random.normal(loc=35000, scale=500, size=50)
df = pd.DataFrame({"Date": dates, "Price": prices})
df.set_index("Date", inplace=True)

# Extract price values as numpy array
prices_array = df["Price"].values

# Find local maximums using scipy.signal.find_peaks
# distance=5 specifies minimum distance between maximums
peaks, _ = signal.find_peaks(prices_array, distance=5)

# Create plot
plt.figure(figsize=(10, 5))
plt.plot(df.index, prices_array, label="Price", marker="o")
plt.plot(df.index[peaks], prices_array[peaks], "rv", label="Local Maxima")
plt.title("Double Top")
plt.xlabel("Date")
plt.ylabel("Price (USD)")
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()