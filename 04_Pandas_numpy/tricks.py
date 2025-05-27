import pandas as pd

# Create DataFrame with missing values

data = {
"Name": ["Bitcoin", "Ethereum", "Litecoin"],
"Price": [35000, 2200, 150],
"Volume": [1200, 3000, 800]
}
df = pd.DataFrame(data)

data_missing = {
"Asset": ["Bitcoin", "Ethereum", "Litecoin"],
"Price": [35000, None, 150],
"Volume": [1200, 3000, None]
}
df_missing = pd.DataFrame(data_missing)
print("Initial data with gaps:\n", df_missing)
print("Gap check:\n", df_missing.isnull())


#Filling in the missing values with the average value of the column
df_missing.fillna({"Price": df_missing["Price"].mean()}, inplace=True)
# Deleting rows with missing data
df_cleaned = df_missing.dropna()
print("Data after cleaning:\n", df_cleaned)


#Sorting and changing indexes


# Sorting DataFrame by ‘Price’ column
df_sorted = df.sort_values(by="Price", ascending=False)
print("Sorting by price:\n", df_sorted)
# Changing indices using the ‘Asset’ column
df_indexed = df.set_index("Name")
print("DataFrame with new index:\n", df_indexed)


