import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#Moving Average Convergence Divergence)


dates = pd.date_range(start="2023-01-01", periods=30, freq="D")
prices = np.random.normal(loc=35000, scale=500, size=30)
df = pd.DataFrame({"Date": dates, "Price": prices})
df.set_index("Date", inplace=True)


# MACD = EMA(12) - EMA(26)
df["EMA_12"] = df["Price"].ewm(span=12, adjust=False).mean()
df["EMA_26"] = df["Price"].ewm(span=26, adjust=False).mean()
df["MACD"] = df["EMA_12"] - df["EMA_26"]

# Signal line MACD:
df["Signal"] = df["MACD"].ewm(span=9, adjust=False).mean()
df["Histogram"] = df["MACD"] - df["Signal"]
plt.figure(figsize=(10, 6))


# MACD and signal line chart
plt.subplot(2, 1, 1)
plt.plot(df.index, df["MACD"], label="MACD", color="blue")
plt.plot(df.index, df["Signal"], label="Signal Line", color="orange")
plt.title("MACD и signal line")
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)


# Histogram of MACD and signal line difference
plt.subplot(2, 1, 2)
plt.bar(df.index, df["Histogram"], label="Histogram", color="gray")
plt.title("Histogram MACD")
plt.xlabel("Date")
plt.ylabel("Price")
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()