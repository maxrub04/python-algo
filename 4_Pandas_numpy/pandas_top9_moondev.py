import pandas as pd

# how to turn csv into dataframe
df = pd.read_csv("XAU_15m_data1.csv",sep=';',encoding="utf-8")
print(df.tail())
print(df.columns)


#how to drop a column in pandas
#df = df.drop("Date", axis=1)
#print("\nAfter dropping Date column:")
#print(df.tail())


# how to rename a column in pandas
#df = df.raname(columns={"Volume":"Vol"})
#print("\nAfter renaming Volume column to Vol:")
#print(df.tail())


# how do you change the index
df = df.set_index("Date")
print("\nAfter changing index:")
print(df.tail())

# how to reset the index of a dataframe
df=df.reset_index()
print("\nAfter resetting index:")
print(df.tail())


# how to make a dataFrame from scratch
df2 = pd.DataFrame({
    "Name":["John","Mary","Lisa","Anna","Anna"],
    "Food":["food","food","food","chair","chair"],
    "Age":[25,30,28,32,32]})
print("\nDataFrame from scratch:")
print(df2)

# how to drop duplicates
df2 = df2.drop_duplicates()
print("\nAfter dropping duplicates:")
print(df2)