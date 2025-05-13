# Determine support an
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dates = pd.date_range(start="2023-01-01", periods=50, freq="D")
prices = np.random.normal(loc=35000, scale=500, size=50)
df = pd.DataFrame({"Date": dates, "Price": prices})
df.set_index("Date", inplace=True)

N = 10
df["Min_N"] = df["Price"].rolling(window=N).min()
df["Max_N"] = df["Price"].rolling(window=N).max()
plt.figure(figsize=(10, 5))
plt.plot(df.index, df["Price"], label="Price", marker="o")
plt.plot(df.index, df["Min_N"], label=f"Minimum for {N} days", linestyle="--", color="green")
plt.plot(df.index, df["Max_N"], label=f"Maximum for {N} days", linestyle="--", color="red")
plt.title("Support and Resistance Levels")
plt.xlabel("Date")
plt.ylabel("Price (USD)")
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()