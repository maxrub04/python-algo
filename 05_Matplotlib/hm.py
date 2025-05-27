import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns


"""pd = pd.read_csv("forex_data.csv", encoding="utf-8")
plt.figure(figsize=(10, 6))
plt.title("Forex Data")
plt.xlabel("Date")
plt.ylabel("Price")
plt.plot(pd["date"], pd["price"], marker="o", linestyle="-", color="purple")
plt.grid(True)
plt.show()



price_sample=np.random.normal(3500,1000,10000)
plt.figure(figsize=(10,6))
plt.hist(price_sample,bins=100,color="skyblue",edgecolor="black",label="Price sample")
plt.title("Price sample")
plt.xlabel("USD")
plt.ylabel("Frequency")
plt.legend()
plt.show()


days = [1, 2, 3, 4, 5]
price_1=[35000, 35200, 35100, 35300, 35500]
price_2=[40000, 38000, 35100, 32000, 30000]
plt.figure(figsize=(10, 5))
plt.plot(days, price_1, marker="o", linestyle="-", color="blue", label="Asset 1")
plt.plot(days, price_2, marker="s", linestyle="--", color="red", label="Asset 2")
plt.annotate("Trend Crossing", xy=(3, 35100), xytext=(3, 36000),arrowprops=dict(facecolor="black",shrink=0.02))
plt.title("Price comparison by day")
plt.xlabel("Day")
plt.ylabel("Price")
plt.legend()
plt.show()"""


dates = [1,2,3,4,5,6,7,8,9,10]
prices = np.random.normal(loc=3500, scale=200, size=10)

df = pd.DataFrame({"Date": dates, "Price": prices})


df["SMA_5"] = df["Price"].rolling(window=5).mean()

plt.figure(figsize=(12, 6))
sns.regplot(data=df, x="Date", y="Price", marker="o", label="Regression Line", color="blue")

plt.plot(df["Date"], df["Price"], label="Price", color="gray")
plt.plot(df["Date"], df["SMA_5"], label="5-Day SMA", color="orange")

plt.title("Time Series with Regression and Moving Average")
plt.xlabel("Date")
plt.ylabel("Price")
plt.legend()
plt.grid(True)
plt.show()
plt.savefig("chart.png")