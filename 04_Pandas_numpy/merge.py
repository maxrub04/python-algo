import pandas as pd

df1 = pd.DataFrame({
"Asset": ["Bitcoin", "Ethereum"],
"Price": [35000, 2200]
})
df2 = pd.DataFrame({
"Asset": ["Litecoin"],
"Price": [150]
})
#  (concatenation)
df_combined = pd.concat([df1, df2], ignore_index=True)
print("Conatenation DataFrame:\n", df_combined)




df_prices = pd.DataFrame({
"Asset": ["Bitcoin", "Ethereum", "Litecoin"],
"Price": [35000, 2200, 150]
})
df_volume = pd.DataFrame({
"Asset": ["Bitcoin", "Ethereum", "Litecoin"],
"Volume": [1200, 3000, 800]
})
# merge by column
df_merged = pd.merge(df_prices, df_volume, on="Asset")
print("Data:\n", df_merged)