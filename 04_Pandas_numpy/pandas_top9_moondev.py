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

# drop dupes based on columns
df2=df2.drop_duplicates(subset=["Food"])
print("\nAfter dropping duplicates based on columns:")
print(df2)

# how to goupby in pandas
df3 = pd.DataFrame({
    "Food":["chicken","chicken","bacon","ranch"],
    "Cals":[500.,390.,600.,52.]
})

print("\nDataFrame:")
print(df3)

df3=df3.groupby("Food").mean()
print("\nAfter grouping by Food:")
print(df3)

# how to FILTER !!!!!

df4 = pd.read_csv("XAU_15m_data1.csv",sep=';',encoding="utf-8")
print(df4)

df4=df4[df4["High"]>2500]
print("\nAfter filtering:")
print(df4)

# use multiple operators
df4= df4[(df4["High"]>2500) & (df4["Volume"]>1000)]
print("\nAfter filtering with multiple operators:")
print(df4)

# filter with a list...
highs =[2500.35,2506.19,2797.51,2300,2500]
df4=df4[df4["High"].isin(highs)]
print("\nAfter filtering with a list:")
print(df4)


# if we want the largets
df4=df4.nsmallest(5,"High") #nlargest
print("\nAfter filtering with a list:")
print(df4)

# if we want specific olumns

df = df.iloc[4:8,:]
print("\nAfter filtering with a list:")
print(df)

# HOW TO SORT IN PANDAS

df5 = pd.read_csv("XAU_15m_data1.csv",sep=';',encoding="utf-8")
df5 = df5.sort_values(by="High", ascending=False)
print("\nAfter sorting:")
print(df5)

# sort by multiple

df5 = df5.sort_values(by=["High","Volume"], ascending=[False,True])
print("\nAfter sorting by multiple:")
print(df5)


# how to read excel files

df6= pd.read_excel("Sea Service Record.xlsx", index_col=0)
print("\nAfter reading excel file:")
print(df6)
