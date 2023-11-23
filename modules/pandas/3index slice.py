import pandas as pd

#indexing and slicing...
'''
DataFrame.head(num of rows)
    --fetch  the top records of data default rows=5
DataFrame.tail(num of rows)
    --fetch  the bottom records of data default rows=5
DataFrame.describe()
    --it would fetch the clear information of the following..
    --count, mean, std, min, 25%, 50%, 75%, max
DataFrame.shape
    --it would give the shape of data table ... rows and columns
DataFrame[start:stop:step]
DataFrame[column name]
DataFrame[[column_1, column_2]]
DataFrame[[column_1, column_2]][start:stop:step]
dataframe.iterrows()
    --it would give the information of the dataframe...
loc & iloc
'''

d = pd.read_csv("C:\\Users\\korad\\Desktop\\python examples\\modules\\pandas\\BILLIONAIRES.csv")
#creating DataFrame
df = pd.DataFrame(d)

#df.head() to get the top 5 records of the table
print("df.head() to get the top 5 records of the table")
print(df.head()) 
print()

#by deault head() contains top 5 records..
print("by deault head() contains top 5 records..")
print(df.head(7))
print()

#df.tail() to get the last records of dataframe..... by default 5 
print("df.tail() to get the last records of dataframe..... by default 5")
print(df.tail())
print()

print(df.tail(2))
print()

#df.describe() it would give clear information of the data..
print("df.describe() it would give clear information of the data..")
print(df.describe())
print()

#df.shape() gives the shape of dataframe..
print("df.shape() gives the shape of dataframe..")
print(df.shape)

#slicing..
print("slicing...")
print(df[:10:1])
print()


print(df["NAME"])
print()

#using double square square braces for multiple column records like 2D....
# df[[col1, col2, col3]][start:end:difference]
print(df[["NAME","AGE"]][:10:2])
print()


for i in df.iterrows():
    print(i)

print()


for i in df.itertuples():
    print(i)

