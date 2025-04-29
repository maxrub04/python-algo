import pandas as pd


data = {
"Name": ["Bitcoin", "Ethereum", "Litecoin"],
"Price": [35000, 2200, 150],
"Volume": [1200, 3000, 800]
}
df = pd.DataFrame(data)
print("DataFrame:\n", df)


df_csv = pd.read_csv("forex_data.csv", encoding="utf-8")
print("Data from CSV:\n", df_csv.head())


#Indexing, filtering and data aggregation in Pandas

prices = df["Price"]
print(f"Prices:\n{prices}")

print("Prices:\n" + df["Price"].to_string())

# Using loc (by index labels)
print("First row DataFrame:\n", df.loc[0])
print("Rows with index 0 и 1:\n", df.loc[0:1])
# Using iloc (by ordinal numbers)
print("Second row:\n", df.iloc[1])
print("Rows from 0 to 2:\n", df.iloc[0:2])


# filter
high_price = df[df["Price"] > 2000]
print("Price higher 2000:\n", high_price)

# volume filter
filtered_df = df[(df["Price"] > 150) & (df["Volume"] < 2000)]
print("Filter by price and volume:\n", filtered_df)


#Data grouping and aggregation



