import pandas as pd


df_csv=pd.read_csv("forex_data.csv", encoding="utf-8")
print("First 5 rows: ",df_csv.head(),end="\n\n")
print("Description: ",df_csv.describe(), end="\n\n")
print("General Info: ",df_csv.info(), end="\n\n")
"""print("Null values: ",df_csv.isnull().sum())
print("Unique values: ",df_csv.nunique())
print("Sum: ",df_csv.sum())
print("Mean: ",df_csv.mean())
print("Median: ",df_csv.median())
print("Mode: ",df_csv.mode())
print("Standard Deviation: ",df_csv.std())
print("Variance: ",df_csv.var())
print("Correlation: ",df_csv.corr())
print("Data types: ",df_csv.dtypes)
print("Shape: ",df_csv.shape)
print("Index: ",df_csv.index)
print("Columns: ",df_csv.columns)
print("Values: ",df_csv.values)
print("Info: ",df_csv.info())
print("Null values: ",df_csv.isnull().sum())
print("Unique values: ",df_csv.nunique())
print("Sum: ",df_csv.sum())"""


filted_df=df_csv[df_csv["price"]>1]
print("Filtered data:\n",filted_df)

df_csv["price_category"] = pd.cut(df_csv["price"], bins=[0, 1, 10, 1000],
labels=["Low", "Mid", "High"])
print("DataFrame with categories:\n", df_csv)

#gropued = df_csv.groupby("price_category")["price"].mean()["volume"].sum()
grouped = df_csv.groupby("price_category").agg({
    "price": "mean",
    "volume": "sum"
})
print("Sum volume and mean price by categories:\n", grouped)

df = pd.DataFrame({
    "pair": ["EUR/USD", "USD/JPY", "GBP/USD", "AUD/USD", "USD/CHF"],
    "price": [1.1, None, 1.24, 0.67, None],
    "volume": [1000000, 2000000, None, 1200000, 800000]
})

print("\nAmount of missing data:\n", df.isnull().sum())
print("\n Statistics:\n", df.describe())


df_filled = df.copy()
df_filled["price"].fillna(df["price"].mean(), inplace=True)
df_filled["volume"].fillna(df["volume"].mean(), inplace=True)

print("\nFilled mising parts:\n", df_filled)
print("\nStatistics after:\n", df_filled.describe())

