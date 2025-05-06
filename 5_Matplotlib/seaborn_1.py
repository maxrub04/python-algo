import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Day":[1,2,3,4,5],
    "Price":[100,105,110,115,110]#[3300,3150,2900,3200,3100]
}
df = pd.DataFrame(data)

plt.figure(figsize=(10,6))
sns.regplot(x="Day", y="Price", data=df,marker="o",color="g")
plt.title("Price change over 5 days")
plt.xlabel("Days")
plt.ylabel("USD")
plt.grid(True)
plt.show()



data_box = {
    "Asset":["BTC","BTC","BTC","ETH","ETH","ETH"],
    "Price":[33000,35000,32000,2900,3100,3200]
}

df_box = pd.DataFrame(data_box)

plt.figure(figsize=(10,6))
sns.barplot(x="Asset", y="Price", data=df_box,color="skyblue")
plt.title("Assets Price")
plt.xlabel("Asset")
plt.ylabel("Price")
plt.show()


dates = pd.date_range(start="2023-01-01", periods=10, freq="D")
prices = [35000, 35200, 34900, 35100, 35300, 35500, 35400, 35600, 35700, 35900]
df_time = pd.DataFrame({"Date": dates, "Price": prices})

plt.figure(figsize=(10, 5))
plt.plot(df_time["Date"], df_time["Price"], marker="o", linestyle="-", color="purple")
plt.title("Price Change Over Time")
plt.xlabel("Date")
plt.ylabel("Price (USD)")
plt.xticks(rotation=45) #Rotation of X-axis labels for better readability
plt.tight_layout() #Eliminates problems with the overlay of elements
plt.grid(True)
plt.show()