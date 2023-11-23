import pandas as pd

'''
dataframe.sort_values["column_name"]
dataframe.sort_value("column_name")
dataframe.sort_value("column_name" asscending=False)  ...descending order
dataframe.sort_value( ["column_name1", "col_2"] )
if we assign two column names... we must define in square braces...

'''

d = pd.read_csv("C:\\Users\\korad\\Desktop\\python examples\\modules\\pandas\\BILLIONAIRES.csv")
#creating DataFrame
df = pd.DataFrame(d)


print(df.sort_values("AGE", ascending=False))
print()

# if we assign two column names... we must define in square braces...

print(df.head(15).sort_values(["AGE", "RANK"] ,ascending=False))
