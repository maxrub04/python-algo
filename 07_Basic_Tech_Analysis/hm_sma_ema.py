import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


dates =  pd.date_range(start="2023-01-01", periods=30, freq="D")
prices = np.random.normal(loc = 2200, scale=500, size=30)
df = pd.DataFrame({"Date": dates, "Price": prices})
df.set_index("Date", inplace=True)

df["SMA_5"] = df["Price"].rolling(window=5).mean()
df["EMA_5"] = df["Price"].ewm(span=5, adjust=False).mean()

plt.figure(figsize=(10, 5))
plt.plot(df.index, df["Price"], label="Price", marker="o")
plt.plot(df.index, df["SMA_5"], label="SMA (5)", linestyle="--")
plt.plot(df.index, df["EMA_5"], label="EMA (5)", linestyle=":")
plt.title("Moving Average")
plt.xlabel("Date")
plt.ylabel("Price (USD)")
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()