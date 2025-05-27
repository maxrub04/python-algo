import pandas as pd
import matplotlib.pyplot as plt

df_price = pd.DataFrame({
    "Asset": ["Bitcoin", "Ethereum", "Cardano", "Solana"],
    "Price": [35000, 2500, 0.4, 90]
})

df_volume = pd.DataFrame({
    "Asset": ["Bitcoin", "Ethereum", "Cardano", "Solana"],
    "Volume": [50000000, 30000000, 10000000, 15000000]
})

df_merged = pd.merge(df_price, df_volume, on="Asset")

print("Merged:\n", df_merged)


correlation = df_merged[["Price", "Volume"]].corr()
print("\nCorrelation between price and volume:\n", correlation)


plt.scatter(df_merged["Price"], df_merged["Volume"])
plt.title("Correlation between price and volume")
plt.xlabel("Price")
plt.ylabel("Volume")
plt.grid(True)
plt.show()